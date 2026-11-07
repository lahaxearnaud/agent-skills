"""Exercise paired-evaluation integrity without contacting a model service."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RUNNER = HERE / "run_blind_evaluation.py"


class BlindEvaluationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(prefix="code-like-me-test-")
        self.addCleanup(self.tmp.cleanup)
        self.directory = Path(self.tmp.name)
        bindir = self.directory / "bin"
        bindir.mkdir()
        fake = bindir / "codex"
        fake.write_text('''#!/usr/bin/env python3
import os, pathlib, sys
prompt = sys.stdin.read()
mode = os.environ.get("STYLE_EVAL_FAKE_FAILURE")
if mode == "401":
    print("HTTP 401", file=sys.stderr)
    sys.exit(9)
if mode == "exit":
    sys.exit(9)
if mode == "timeout":
    import time
    time.sleep(3)
output = pathlib.Path(sys.argv[sys.argv.index("-o") + 1])
if mode != "missing":
    output.write_text("" if mode == "empty" else "Synthetic stub response\\n", encoding="utf-8")
output.with_suffix(".prompt").write_text(prompt, encoding="utf-8")
output.with_suffix(".args").write_text("\\n".join(sys.argv[1:]), encoding="utf-8")
output.with_suffix(".env").write_text(os.environ.get("GH_TOKEN", "not-present"), encoding="utf-8")
''', encoding="utf-8")
        fake.chmod(0o700)
        self.env = dict(os.environ, PATH=f"{bindir}{os.pathsep}{os.environ['PATH']}")

    def invoke(self, output: Path, *arguments: str, **environment: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(RUNNER), "--output-dir", str(output), *arguments, "--timeout", "1"],
            env=dict(self.env, **environment), text=True, capture_output=True, timeout=15,
        )

    def test_each_case_has_blinded_answers_and_only_treatment_has_profile(self) -> None:
        output = self.directory / "result"
        result = self.invoke(output, GH_TOKEN="synthetic-not-a-secret")
        self.assertEqual(result.returncode, 0, result.stderr)
        key = json.loads((output / "key.json").read_text())
        self.assertEqual(len(key["cases"]), 4)
        self.assertEqual(output.stat().st_mode & 0o777, 0o700)
        self.assertTrue((output / "scorecard.md").is_file())
        for case, mapping in key["cases"].items():
            self.assertEqual(set(mapping), {"A", "B"})
            self.assertEqual(set(mapping.values()), {"baseline", "profile"})
            for label, variant in mapping.items():
                prompt = (output / case / f"{label}.prompt").read_text()
                self.assertEqual("# Code like me" in prompt, variant == "profile")
                self.assertEqual((output / case / f"{label}.md").read_text(), "Synthetic stub response\n")
                self.assertEqual((output / case / f"{label}.env").read_text(), "not-present")
                self.assertIn("--disable\nshell_tool", (output / case / f"{label}.args").read_text())

    def test_failed_session_stops_without_scorecard_or_fake_results(self) -> None:
        output = self.directory / "failure"
        result = self.invoke(output, STYLE_EVAL_FAKE_FAILURE="exit")
        self.assertEqual(result.returncode, 2)
        self.assertTrue((output / "failure.txt").is_file())
        self.assertFalse((output / "scorecard.md").exists())
        self.assertFalse(list(output.rglob("[AB].md")))

    def test_rejects_missing_or_empty_answers_and_authentication_failure(self) -> None:
        for mode in ("missing", "empty", "401"):
            with self.subTest(mode=mode):
                output = self.directory / mode
                result = self.invoke(output, STYLE_EVAL_FAKE_FAILURE=mode)
                self.assertEqual(result.returncode, 2)
                self.assertFalse((output / "scorecard.md").exists())
                if mode == "401":
                    self.assertIn("HTTP 401", (output / "failure.txt").read_text())

    def test_timeout_is_reported_without_scorecard(self) -> None:
        output = self.directory / "timeout"
        result = self.invoke(output, STYLE_EVAL_FAKE_FAILURE="timeout")
        self.assertEqual(result.returncode, 2)
        self.assertIn("TimeoutExpired", (output / "failure.txt").read_text())
        self.assertFalse((output / "scorecard.md").exists())

    def test_model_override_is_passed_to_both_sessions(self) -> None:
        output = self.directory / "model"
        result = self.invoke(output, "--model", "synthetic-model")
        self.assertEqual(result.returncode, 0, result.stderr)
        args = list(output.rglob("*.args"))
        self.assertEqual(len(args), 8)
        for argfile in args:
            self.assertIn("-m\nsynthetic-model", argfile.read_text())

    def test_refuses_existing_output_directory(self) -> None:
        output = self.directory / "exists"
        output.mkdir()
        marker = output / "marker"
        marker.write_text("preserve")
        result = self.invoke(output)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(marker.read_text(), "preserve")

    def test_invalid_timeout_does_not_create_output(self) -> None:
        output = self.directory / "invalid-timeout"
        result = subprocess.run(
            [sys.executable, str(RUNNER), "--output-dir", str(output), "--timeout", "0"],
            env=self.env, text=True, capture_output=True, timeout=5,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(output.exists())

    def test_missing_cli_is_reported_without_results(self) -> None:
        output = self.directory / "missing-cli"
        empty_bin = self.directory / "empty-bin"
        empty_bin.mkdir()
        result = subprocess.run(
            [sys.executable, str(RUNNER), "--output-dir", str(output)],
            env=dict(self.env, PATH=str(empty_bin)), text=True, capture_output=True, timeout=5,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("FileNotFoundError", (output / "failure.txt").read_text())
        self.assertFalse((output / "scorecard.md").exists())

    def test_refuses_repository_root_as_output(self) -> None:
        result = self.invoke(ROOT)
        self.assertNotEqual(result.returncode, 0)

    def test_refuses_output_inside_public_repository(self) -> None:
        output = ROOT / "forbidden-style-evaluation-output"
        self.assertFalse(output.exists())
        result = self.invoke(output)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()

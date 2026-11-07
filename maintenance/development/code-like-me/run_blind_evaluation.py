#!/usr/bin/env python3
"""Run synthetic paired Codex sessions; keep the answer key private until review."""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SKILL = ROOT / "skills/development/code-like-me"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path, help="new directory outside the repository")
    parser.add_argument("--model", help="optional model override; otherwise use the CLI default")
    parser.add_argument("--timeout", type=int, default=180, help="seconds per independent session")
    args = parser.parse_args()
    output = args.output_dir.expanduser().resolve()
    if output == ROOT or ROOT in output.parents:
        parser.error("output must be outside the public repository")
    if args.timeout < 1:
        parser.error("timeout must be positive")
    os.umask(0o077)
    try:
        output.mkdir(mode=0o700, parents=False, exist_ok=False)
    except OSError as exc:
        parser.error(f"cannot create new output directory: {exc}")
    os.chmod(output, 0o700)
    cases = json.loads((HERE / "scenarios.json").read_text(encoding="utf-8"))
    profile = "\n\n".join((SKILL / name).read_text(encoding="utf-8") for name in ("SKILL.md", "references/profile.md", "references/examples.md"))
    common = ("This is a synthetic coding exercise. Use only the scenario in this prompt. "
              "Do not read files, call tools, access the network, or mention the evaluation or profile. "
              "Return code, tests and a concise explanation.\n\n")
    variants = {"baseline": "Do not apply installed skills or personal coding profiles.\n\n",
                "profile": "Apply the following personal coding profile when compatible with the scenario:\n\n" + profile + "\n\n"}
    secret = random.SystemRandom()
    # The subprocess needs model authentication but not GitHub or unrelated service credentials.
    allowed_model_auth = {"OPENAI_API_KEY", "CODEX_ACCESS_TOKEN"}
    child_env = {
        name: value for name, value in os.environ.items()
        if name in allowed_model_auth
        or not re.search(r"TOKEN|PASSWORD|SECRET|API_KEY|CREDENTIAL|^GH_|^GITHUB_", name, re.I)
    }
    key = {"method": "independent ephemeral CLI sessions; synthetic inputs only", "model": args.model or "CLI default", "cases": {}}
    with tempfile.TemporaryDirectory(prefix="code-like-me-eval-") as workspace:
        for case in cases:
            labels = ["A", "B"]
            secret.shuffle(labels)
            pairs = list(zip(labels, ("baseline", "profile")))
            secret.shuffle(pairs)
            case_dir = output / case["id"]
            case_dir.mkdir(mode=0o700)
            key["cases"][case["id"]] = {label: variant for label, variant in pairs}
            for label, variant in pairs:
                destination = case_dir / f"{label}.md"
                cmd = ["codex", "exec", "--skip-git-repo-check", "--ephemeral", "--ignore-user-config", "-s", "read-only", "-C", workspace, "-o", str(destination)]
                for feature in ("shell_tool", "apps", "browser_use", "standalone_web_search", "skill_search", "computer_use", "code_mode_host"):
                    cmd += ["--disable", feature]
                if args.model:
                    cmd += ["-m", args.model]
                cmd += ["-"]
                prompt = common + variants[variant] + case["prompt"]
                print(f"Running {case['id']}, response {label}...", flush=True)
                try:
                    result = subprocess.run(cmd, input=prompt, text=True, capture_output=True, timeout=args.timeout, check=False, env=child_env)
                except (OSError, subprocess.TimeoutExpired) as exc:
                    (output / "failure.txt").write_text(f"Session could not complete: {type(exc).__name__}\n", encoding="utf-8")
                    (output / "key.json").write_text(json.dumps(key, indent=2), encoding="utf-8")
                    print("Evaluation blocked; no result was inferred. See private output directory.", file=sys.stderr)
                    return 2
                if result.returncode or not destination.exists() or not destination.read_text(encoding="utf-8").strip():
                    reason = "authentication rejected (HTTP 401)" if "401" in result.stderr else f"session exited {result.returncode}"
                    (output / "failure.txt").write_text(f"{reason}; no answer accepted.\n", encoding="utf-8")
                    (output / "key.json").write_text(json.dumps(key, indent=2), encoding="utf-8")
                    print("Evaluation blocked; no result was inferred. See private output directory.", file=sys.stderr)
                    return 2
    (output / "key.json").write_text(json.dumps(key, indent=2), encoding="utf-8")
    scorecard = ("# Blind scoring\n\nCompare A and B before opening key.json. Evaluate correctness, project rules, resemblance to the owner's preferences, changed-branch coverage, and reasoning. Record ties and uncertainty.\n\n"
                 "| Scenario | Better response (A/B/tie) | Correctness and project rules | Style and branch coverage | Comments |\n"
                 "|---|---|---|---|---|\n")
    scorecard += "".join(f"| {case['id']} | | | | |\n" for case in cases)
    (output / "scorecard.md").write_text(scorecard, encoding="utf-8")
    print(f"Blind answers and scorecard written to {output}; keep key.json closed until scoring.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

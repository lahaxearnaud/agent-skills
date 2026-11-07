# Paired blind evaluation

The four tasks in [scenarios.json](scenarios.json) are synthetic; no private repository code is included. Each is sent twice to independent ephemeral `codex exec` sessions with the same task: one is instructed not to use installed skills, the other receives the skill, profile and example texts. The harness ignores user configuration, uses a fresh empty temporary workspace and a read-only sandbox; disables shell, app, browser, web-search, skill-search, computer and code-mode features; strips GitHub and unrelated secret environment variables; and instructs both sessions not to read files, use tools, or access the network. Model-authentication variables may be retained for the CLI. It randomizes execution order and whether `A` or `B` receives the profile.

After authenticating the Codex CLI, run from a safe checkout:

```sh
python maintenance/development/code-like-me/run_blind_evaluation.py --output-dir /path/outside/the/repository/new-evaluation
```

The output directory must not already exist; its parent must exist. Read each pair and fill `scorecard.md` before opening `key.json`. Judge correctness and project constraints first, then resemblance to the owner's confirmed preferences, changed-branch coverage and clarity. The owner may privately compare with the locally retained qualitative research; do not send private commits or source code to the agent sessions. Branch coverage is judged from proposed tests, not measured unless they are actually executed. Record ties and uncertainty, compare the same cases and only then reveal the key. Results stay local and are not published automatically. Use multiple repetitions and reviewers for a stronger conclusion; one pair per scenario is an exploratory sample, not a statistical estimate.

The runner requires a CLI version supporting these feature switches. A CLI may still inject system-level instructions, expose other tools, or discover context outside user configuration; the prompt explicitly disables skills for the baseline, but perfect isolation is not guaranteed. Model versions, sampling randomness and human scoring create additional uncertainty. If a session fails or produces no answer, the runner stops, records failure privately and does not fabricate a result or score. The initial attempt to connect Codex on 2026-11-07 returned HTTP 401, so no paired answers were produced in that attempt.

# Evaluation of SQL injection static review

Date: 2026-11-03. These are small qualitative scenario checks, not a benchmark, application audit or evidence of improved detection rates.

## Independent scenario comparison

An agent without the new skill and another with it received the same five short descriptions and were asked for static-only analysis, limits and fixes. No repository, runtime or application was provided. Both independently made the following distinctions:

| Scenario | Both agents' result |
|---|---|
| Fixed Doctrine SQL with bound name | No injection established for that value; check API and other fragments. |
| HTTP sort key to Doctrine `orderBy` | Candidate; verify validation, control and execution; map to fixed fields. |
| Stored display name concatenated in job SQL | Possible second-order flow; establish write/read connection and execution; bind at later sink. |
| Bound LIKE pattern | Not SQL grammar injection for that value; wildcard semantics may be a separate logic problem. |
| Fixed `%d` with effective integer validation | No SQL grammar injection at that position; validate paths and semantics; prefer binding. |

The baseline already handled all five well, and the skill-guided agent identified no blocking technical defect. This comparison does not establish that the skill improves results or generalizes to real projects. It does not quantify false positives, recall or inter-agent variability. No code paths or line numbers were available, and neither agent claimed runtime exploitation. The skill itself asks for evidence paths when actual code is available.

## Other checks

- The incomplete-flow and hostile-comment examples were reviewed as documentary scenarios; they were not independently exercised in an agent run.
- `npx --yes skills@1.7.6 add . --list` discovered all three repository skills.
- Installed the SQL skill from the local checkout in a temporary directory for Codex and OpenCode using `--copy --yes`; compared the installed directory with the source using `diff -qr`, with no differences.
- Checked relative Markdown links and `git diff --check`. No target application, scanner, probe or SQL payload was run.

## Corpus expansion note

The later corpus expansion added 54 sourced advisory summaries, 20 triage leads and 10 synthetic scenarios; the original five-scenario comparison above predates those additions. The operational skill workflow was not changed, but its source/sink reference now calls out the newly documented key-name, workflow, pagination-token, generated-code and driver-parser patterns. This update did not rerun the five-agent scenarios or establish any accuracy change.

# Initial paired scenario review

These are hand-authored paired responses to the same synthetic prompts, reviewed against the profile; they are not independent agent runs or an empirical quality benchmark.

| Prompt | Without profile: plausible response | With profile: expected response |
|---|---|---|
| Add a small PHP calculation to a typed modern project. | Add a function without considering local type conventions. | Inspect neighbors and use explicit compatible types; avoid imposing `final` or `strict_types` globally. |
| Add a JavaScript constant to an ES module. | Use a mutable binding by default. | Prefer `const` if not reassigned; preserve the module system. |
| Add error handling to a Rust project. | Infer a personal preference from the task alone. | Follow existing project error handling; acknowledge insufficient personal Rust evidence. |
| A project requires an older PHP syntax. | Use newer syntax because a general profile suggests it. | Follow project version and conventions; do not force the personal profile. |
| A validation fix needs a test. | Change the code without examining tests. | Inspect adjacent tests and add a focused test where justified by scope and repository instructions. |

This conceptual comparison checks intended precedence and boundaries only. No fresh independent agent responses or statistical measurements were run, so no improvement in output quality or automatic activation is claimed. Run paired blinded agent evaluations before asserting either.

## Follow-up qualitative review and paired evaluation

A follow-up examined structurally redacted changes in 35 selected commits across 14 projects and three periods; one unusually large patch was not interpreted, and eight additional PHP examples were selected for class/constructor and test changes. This is a purposive sample, not an independent benchmark. Contradictions included `final` being both added and removed, as well as direct controller logic and extracted service logic. The owner subsequently confirmed a pragmatic Symfony split, conditional preference for `final`/`readonly`, and tests for each new or changed reachable branch. Those direct preferences are distinguished from inferred observations.

An independent A/B protocol and runner are documented in [blind-evaluation.md](blind-evaluation.md). The initial CLI connectivity check and a real harness attempt both returned HTTP 401; no independent A/B responses have yet been obtained or scored. The ten local runner tests passed with a fake CLI, checking pairing, project-boundary protection, model selection and failure handling; those are harness tests, not model evaluations. Do not treat the hand-authored table above as the paired experiment.

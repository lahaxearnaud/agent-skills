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

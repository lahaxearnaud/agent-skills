# Evaluation record

## Scope and status

The fixed suite is in [evaluation-scenarios.md](evaluation-scenarios.md). This is a source-only qualitative retrieval/triage evaluation, not a scanner benchmark: the snippets are inert, no application or payload is executed, and no precision/recall claim is made.

**Status on 2026-11-03: independent baseline/with-skill comparison not run.** No separate fresh-context evaluation outputs were captured during this implementation, so no baseline or with-skill result is fabricated. The scenarios and expected classifications are recorded for a future independent run. A final repository reviewer is a quality review, not a substitute for this evaluation.

## Expected classification matrix

| Scenario | Expected result | Required distinction |
| --- | --- | --- |
| P1 | Positive candidate / static flow if route context confirms | Shell string versus argv; request route and process identity |
| P2 | Negative for shell injection, further child semantics check | Argument vector does not equal universal safety |
| P3 | Incomplete candidate | No shell shown; argument/option interpretation unresolved |
| D1 | Positive candidate / static flow | Remote source reaches general evaluator; no runtime claim |
| D2 | Negative | Fixed expression and no remote source in excerpt |
| T1 | Positive candidate / static flow | User-authored source stored, rendered later; permissions/sandbox unknown |
| T2 | Negative for SSTI from excerpt | Trusted source/value separation; missing app context stated |
| S1 | Incomplete high-priority candidate | Remote bytes reach native deserializer; gadget/filter/classpath unproven |
| S2 | Negative for native-object RCE from excerpt | Data-only JSON; downstream custom hooks absent |
| L1 | Negative/incomplete | Upload/storage is not later execution |
| L2 | Incomplete | Worker sink without producer/reachability link |
| L3 | Positive chain if repository edges and conditions are confirmed | Remote model selection → queue → dynamic import; execution context unknown |
| X1 | Mixed/negative for SSTI; incomplete process semantics | Trusted template data and argv do not establish RCE; inspect child behavior |

## Future run protocol

Use two separate fresh contexts with identical scenario prompts. Baseline receives only the scenario suite and the repository-under-review boundary. With-skill receives only `skills/security/rce-static-review/` plus the same scenarios. Do not provide corpus files to either evaluator. Preserve exact answers, model/tool/version, date, prompt, scenario-by-scenario classification and citations. Score the distinctions in the table, unsupported impact claims, false positives and missing preconditions. Report disagreements; do not infer statistical significance from this small qualitative suite.

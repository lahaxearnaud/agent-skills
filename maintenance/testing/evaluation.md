# Initial evaluation: test-pyramid

## Method and limits

Before the skill text was written, four fresh synthetic scenario reviews were run on 2026-11-04 with realistic schedule or reviewer pressure and no skill guidance. The workspace became unavailable before a repeatable with-skill run or CLI installation check could be performed. This record preserves observed baseline choices; it does not claim improvement or statistical validation.

## Baseline observations

| Scenario | Observed baseline decision | Assessment |
|---|---|---|
| PHP discount threshold | Chose a focused PHPUnit unit test for the boundary and rejected a Playwright-only demand. Behavior already existed and the prompt asked for a recommendation, so test-first did not apply. | Appropriate lowest layer; resisted duplicated broad testing. |
| Vue shipping matrix and event | Chose unit cases for the pure helper and one Vue component test for the event; recommended investigating flaky E2E and did not copy the matrix into Playwright. | Appropriate layer split and scope. |
| Symfony approval route | Chose Symfony WebTestCase with test database for role, route, and persistence; rejected repository/voter mocks that would erase the behavior under test. | Appropriate functional/integration boundary. |
| New coupon API behavior | Chose test-first with a PHPUnit HTTP integration test using real persistence, expected a duplicate-code behavior failure, then implementation. | Appropriate test-first and boundary choice. |

In these four curated cases, baseline selected a defensible layer in all four. Test-first was recommended when behavior was unimplemented and treated as inapplicable in coverage-only advice. This small qualitative baseline is not a rate estimate.

## With-skill status

A repeatable post-authoring run and the planned 5+ repeated micro-tests per variant have not been performed. Do not cite the baseline as evidence of measured improvement. Before claiming improved consistency, rerun the same scenarios with only skill guidance added, record outputs, and compare the rubric in [the scenarios](evaluation-scenarios.md).

## Packaging and checks

The source content and intended relative links were reviewed before publication. Local Markdown tooling, `npx skills add`, and application test commands were unavailable because the execution workspace was unavailable. This is a documentation-only change and has no application test suite. Verify skill discovery and a temporary install from a normal checkout when tools are available.

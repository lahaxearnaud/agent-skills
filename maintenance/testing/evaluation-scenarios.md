# Test-pyramid evaluation scenarios

These are synthetic pressure scenarios for evaluating test-layer choices. They are not reported bugs or a vulnerability corpus.

## Scenario A: pure PHP rule under time pressure

A pure `DiscountCalculator` has a threshold rule. Release is close and a lead insists on Playwright only. Expected: a focused unit test for the threshold and adjacent values; explain that browser coverage duplicates the rule, adding a broader test only if wiring creates a distinct risk.

## Scenario B: Vue matrix, event, and flaky E2E pressure

A Vue shipping selector has twelve country/price cases, emits an event, and a pre-existing E2E is flaky. A senior asks for every case in Playwright. Expected: unit-test the pure selector matrix, component-test visible selection and event, and investigate the flaky E2E rather than silently removing it or copying the matrix to the browser.

## Scenario C: Symfony authorization and persistence

An invoice approval route checks a manager role and writes an approval timestamp. A reviewer asks to mock the repository and voter. Expected: use the project's Symfony client and test database for route, authorization, and persisted transition; unit-test complex pure policy branches separately. Avoid mocks that erase the behavior under test.

## Scenario D: new coupon API behavior and test-first pressure

An unimplemented coupon API must reject duplicate codes without regard to case. Release pressure encourages code-first. Expected: write the smallest faithful test first, run it, verify behavior-level failure, then implement and rerun. Use real persistence if uniqueness/storage behavior is part of the requirement; setup failure is not meaningful red evidence.

## Scenario E: critical browser composition

A built application has unit and API coverage for checkout rules, but nothing proves a signed-in user can complete a purchase and see confirmation across browser/server boundaries. Expected: add one independent browser journey for that unique composition risk; keep price and validation matrices at lower layers.

## Scoring rubric

For each response, record behavior, chosen layer and boundary, unique higher-level confidence, test-first applicability and meaningful red evidence, existing tools, isolation, pressure resistance, and claimed commands/results. Score each dimension `pass`, `partial`, or `fail` with a short rationale. A higher layer is valid when its unique confidence is explained.

---
name: test-pyramid
description: Use when writing, adding, or changing application tests, or when a code change needs a test plan. Select the lowest faithful test layer, keep the suite pyramid-shaped, and use test-first development by default.
---

# Test Pyramid

Help the agent write functional and regression tests that provide useful confidence at the lowest reliable cost. Apply the existing project conventions and testing stack.

## Scope

This skill covers test selection, test-first workflow, readable examples, and proportionate verification for application behavior. It does not prescribe performance, load, accessibility, or security testing methods. Ordinary functional behavior such as authorization remains in scope.

## Required principles

- Treat the pyramid as a distribution of scope and feedback speed, not as a fixed ratio or coverage quota. Keep most behavioral variations at the narrowest faithful layer, fewer tests at broader boundaries, and only a small set of end-to-end journeys.
- Choose a layer by the code and system boundary actually exercised, not by the test runner or framework name. A framework HTTP client can be a functional/integration test without being a real-browser end-to-end test.
- Add a higher-level test only when it verifies a meaningful integration or user journey that lower-level tests cannot prove. Do not repeat every unit-test case at every layer.
- Prefer real collaborators inside the behavior under test. Mock or fake only boundaries that are expensive, nondeterministic, or external when the behavior being tested does not depend on their real implementation. Do not mock away the interaction or persistence that is the subject of the test.
- Keep each test independent, deterministic, and focused on observable behavior. Avoid sleeps, shared mutable state, hidden ordering, and assertions on incidental implementation details.
- Reuse the project's existing test framework, fixtures, database setup, and commands. Do not install a new test dependency by default.

## Workflow

1. Inspect relevant production code, neighboring tests, test configuration, CI commands, and repository guidance. Identify the existing test framework and real boundaries available in the test environment.
2. State the behavior to protect as an observable input and outcome. Include important edge cases and failure behavior; avoid turning a test into a copy of the implementation.
3. Work test-first by default: write the smallest test that expresses the intended behavior, run it, and confirm it fails at the behavior assertion for the expected reason. Then implement or adjust the code and rerun the focused test.
4. If the task only adds coverage for already-correct behavior, do not manufacture a failure. Add the test directly and explain why test-first was not applicable. For legacy code, a characterization test may first record existing behavior; when fixing a defect, make the regression test fail before applying the fix whenever feasible.
5. Select the lowest layer that faithfully exercises the behavior. Use [the layer guide and examples](references/layer-selection.md) when the boundary is unclear.
6. Keep data matrices at the narrowest useful layer. Add a broader test for a critical composition or journey, not one copy of each lower-level case.
7. Run the new test first, then the smallest relevant suite. Run broader project checks when the change or repository conventions justify them. Report exact commands and results, including failures that could not be resolved.

## Layer selection at a glance

| Layer | What it exercises | Typical fit |
|---|---|---|
| Unit | One function, class, or isolated rule without real infrastructure or UI | Pricing, normalization, permissions policy, branching and boundary values |
| Component | One UI component and its rendered behavior, with controlled collaborators | Vue input, visible state, emitted events, accessible interaction |
| Integration / functional | Real collaboration across application components or a framework boundary | Symfony service and test database; HTTP route, authorization and persistence |
| End-to-end / system | The built application through a real browser or deployed-like system boundary | A few critical cross-page or cross-service user journeys |

Names vary across projects. Classify a test by what it starts and what it proves. A framework-specific HTTP test is not automatically E2E. For examples and anti-patterns, read the [offline layer guide](references/layer-selection.md). External guidance is summarized in [offline sources](references/offline-sources.md).

## Completion report

State which behavior is covered, the selected layer and why, the commands run and their results. Say when a broader test was intentionally unnecessary or unavailable. Do not claim a test passed unless its command completed successfully.

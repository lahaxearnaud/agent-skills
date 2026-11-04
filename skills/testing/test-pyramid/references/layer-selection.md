# Choosing the lowest faithful test layer

Use the narrowest test boundary that can establish the behavior in question. A higher layer is justified when it checks a collaboration or system property that narrower tests cannot prove.

## Practical definitions

| Layer | Boundary and confidence | Examples |
|---|---|---|
| Unit | A small unit of code runs without real UI, database, network, or framework boot. It gives fast feedback on a rule. | Pure JavaScript function, PHP value object, calculator, parser, policy decision. |
| Component | A UI component is rendered and interacted with while unrelated services remain controlled. It checks visible state and component contracts. | Vue Test Utils mount, click/select input, assert rendered output or emitted event. |
| Integration / functional | Real application collaborators cross a framework, storage, or HTTP boundary in a controlled test environment. Exact labels vary. | Symfony kernel/service test; WebTestCase request with test database and real persistence path. |
| End-to-end / system | A built application is driven through its real browser or system boundary, often including multiple pages or services. | Playwright flow across login and a critical purchase journey. |

The tool name does not determine the layer. A Symfony WebTestCase uses an HTTP-shaped interface but typically exercises an in-process application client and test kernel, so describe it as a functional or integration test unless the project defines another term. A Vue mount may be a focused component test or a broader integration test depending on which real collaborators it includes. A real browser against the built application is a different boundary.

## Examples

### PHP: a discount boundary belongs at unit level

Suppose a pure `DiscountCalculator` applies a discount at a minimum order amount. Keep threshold and neighboring values in a focused unit test:

```php
self::assertSame(0, $calculator->discountFor(49.99));
self::assertSame(5, $calculator->discountFor(50.00));
self::assertSame(5, $calculator->discountFor(50.01));
```

A browser test for each amount would repeat the rule while adding setup and failure noise. Add a separate integration test only if the calculation's wiring or persisted order total has a distinct risk.

### JavaScript and Vue: split pure rules from component behavior

For a pure shipping-option selector, exercise a country/price matrix in the existing unit runner (for example, Vitest in a Vue/Vite project). Test empty choices, boundary prices, and a few representative countries. Do not duplicate the whole matrix in a browser.

For a Vue component that lets the user choose an option, mount it with the component test tools already used by the project. Select an option and assert the visible selection and emitted event. Keep the test about user-observable behavior rather than private component fields.

```js
expect(selectShipping({ country: "FR", total: 50 })).toEqual("express");
```

```js
const wrapper = mount(ShippingOptions, { props: { options } });
await wrapper.get('[data-test="express"]').trigger("click");
expect(wrapper.emitted("shipping-selected")).toHaveLength(1);
```

If the project relies on accessible user-facing selectors, prefer those over test-only selectors. Follow its established convention.

### Symfony: authorization plus persistence is functional/integration coverage

For an invoice approval endpoint, use the existing Symfony test client and isolated test database to exercise the route, authenticated role, state transition, and persisted timestamp together. Keep the repository and voter real when their behavior is part of the requirement. Assert the observable response and stored state. Do not replace the persistence path with mocks and then claim persistence was tested.

```php
$client->loginUser($manager);
$client->request("POST", "/invoices/42/approve");

self::assertResponseRedirects();
self::assertSame("approved", $invoiceRepository->find(42)->status());
```

Use smaller unit tests for a pure policy or state-transition rule if those rules have several branches. The functional test then checks that the route, authentication, and persistence are wired together.

### Browser E2E: reserve for unique critical confidence

A Playwright test may verify one critical journey such as signing in, completing checkout, and seeing the resulting confirmation in the built app. Keep it independent and assert through user-facing controls. The unit suite should carry price and validation variations; the functional suite should cover important server boundaries. Add browser tests for cross-layer failures they uniquely prevent, not to recreate the lower-level suite.

## Test-first and failure diagnosis

For a new or fixed behavior, first run the focused test and verify that it fails because the asserted behavior is missing. A syntax error, unbootable database, bad fixture, timeout, or missing dependency is a test setup failure, not useful red evidence. Fix the harness before interpreting the result.

When the production behavior already exists and the task is coverage-only, a test may pass on its first run. Record that test-first was not applicable instead of adding artificial changes just to obtain a red result.

## Common anti-patterns

- Putting every data combination in end-to-end tests.
- Adding a browser test for every pure business rule.
- Calling a framework HTTP client “E2E” without a real browser or system boundary.
- Mocking the database, repository, or policy whose real behavior the test claims to verify.
- Treating line coverage, test count, or a fixed unit/integration/E2E percentage as the pyramid.
- Quarantining a flaky test without first checking isolation, timing, shared data, environment, and a responsible follow-up.
- Asserting internal calls or private state where a stable observable result would express the contract.

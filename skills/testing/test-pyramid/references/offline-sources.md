# Offline source notes

These attributed notes carry the operational points used by the skill so an agent can work when external documentation is unavailable. They are summaries, not copied documentation. URLs are provenance and optional lookup pointers.

## Symfony testing documentation

- Source: [Symfony testing guide, 7.4](https://symfony.com/doc/7.4/testing.html); source snapshot: [symfony/symfony-docs, 7.4/testing.rst](https://github.com/symfony/symfony-docs/blob/7.4/testing.rst).
- Consulted: 2026-11-04.
- The guide uses PHPUnit and distinguishes test types by project convention: unit tests cover an individual class or code unit; integration tests exercise combinations of classes and may use the service container without testing the whole application; application or functional tests exercise application behavior through HTTP requests. These labels are not universal, so identify the actual boundary.
- `KernelTestCase` boots the kernel for tests involving services. `WebTestCase` provides an application test client to make requests and inspect responses. Tests should be isolated, use a test database, and avoid state leaking between cases. Use the project's existing reset and fixture mechanisms.

## Vue testing guide

- Source: [Vue guide: Testing](https://vuejs.org/guide/scaling-up/testing.html); source snapshot: [vuejs/docs, testing.md](https://github.com/vuejs/docs/blob/main/src/guide/scaling-up/testing.md).
- Consulted: 2026-11-04.
- Vue's guide describes a layered approach: unit tests for isolated logic, component tests for rendering and interaction, and end-to-end tests for complete application flows. Component testing provides confidence in rendered behavior and user interaction; E2E covers integrated application behavior in a browser.
- The guide notes that unit tests alone do not prove component rendering or application wiring. Add the smallest higher-level check that covers an integration boundary not already covered below it; do not infer that every lower-level case should be duplicated at browser level.

## Vue Test Utils

- Source: [Vue Test Utils guide](https://test-utils.vuejs.org/guide/); source snapshot: [vuejs/test-utils documentation](https://github.com/vuejs/test-utils/tree/main/docs).
- Consulted: 2026-11-04.
- Vue Test Utils mounts components so tests can inspect rendered output, provide props, interact with DOM elements, and check emitted events. Use it for component contracts and visible behavior; keep pure domain logic at unit level. Follow selectors and conventions already established in the repository.

## Vitest

- Source: [Vitest guide](https://vitest.dev/guide/); source snapshot: [vitest-dev/vitest documentation](https://github.com/vitest-dev/vitest/tree/main/docs).
- Consulted: 2026-11-04.
- Vitest is designed to work with Vite and can reuse the Vite configuration. It supports familiar test and assertion APIs and is commonly used for Vue/Vite projects. This is an example tool, not a reason to replace the project's runner or introduce a dependency.

## Playwright

- Source: [Playwright best practices](https://playwright.dev/docs/best-practices); source snapshot: [microsoft/playwright documentation](https://github.com/microsoft/playwright/tree/main/docs/src/best-practices-js.md).
- Consulted: 2026-11-04.
- Playwright recommends isolated tests that can run independently, stable user-facing locators, and web-first assertions that wait for observable conditions rather than fixed sleeps. Apply those ideas to the few browser journeys selected for unique end-to-end confidence.

## Limits

Framework terminology and APIs change. These summaries preserve stable selection guidance, not an exhaustive reproduction of each manual. If network access is available and a version-specific behavior materially affects the work, consult the matching official docs. Otherwise follow the codebase's installed versions and state unresolved uncertainty.

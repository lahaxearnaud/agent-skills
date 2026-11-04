# Update prompt: test-pyramid

Use this prompt when reviewing the skill after changes in test practice, agent formats, or repository conventions.

> Review `skills/testing/test-pyramid/` for accuracy and usability. Keep it focused on writing functional and regression tests with the test pyramid: select the lowest faithful boundary, keep broad tests few and purposeful, use test-first by default, and respect existing project tooling.
>
> Read the skill, its offline source notes, `AGENTS.md`, README, and ADR index first. Preserve scope: this skill does not define performance, accessibility, load, or security test methodology. Do not add a numeric test ratio or coverage quota.
>
> If external documentation is available, consult only relevant current official sources and record what was verified. Keep attributed local summaries detailed enough for offline use. Do not copy large third-party passages. If a source is unavailable, say so and retain uncertainty rather than inventing details.
>
> Keep examples representative of PHP/Symfony, vanilla JavaScript, Vue, and browser E2E where useful. Classify by actual execution boundary, not tool name. Use the project's existing test stack; do not recommend new dependencies by default.
>
> Preserve the synthetic evaluation scenarios and baseline results. Add scenarios for new failure modes, distinguish observations from assumptions, and do not claim improvement without a with-skill comparison. Update the skill README, root catalog, maintenance evaluation, and ADR index if the decision or package structure changes. Check links and verify skill discovery/installability when tooling is available.

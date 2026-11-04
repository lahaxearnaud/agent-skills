# Test-pyramid skill design

## Goal

Publish an installable English-language skill that guides coding agents writing application tests to respect the test pyramid and use test-first development proportionately.

## User and trigger

The audience is code agents working in application repositories. Trigger when writing, adding, or changing tests or when a change needs a test plan. This is not a general test-suite audit skill.

## Behavior

- Inspect project conventions and test boundaries before proposing tools.
- Prefer many fast, narrow tests, fewer integration checks, and a small number of E2E journeys, without prescribing ratios.
- Select by actual execution boundary, not framework terminology.
- Add a higher-level test only for unique integration confidence; keep matrices and branches at the lowest faithful layer.
- Test-first by default, with explicit coverage-only and characterization exceptions.
- Keep tests independent and deterministic; preserve dependencies and commands already used by the project.
- Focus on functional and regression behavior. Security, performance, accessibility, and load methods remain out of scope.

## Packaging and evaluation

Package: `skills/testing/test-pyramid/`, name: `test-pyramid`, with operational references stored locally. Examples cover PHP/Symfony, vanilla JavaScript, Vue, and browser E2E. Maintenance scenarios are synthetic and separate from source corpora. Root README and AGENTS index the skill; ADR-0015 records the repository decision.

Baseline outcomes are recorded honestly. No improvement claim is made without a with-skill comparison.

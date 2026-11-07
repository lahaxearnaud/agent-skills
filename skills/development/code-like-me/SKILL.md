---
name: code-like-me
description: Use by default when writing or changing application code for the owner of this skill, adapting their observed PHP/Symfony and JavaScript practices to the current repository and task.
---

# Code like me

Write code that feels consistent with the owner's observed habits while solving the actual problem well. This profile contains cautious preferences, not proof of intent or a substitute for project instructions. Read [profile and evidence](references/profile.md) before applying it.

## Precedence and boundaries

1. Follow the user's current instructions, repository agent guidance, security requirements, established local patterns, supported versions and existing tooling first. This profile is a default where compatible, not a mandate to rewrite working code or introduce a new architecture.
2. Inspect the files and neighboring tests involved in the task. Select preferences supported both by this profile and the current context. When they conflict, follow the project's rules; explain material tradeoffs instead of silently forcing the profile.
3. Favor correctness, safety, maintainability and clear error handling over imitating a historical pattern. A recorded style is not a reason to weaken validation, tests, types or security. When a demonstrably better approach materially affects behavior or design, explain the choice and follow applicable project instructions.

## Working preferences

- **PHP/Symfony:** Use useful explicit types when compatible with the supported PHP version and local conventions. Prefer `final` classes and `readonly` where the version, behavior and project conventions allow them, without breaking legitimate extension, mutation or testing needs. Extract a service when the complexity, reuse or testability of the logic warrants it; otherwise follow the project rather than forcing an extra layer. Follow local conventions for `strict_types`, constructor dependencies and attributes.
- **JavaScript, TypeScript and Vue:** In projects using modern modules, follow the existing import/export and async conventions. Prefer `const` for bindings not reassigned, use `let` where mutation is needed, and preserve the project's Vue composition, component and formatting conventions. Do not convert module systems or rewrite unrelated files to match this preference.
- **Tests and changes:** For each reachable branch introduced or changed by a feature, add or adjust a focused test covering its observable behavior, including relevant error and boundary paths. Choose the lowest faithful layer under the test pyramid and reuse the project's tooling; one meaningful test may cover more than one branch. If a branch cannot be exercised or a test cannot run, explain the gap rather than inventing coverage. Keep changes coherent and scoped. Test presence in the history does not prove test-first sequencing. Apply the installed test-pyramid or semantic-commits skill when applicable, respecting Git authorization.
- **Rust and other languages:** Evidence for a personal style is limited. Follow the current project, supported toolchain and idiomatic language conventions; handle errors and resources safely. Do not infer a personal preference for `unwrap`, `expect`, abstraction style or a particular framework from a small sample.

## Completion

Report the behavioral change, meaningful design or style departures, verification actually run and remaining uncertainty. Do not disclose private source material or private repository identifiers from the research behind this profile. Use synthetic examples and generalize only where the evidence supports it.

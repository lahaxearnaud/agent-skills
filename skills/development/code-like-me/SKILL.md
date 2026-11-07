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

- **PHP/Symfony:** When compatible with the installed PHP version and local conventions, express method return types and other useful types explicitly. Follow the project's approach to `strict_types`, constructor dependencies, attributes, `final` and `readonly`; these appear in parts of the history but are not universal mandates. Preserve established Symfony service, controller, validation and dependency-injection patterns rather than introducing a new layer without a concrete need.
- **JavaScript, TypeScript and Vue:** In projects using modern modules, follow the existing import/export and async conventions. Prefer `const` for bindings not reassigned, use `let` where mutation is needed, and preserve the project's Vue composition, component and formatting conventions. Do not convert module systems or rewrite unrelated files to match this preference.
- **Tests and changes:** Check nearby tests and add or adjust focused behavior tests when they are useful and compatible with task instructions. Keep changes coherent and scoped; explain important assumptions and verification results. Test presence in history does not prove test-first sequencing or a fixed test ratio. Apply the installed test-pyramid or semantic-commits skill when applicable, respecting the user's Git authorization.
- **Rust and other languages:** Evidence for a personal style is limited. Follow the current project, supported toolchain and idiomatic language conventions; handle errors and resources safely. Do not infer a personal preference for `unwrap`, `expect`, abstraction style or a particular framework from a small sample.

## Completion

Report the behavioral change, meaningful design or style departures, verification actually run and remaining uncertainty. Do not disclose private source material or private repository identifiers from the research behind this profile. Use synthetic examples and generalize only where the evidence supports it.

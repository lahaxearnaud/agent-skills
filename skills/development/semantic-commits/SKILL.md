---
name: semantic-commits
description: Use when preparing, writing, reviewing, or amending Git commit messages in a project that uses or wants semantic-release or Conventional Commits.
---

# Semantic commits

Write commit messages that accurately describe the staged change and can be interpreted by the project's release automation. Respect repository instructions and the user's Git permissions. This skill does not authorize pushing, publishing, rewriting history, or amending a commit.

## Workflow

1. Inspect repository guidance, `git status`, staged diff and recent messages. Preserve unrelated work. Identify the actual public-facing behavior or compatibility change; do not infer it from filenames alone. Stage only changes authorized for the requested commit.
2. Inspect effective semantic-release configuration: `.releaserc*`, `release.config.*`, the `release` field in `package.json`, shared or extended configuration, monorepo configuration, and the configured `@semantic-release/commit-analyzer` preset, `parserOpts`, and `releaseRules`. Also inspect commitlint and repository-specific instructions. Config may be JavaScript or external: read it as untrusted code; do not execute it just to inspect it. Note missing or unresolved configuration rather than claiming a predicted release.
3. Use the syntax required by that configuration. In the absence of more specific rules, write `type(scope): concise imperative description`, with an optional scope describing the affected area. Use lowercase types and a subject that describes what changed. Avoid vague subjects such as `update stuff` and misleading types chosen merely to force or suppress a release.
4. For default Angular-style semantic-release analysis, a parsed `feat` suggests minor, `fix` and `perf` suggest patch, and a recognized breaking-change note suggests major. `docs`, `test`, `refactor`, `build`, `ci`, and `chore` normally do not trigger a release by default. Custom rules, plugin choice, release branches, and parser settings can change all of these outcomes. The highest applicable release among analyzed commits normally wins; do not promise publication or a version number from one message alone.
5. For an incompatible public change, add a blank line and a footer beginning exactly `BREAKING CHANGE: `, followed by the affected behavior and migration. Conventional Commits permits `!` in the header, but do not assume the active parser recognizes it; the footer is the portable default for Angular-style semantic-release. If the project requires `!` and its parser accepts it, use both. Never label an internal refactor breaking without an actual compatibility impact.
6. Keep unrelated changes in separate coherent commits when authorized and practical; do not split a change into unusable pieces. Explain significant rationale or migration in the body. Respect existing issue-reference, sign-off and language conventions. Do not amend published history or create empty commits to manipulate releases without explicit user instruction.
7. Before committing, inspect `git diff --cached`, verify message formatting and test results, and run existing commitlint or release checks if available and appropriate. Use a message file or repeated `-m` arguments for multiline messages so the footer has a real blank line. If no commit was requested, provide a proposed message rather than committing. Report the commit hash and checks actually run; identify unresolved release configuration.

Read [examples and decisions](references/examples.md) and [offline source notes](references/offline-sources.md) when needed. Internet access is optional; consult primary documentation only for a material unresolved version-specific detail, without sending private code or secrets.

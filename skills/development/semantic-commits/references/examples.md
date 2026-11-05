# Examples and decisions

These are examples; the target repository's actual parser and release rules govern the result.

| Change | Message | Typical default analyzer result |
|---|---|---|
| Add a compatible public API | `feat(api): add cursor pagination` | minor |
| Fix incorrect output | `fix(parser): preserve empty fields` | patch |
| Improve performance without changing behavior | `perf(search): cache normalized keys` | patch |
| Documentation only | `docs: explain local installation` | no release by default |
| Tests only | `test(api): cover expired tokens` | no release by default |
| Internal restructuring | `refactor(auth): extract policy lookup` | no release by default |

A breaking change should state the consequence and migration:

```text
feat(api): replace page numbers with cursors

BREAKING CHANGE: The list endpoint no longer accepts page; use the cursor returned by the previous response.
```

A Conventional Commits header such as `feat(api)!: replace page numbers with cursors` is valid for that specification, but a semantic-release installation using another parser might not interpret `!`. Use the footer and verify actual parser support before relying on the marker. `BREAKING CHANGE:` is a footer, separated from the body by a blank line, not a casual mention embedded in prose.

Before predicting an outcome, inspect custom rules and their matching conditions. A custom `release: false` rule can suppress a match; a rule may map `docs`, `refactor`, scope or other parsed properties to any release type. Rules are evaluated according to the installed analyzer version; a custom rule that does not match ordinarily falls back to defaults. Branch configuration, last release/tag, eligible commits, monorepo tooling and other plugins affect publication. A valid commit message alone does not prove a release will occur.

For a squash merge the eventual squash message, rather than the individual branch messages, may be what the release analyzer sees. Check the repository's merge policy and ensure the final authorized commit message conveys the change; do not assume hosting settings.

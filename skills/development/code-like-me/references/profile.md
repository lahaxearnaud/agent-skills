# Personal coding profile and limits

This is an anonymized, local-first profile derived from the owner's accessible GitHub history over 2023-11-07 through 2026-11-07 UTC. It describes defaults to consider, not requirements. Project conventions and current instructions take precedence.

## Observations

- PHP changes repeatedly use explicit method return types across multiple repositories. `strict_types`, `final`, constructor patterns, attributes and `readonly` also appear, but in fewer projects and unevenly across the history. Prefer useful types where the target project and PHP version support them; copy the local convention for the other constructs rather than applying them everywhere.
- JavaScript-family changes repeatedly use ES module imports and `const` for bindings, with `let` used as well and `async`/`await` present across projects. Favor the local module system and use `const` when a binding is not reassigned. Do not infer that mutation, `var`, or another project style is categorically wrong.
- Changes touching test paths occur across multiple repositories. When a behavior change warrants tests, follow the project's existing test approach. A changed test file does not establish that all changes were tested or that tests preceded implementation.
- Rust evidence is sparse compared with PHP and the JavaScript family. No personal preference for Rust error handling, ownership patterns or architecture is established. Respect the repository and current Rust idioms.
- Architecture and workflow choices cannot be reliably reconstructed from syntax or commit metadata alone. Avoid claiming a general preference for a particular domain architecture, library, commit granularity, or development sequence without corroborating evidence from the current task.

## Evidence and confidence

The research indexed 2,298 distinct GitHub search results attributed to the account across 38 accessible repositories. GitHub search and account visibility are not proof of complete history: inaccessible organizations, unindexed branches, alternate identities, amended/deleted commits and unmarked co-authors may be absent. All indexed commit objects and changed paths were inspected locally. Forty-five commits identifiable as agent-produced or generated from available session provenance and markers were excluded from the code-style scan. Remaining commits cannot be assumed to be solely human-authored.

Among 2,253 remaining commits, the scan excluded merges and generated/vendor/build files and inspected 1,177 non-merge commits with matching PHP, Twig, JavaScript, TypeScript, Vue, Rust or Python paths. Other commits were considered through metadata and paths, not their complete patches. The scan is lexical, not a semantic review of every line. Return-type syntax appeared in 271 scanned PHP commits across seven repositories; JavaScript-family `const` and imports appeared in 249 and 205 commits across 13 repositories respectively; test paths appeared in 306 scanned commits across 16 repositories. Counts overlap and do not establish intent or frequency per line. Recent observations were checked separately; they support retaining these broad, conditional preferences. PHP modifiers are project-dependent; Rust's small sample supports no specific rule.

The source details and local analysis artifacts are private and are deliberately not packaged here. Examples in this skill are synthetic. No actual private source, identifiers, repository names or unique architecture has been included.

# Offline skill-reference evaluation scenarios

Evaluation protocol: give an evaluator only the installed skill package under review. Do not access the Internet, repository corpus, external model knowledge, or another skill package. For each prompt, answer only from local package text and cite its relative file and section. If the information is absent, mark it unavailable rather than guessing.

## Scenario 1 — OAuth redirect URI reference

Using `open-redirect-static-review`, explain what local reference material says about OAuth redirect URI validation, exact matching, and validation on error/denial branches. Identify the source document and the conditions that must be inspected in the reviewed code.

## Scenario 2 — Twig safety advisory

Using `xss-static-review`, summarize the source-backed condition, affected behavior, and remediation for the cited Twig `is_safe` advisory. Cite only local package material.

## Scenario 3 — CodeQL SQL injection query

Using `sql-injection-static-review`, explain the documented source/sink model and limitations of the linked JavaScript SQL injection query. State what a reviewer must verify in source.

## Scenario 4 — Filesystem API behavior

Using `path-traversal-static-review`, describe the documented guarantees and failure cases for PHP `realpath()`, PHP ZIP extraction, Node path resolution, and Symfony path containment. Distinguish lexical normalization, canonicalization, and race resistance.

## Scenario 5 — ADR format sources

Using `adr-authoring`, compare the core sections and useful optional sections attributed to Nygard, MADR, and Microsoft ADR guidance. State the repository-first rule that takes precedence.

## Scenario 6 — Research-backed skill builder

Using `research-backed-skill-builder`, explain how to preserve source provenance, label evidence, and package references for offline use. Confirm whether any external document must be opened to follow the skill.

## Acceptance criteria

- Each answer is supported by an installed local file and cites it precisely.
- No scenario requires network access or repository-only corpus files.
- Unknown version-specific behavior remains explicitly unknown when the local source note does not establish it.
- External source URLs may remain in local notes for attribution, but are not treated as instructions to fetch during review.

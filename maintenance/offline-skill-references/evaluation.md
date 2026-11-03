# Offline reference evaluation

Evaluation date: **2026-11-03**. This is a qualitative retrieval check, not a benchmark of code-review accuracy. A fresh-context evaluator used only the six skill package directories and was instructed not to use the corpus, network, or unsupported prior knowledge. The prompts are in [evaluation scenarios](evaluation-scenarios.md).

## Baseline before adding offline source notes

The baseline evaluator used the exact package roots. It cited existing local files and marked absent details unknown.

| Scenario | Baseline result | Evidence observed |
|---|---|---|
| OAuth redirect URI | **Pass** | Existing Open Redirect guidance already gave exact registered-URI matching, the native-app loopback-port exception, and review of error/denial branches. It named RFC 9700 but did not include a source synopsis. |
| Twig `is_safe` advisory | **Partial** | The package explained that a safe-context declaration is not proof and identified relevant Twig behavior, but did not locally establish the advisory's affected behavior, versions, or patch. |
| CodeQL JavaScript SQL query | **Partial** | General source/sink and static-analysis limits were present, but the specific query's source/sink model was not locally summarized. |
| Filesystem API behavior | **Partial** | The evaluator correctly marked ZIP extraction and Symfony helper details as unknown; generic path, `realpath()`, symlink, and race guidance was available. The scenario asked for the documented behavior of all four APIs, so unknowns are a coverage gap rather than a complete pass. |
| ADR format sources | **Partial** | The repository's template was sufficient to write an ADR, but the package did not explain the source-specific differences among Nygard, MADR, and Microsoft guidance. |
| Research-backed skill builder | **Pass** | Existing local references already covered provenance, evidence labels, and self-contained packaging without external dependencies. |

The baseline showed that generic workflow guidance and some security rules were already local, while source-specific details remained behind links. No claim is made about detection accuracy or performance.

## Evaluation with offline notes

The post-change evaluator used the same prompts and exact package roots, with only package-local files available. It cited package-relative sections and did not use the corpus or network.

| Scenario | Result with offline notes | Observed local support |
|---|---|---|
| OAuth redirect URI | **Pass** | The pack states RFC 9700 exact matching and the native-app loopback exception, and existing guidance covers success, error, denial and unsupported-response branches. See [offline source notes](../../skills/security/open-redirect-static-review/references/offline-sources.md#protocol-browser-and-security-guidance) and [framework guidance](../../skills/security/open-redirect-static-review/references/validation-and-frameworks.md#oauth-and-identity). |
| Twig `is_safe` advisory | **Pass** | The local case note identifies the affected extras and filters, the `<3.26.0` range, the entity-decoding/HTML-rendering path, and the 3.26.0 fix that removes `all` or narrows the declaration to `html`. See [offline source notes](../../skills/security/xss-static-review/references/offline-sources.md#published-report-summaries) and [context guidance](../../skills/security/xss-static-review/references/contextes-et-protections.md#conditional-guarantees). |
| CodeQL JavaScript SQL query | **Pass** | The pack describes taint tracking to a modeled query API, model/version limits and required source/query/execution checks. See [offline source notes](../../skills/security/sql-injection-static-review/references/offline-sources.md#query-builder-and-prevention-guidance) and [source/sink guidance](../../skills/security/sql-injection-static-review/references/sources-and-sinks.md#candidate-sinks-and-sql-construction). |
| Filesystem API behavior | **Pass, ZIP version behavior unknown** | Local notes distinguish `realpath()` resolution/failure, archive extraction limits, Node's lexical path APIs, Symfony's lexical containment helpers, and check/use races. See [API notes](../../skills/security/path-traversal-static-review/references/offline-sources.md#api-behavior-notes), [confinement guidance](../../skills/security/path-traversal-static-review/references/path-confinement.md#common-incomplete-controls) and [archive/symlink guidance](../../skills/security/path-traversal-static-review/references/archive-and-symlink.md#symlinks-and-time-of-checktime-of-use). |
| ADR format sources | **Pass** | The pack summarizes Nygard, MADR and Microsoft guidance separately and points back to the repository-first template rule. See [offline source notes](../../skills/documentation/adr-authoring/references/offline-sources.md#use-in-this-repository), [fallback template](../../skills/documentation/adr-authoring/references/default-template.md#reference-basis) and [skill workflow](../../skills/documentation/adr-authoring/SKILL.md#workflow). |
| Research-backed skill builder | **Pass** | The updated local method directly requires attributed offline summaries and makes external URLs provenance/update pointers rather than use-time dependencies. See [provenance guidance](../../skills/meta/research-backed-skill-builder/references/recherche-et-provenance.md#select-and-qualify-sources), [generation and evaluation](../../skills/meta/research-backed-skill-builder/references/generation-et-evaluation.md#from-research-to-method) and the [skill method](../../skills/meta/research-backed-skill-builder/SKILL.md#method). |

The evaluator concluded that all six prompts could be answered from package-local text, while keeping unsupported versions and details unknown. For Twig, the local advisory note records the published affected range and fix; for ZIP extraction, exact runtime/version behavior remains unknown. This is a small qualitative retrieval check. It demonstrates that the selected reference material is present locally; it does not measure security detection performance, prove completeness of every reference, or replace periodic source maintenance. No application, browser, scanner, or network request was part of this evaluation.

## Limits

Six retrieval prompts cover representative documentation gaps only. They do not establish completeness of all technical knowledge, version applicability, or security findings. The external URLs remain useful to maintainers on a connected machine but are not an audit-time dependency.

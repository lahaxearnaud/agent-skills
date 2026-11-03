# Open redirect research corpus

Research snapshot: **2026-11-03**. This corpus is being assembled for a future **static code-review skill** covering server-side redirects and client-side navigation, with emphasis on PHP/Symfony/Twig, JavaScript, Vue/Nuxt, and adjacent web frameworks.

The inventory contains **60 distinct public advisory/CVE records**, **one unreviewed GitHub issue lead**, **two lower-detail CVE/third-party leads**, and **two adjacent navigation cases** (one XSS chain and one meta-refresh case). The leads file also notes a script-scheme subfinding from a counted Nuxt advisory; it is not a separate open-redirect record. These counts are records, not a claim of 60 unrelated root causes: related advisories and fix bypasses are explicitly cross-referenced. Leads and adjacent cases do not count toward the 60. No application, browser, scanner, proof of concept, or live target was run; the descriptions below are source-based summaries, not independent reproductions.

## Contents

- [Published cases](published-cases.md) — 60 distinct public records with stack, preconditions, code-level flow, impact and direct source.
- [Related cases and leads](related-cases-and-leads.md) — one Vue Router issue lead, two lower-detail CVE/third-party leads, and two navigation/XSS cases that should not be misreported as confirmed open redirects.
- [Patterns and controls](patterns-and-controls.md) — static-review taxonomy, source/sink patterns, remediation themes, CSP limits, and research sources.

## Evidence and counting rules

- A maintainer security advisory or official coordinated-disclosure bulletin is treated as a **primary published case**. GitHub's `Reviewed` label describes the GitHub Advisory Database status; it is not a claim that this repository independently verified the issue.
- CVE/NVD-only records are included only where the published record contains a concrete product, condition, or affected component. Sparse records are marked as such and must not be used to invent code paths.
- Several CVE/GHSA identifiers may document the same underlying issue. Spring CVE-2024-22243 and CVE-2024-22259 are represented once. The WebOb and React Router follow-ups are kept as separate patch-regression examples and linked to their earlier fixes.
- A generated off-site URL is not automatically an exploitable redirect. Where the source reports URL generation rather than a redirect sink, the entry says a redirect/navigation sink must be confirmed in the application.
- “Open redirect” here includes untrusted server `Location` responses and browser-side external navigation from untrusted destinations. OAuth token/code leakage and XSS are identified as chained impacts, not assumed consequences of every redirect.
- Issue reports and incomplete/third-party CVE descriptions are kept outside the 60-case count in the companion file.

## Research method and limitations

Research used vendor and maintainer advisories, official security bulletins, NVD/CVE records, and GitHub issues where relevant. Sources were consulted on the date above. The inventory is a curated research snapshot, not an exhaustive search of every bounty platform or CVE. Some advisories omit exact handler names, versions, authentication requirements, or proof details; those gaps remain unknown. Severity labels are not treated as impact evidence.

The corpus supports static pattern discovery: trace untrusted values from requests, headers, stored state, OAuth parameters, route inputs and browser state into redirect/navigation sinks; inspect parsing, canonicalization and allowlisting in between. It does **not** establish that a specific repository has the relevant deployment settings, reachable route, vulnerable dependency version, or user interaction needed to exploit a case.

## Maintenance

For every new entry, record the direct advisory or report URL, source type/status, affected versions if stated, precise enabling conditions, source-to-sink flow, source-attributed impact, remediation, unknowns, and any relationship to an earlier case. Read the underlying advisory and, when available, its fix before promoting a search result into a confirmed entry. Keep leads and synthetic patterns separate, preserve links, and update the count only after deduplication.

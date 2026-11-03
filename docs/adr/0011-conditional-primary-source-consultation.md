# ADR-0011: Conditional primary-source consultation

- **Status:** Accepted
- **Date:** 2026-11-03
- **Decision owners:** Repository maintainers

## Context

Installable skills are intended to work on machines without general Internet access, so each package carries local summaries of the external documentation it cites. Those summaries cannot always preserve every version-specific behavior, exception, or current advisory detail. Several review instructions treated URLs as attribution-only and prohibited consultation even when an agent was connected and the missing fact could materially change a conclusion. Conversely, requiring online research at review time would break offline use and could encourage unnecessary disclosure of reviewed source code.

## Decision

Use package-local references first. When a suitable primary source is available, an agent may consult it only when a material detail absent from the local note and reviewed repository sources affects version applicability, configuration, behavior, impact, remediation, or confidence. The lookup is optional and must not become a prerequisite for using a skill. If the agent is offline or cannot verify the needed detail, it must state the uncertainty rather than infer from a title or search snippet.

Prefer the exact-version official documentation, maintainer advisory, standard, or source change. Record the source and access date in the finding or package note when that lookup supports a reusable claim. Keep local notes sufficiently detailed for the skill's ordinary offline workflow; enrich demonstrated gaps without imposing a word-count target. Never send private code, secrets, or user data to an external service. This decision permits documentation research only: it does not authorize application execution, target requests, payloads, or active scanning where a skill prohibits them.

This decision complements [ADR-0009](0009-offline-skill-references.md): offline references remain mandatory and sufficient for normal use, while focused primary-source consultation is an optional way to resolve a material gap.

## Consequences

Agents can resolve important public documentation gaps when connected without making network access a dependency. Reviews must distinguish locally established facts from newly verified source details and preserve unknowns when verification is unavailable. Maintainers should audit summaries for operational sufficiency and selectively expand entries whose missing conditions or limits could cause a wrong review conclusion. Public-source lookup must not disclose private project material.

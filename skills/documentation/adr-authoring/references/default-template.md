# Default ADR template

Use this template only when the repository has no existing ADR template. Adapt the status vocabulary and metadata to local conventions.

## Template

# ADR-NNNN: Short decision title

- **Status:** Proposed | Accepted | Rejected | Superseded by ADR-NNNN
- **Date:** YYYY-MM-DD (the date the decision was made)
- **Decision owners:** Team or maintainers, when known or required locally

## Context and problem statement

Describe the problem, constraints, and why a durable decision is needed. Separate established facts from unresolved assumptions.

## Decision

State the chosen approach clearly. If the decision is still pending, state the proposal and its approval status.

## Consequences

Describe significant positive and negative effects, follow-up work, and constraints created by the decision.

Optional sections, when useful:

- **Options considered:** Include only options the team actually considered and the reason for the selection.
- **Examples or implementation notes:** Add a small example or link when it makes the decision easier to apply.
- **References:** Link relevant requirements, discussions, or related ADRs.

## Reference basis

ADR formats vary. The template follows the concise context/decision/consequences structure associated with Michael Nygard's ADR format and the Markdown ADR (MADR) project. MADR and Microsoft guidance also describe recording alternatives, implications, and superseding decisions. Follow the repository's established template when it differs. The linked format sources are summarized for offline use in [offline source notes](offline-sources.md); their URLs are retained for attribution and future updates.

- [Michael Nygard: Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [MADR: About the format](https://adr.github.io/madr/)
- [MADR: ADR template](https://github.com/adr/madr/blob/develop/template/adr-template.md)
- [Microsoft Azure Well-Architected: Maintain an ADR](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)

# ADR-0009: Offline skill references

- **Status:** Accepted
- **Date:** 2026-11-03
- **Decision owners:** Repository maintainers

## Context

Coding agents may use these skills on machines without general Internet access. A Markdown link alone does not make its cited standard, framework behavior, or published advisory available after installation. Installable skills already bundle relative references, but some of those references still direct an agent to external pages for important details. Full third-party page copies also raise licensing and maintenance concerns.

## Decision

Every external technical source cited as a basis for operational guidance in an installable skill must have a concise, attributed paraphrase in that same skill package. Preserve the original URL as provenance and a future-update pointer; do not require the agent to open it during normal use. Record relevant versions, conditions, evidence limits, and unknowns where applicable. Do not reproduce full third-party pages unless their license explicitly permits it.

The package must remain usable after it is transferred to an offline machine. Remote installation commands are convenience paths only; offline installation uses a pre-staged repository or complete skill directory, a locally available CLI, or direct copy to the agent's configured skills location. When local reference notes do not establish version-specific behavior, the agent inspects source already present in the reviewed repository or reports the detail as unknown.

This decision complements [ADR-0001](0001-skill-layout-and-installation.md) on portable packaging and [ADR-0002](0002-corpus-evidence-and-provenance.md) on evidence, attribution, and third-party rights.

## Consequences

Installed skills can be used without scraping external pages, and each package carries the context needed for its own use. The packages become larger and their paraphrases need updates when sources or versions change. Local notes can become stale or omit nuance, so they must identify their date and limits; they do not replace code evidence or justify inferring an unrecorded version-specific behavior.

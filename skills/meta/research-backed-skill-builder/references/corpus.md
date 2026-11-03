# Organize a reusable corpus

Adapt to repository conventions; otherwise use `corpus/<domain>/<topic>/` for the corpus and `maintenance/<domain>/` for its maintenance method. Avoid machine-specific absolute paths in deliverables. The corpus remains available to maintainers, but the installed skill must include the references it needs unless requested otherwise.

## Minimum structure

- An index or README states topic, date, scope, research method, counts by status, sources, possible duplicates, exclusions, gaps, and relative links to detail files.
- Structured entries or rows group cases and examples; use Markdown, CSV, or JSON as appropriate. A collection of titles identifies leads, not a set of confirmed analyses.
- A section describes recurring technologies and mechanisms, protections or practices, and their limits; link conclusions to sources or label inferences.
- A maintenance plan explains how to enrich the corpus, verify sources, trace changes related to the skill, and preserve pre-existing data.

## Entry fields

When relevant, record `id`, `titre`, `categorie`, `source_url`, `auteur`, `date_publication`, `date_consultation`, `nature_source`, `statut_verification`, `technologie`, `versions`, `acteurs`, `conditions`, `entree`, `transformations`, `destination`, `mecanisme`, `impact_attribue`, `correction`, `preuve`, `limites`, and `relations_doublons`. Unknown values remain explicitly unknown; do not invent a complete schema when a field is inapplicable.

For security, distinguish vulnerability, prerequisites, actors, surfaces, observed or alleged exploitation, conditional impact, protections, and limitations; if documenting attacks or tools, add context and what results prove. For other domains, adapt fields to symptoms, conditions, effects, diagnostics, and fixes.

## Update an existing corpus

Read existing indexes and conventions, preserving content and sources; add or correct information with traceability. Deduplicate by identifier, note related entries and possible unestablished duplicates. Keep hypothetical scenarios, labs, and independent incidents clearly separate. A correction must state its origin and must not silently erase previous information or limitations.

# ADR-0001: Skill layout and installation

- **Status:** Accepted
- **Date:** 2026-11-03
- **Decision owners:** Repository maintainers

## Context

The repository needs to host multiple reusable skills across topics and make each skill installable without requiring users to copy an entire corpus or know repository-specific paths.

## Decision

Store installable skills under `skills/<domain>/<skill-name>/`, with a `SKILL.md` and any required relative references in the same directory. Group general skill-authoring methods under `skills/meta/`. Use the `skills` CLI as the supported discovery and installation path, and keep the repository README as the human-facing catalog.

## Consequences

A skill can be installed independently and must carry the operational material it needs. Research corpora and regeneration material remain in `corpus/` and `maintenance/`; skills may cite them as provenance but cannot require them at audit time by default. Adding a skill requires updating the catalog and checking CLI discovery.

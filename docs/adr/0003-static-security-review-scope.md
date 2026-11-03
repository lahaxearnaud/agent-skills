# ADR-0003: Static security review scope

- **Status:** Accepted
- **Date:** 2026-11-03
- **Decision owners:** Repository maintainers

## Context

The XSS and SQL injection skills are intended to help code agents assess a project's own source code when no application execution or runtime probing is available.

## Decision

The XSS and SQL injection review skills perform static analysis of available source, templates, configuration, dependencies and supplied static-analysis output. They do not launch the target application, a browser, payloads or active scanners. Findings distinguish an established source-to-sink path from a candidate with missing evidence, and neither status claims runtime exploitation.

## Consequences

The skills must state environmental unknowns and limits, and recommend code-level remediation. This boundary applies to those review workflows only; it is not a repository-wide prohibition on unrelated authorized tests or tools. A future dynamic-review skill must have its own explicit scope and ADR if it changes this architecture.

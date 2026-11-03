# ADR-0004: Skill language policy

- **Status:** Accepted
- **Date:** 2026-11-03
- **Decision owners:** Repository maintainers

## Context

Skills are reusable across coding agents and repositories, while the user and many source materials may use other languages.

## Decision

Write new skill instructions, operational references and skill READMEs in English by default unless the user explicitly requests another language. Preserve source-language quotations and identifiers accurately. Respond to users in the language they request, or otherwise in the language of their request. Human-facing repository documentation may retain its existing language.

## Consequences

Skill authoring language does not dictate the agent's response language. Existing French corpus and README content need not be translated as part of unrelated changes.

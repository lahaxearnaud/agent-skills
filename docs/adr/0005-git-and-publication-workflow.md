# ADR-0005: Git and publication workflow

- **Status:** Accepted
- **Date:** 2026-11-03
- **Decision owners:** Repository maintainers

## Context

Agents may prepare repository changes autonomously, but commits and publication have different effects. Changes must remain reviewable and must not accidentally include unrelated work or publish without the user's intent.

## Decision

Inspect and preserve the current worktree before editing. Stage only files for the requested change and make a targeted local commit for a repository deliverable when appropriate. Pushes, public releases, pull requests and branch merges require explicit user authorization. When authorized, use the branch and integration method the user specifies; authorization for one task does not automatically authorize publication of future changes.

## Consequences

Agents can complete and commit reviewable local work without publishing it. Before any authorized publication, inspect the exact diff and verify the destination. Report whether work is local, pushed, merged or otherwise published accurately.

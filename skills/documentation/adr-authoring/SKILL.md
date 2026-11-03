---
name: adr-authoring
description: Use when a durable architectural or repository-level decision needs an ADR, an existing decision must be superseded, or ADR guidance and indexes need updating.
---

# Authoring and maintaining ADRs

Use this skill to make a durable decision understandable and discoverable to future contributors. Treat the repository's own ADR policy as authoritative; use the defaults below only when the project has no established convention.

## Workflow

1. **Discover the project convention.** Read repository agent instructions such as `AGENTS.md` or `CLAUDE.md`, the main `README.md`, existing ADRs, their template, and their index. Follow the existing location, numbering, status vocabulary, required fields, and index. Do not create a second index when the project already has one.
2. **Confirm the decision and its scope.** ADRs are for durable choices that constrain future architecture, interfaces, platforms, dependencies, data or security boundaries, or repository-wide processes. Do not turn routine implementation details into ADRs. Distinguish an accepted decision from a proposal. Do not make an architectural choice on the team's behalf; ask only when missing information would materially change the record. Otherwise mark unknowns plainly.
3. **Write one focused record.** Use the project's template. If none exists, use `references/default-template.md`. The problem/context, decision, date, status, and consequences are required. Add alternatives, examples, diagrams, or implementation notes only when they clarify the decision. Follow an explicit ADR-specific language policy; otherwise use the primary language of the main README, even when historical ADRs use another language. If the README is absent or genuinely ambiguous, ask. Translate template headings as needed while preserving its fields. Preserve code identifiers and quotations accurately.
4. **Save and register it.** Use the project's ADR directory and identifier scheme. If neither is established, create `docs/adr/`, use the next unused four-digit number in a kebab-case Markdown filename, and add `docs/adr/0000-template.md`. If an ADR directory exists but has no template, add a local `0000-template.md` there, adapting its name to local conventions. If there is no existing ADR index, create an ADR register in `AGENTS.md` with a Markdown link, exact title, and brief description for each record. Update the register in the same change as the ADR.
5. **Preserve the decision history.** Never delete or replace an accepted ADR. When a decision changes, write a new record that links to the earlier one; update its status or add a supersession link only as the project convention requires. Keep both records discoverable.
6. **Verify the result.** Check the diff, unique numbering, required fields, date and status conventions, resolved relative links, and complete index entries. Keep summaries faithful to the decision; do not invent rationale, alternatives, owners, or consequences.

## Default selection rules

- Prefer existing repository instructions and templates over this skill's defaults.
- Use an explicit ADR language policy when the repository has one; otherwise use the README's primary language for ADR prose. Ask only when the README is missing or language cannot be determined confidently.
- Record the date the decision was made, not automatically the date the ADR was drafted. Determine it from the request or project history; if it is not clear, ask rather than inventing it. Use the repository's date format or `YYYY-MM-DD` when none is established.
- If a decision is not approved, mark it `Proposed` or the project's equivalent rather than presenting it as accepted.
- Keep the ADR concise and focused on one decision. Examples and alternatives are optional, not required filler.

See `references/default-template.md` for the fallback template and its source basis.

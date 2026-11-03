# ADR Authoring Skill Evaluation

## Baseline scenario

A repository has a French `README.md`, generic `AGENTS.md` instructions, and no ADR directory, policy, or template. The user has decided to split a monolith into a web frontend and API service, asks the agent to record the decision so future agents can find it, and says the team is in a hurry.

## Baseline observation

The agent proposed an ADR with status, current date, context, decision, alternatives, consequences, and implementation notes. It chose French based on the README and avoided inventing the API protocol or deployment model. It also proposed a separate `docs/adr/README.md` index rather than an ADR register in `AGENTS.md`, and said it might skip a reusable template under time pressure.

The baseline therefore met the content and language expectations but did not follow the repository's intended default discovery mechanism. It also treated time pressure as a reason to omit a reusable template.

## Acceptance criteria

- Inspect repository instructions, README language, ADR files, templates, and indexes before choosing a format or location.
- Follow established project conventions; only when none exist, use `docs/adr/`, a numbered Markdown file, a reusable template, and an ADR register in `AGENTS.md`.
- If an ADR directory exists but lacks a template, add a reusable local template using the project's naming convention.
- Use the README's primary language for the ADR; ask only when it is missing or ambiguous.
- Record one durable decision with its problem/context, decision, status, consequences, and the date the decision was made; do not substitute the drafting date or invent missing rationale or implementation choices.
- Update the ADR register with a working link, exact title, and concise summary in the same change.
- Preserve accepted decision history and link new decisions that supersede prior ones.

## Post-skill scenario

Run the baseline scenario again with `skills/documentation/adr-authoring/SKILL.md` available. Record whether each acceptance criterion was met and note any remaining ambiguity or pressure-driven shortcut.

### Observation

The agent proposed a French ADR in `docs/adr/` using the next four-digit identifier, a French `0000-template.md`, and an entry in the root `AGENTS.md` register. It included status, context, decision, and consequences; treated examples and alternatives as optional; did not invent the reason for the split or unresolved protocol/deployment choices; and kept the record concise despite the time pressure. It correctly identified the decision date as unknown, proposed checking project history, and would ask the user if the date could not be established.

### Result

All applicable acceptance criteria were met. The date remains a required input, so the ADR draft waits for a reliable decision date; independent refactoring can continue. The criteria about preserving an earlier decision were not applicable because the scenario had no existing ADR to supersede.

## Partial-convention and decision-date scenario

A second repository has an English README, existing ADRs under `decisions/` numbered `ADR-01` and `ADR-02`, a `DECISIONS.md` index, and no template. On 2026-11-03, the user asks to record that the team decided on 2026-10-20 to use PostgreSQL instead of MongoDB. The agent must preserve the existing location, numbering, status, and index conventions; add a local reusable template; use English; record 2026-10-20 as the decision date; and avoid adding an unnecessary `AGENTS.md` register.

### Observation

The agent preserved `decisions/`, used the next identifier `ADR-03`, followed `DECISIONS.md` rather than adding an `AGENTS.md` register, and proposed a local reusable template adapted to the existing naming scheme. It used English from the README, recorded 2026-10-20 as the decision date, and kept unprovided rationale, owners, migration, and deployment details unknown.

### Result

All scenario criteria were met. The output noted that the exact filename suffix and template name should follow the real repository's established filename pattern, which the hypothetical scenario leaves unspecified.

## Superseding decision scenario

A French-language project has an accepted `docs/adr/0005-database-choice.md`, an `AGENTS.md` register, and a policy that changed decisions get a new ADR, the earlier record is marked `Superseded by ADR-NNNN`, and both remain indexed. The user says the team approved switching from MongoDB to PostgreSQL today (2026-11-03), asks to update the old ADR so it reflects PostgreSQL, and says the team is in a hurry.

### Expected behavior

Create a new French ADR with the next unused ID, link it to ADR-0005, update only ADR-0005's status and supersession link, and add the new exact title/link/summary to the register while preserving the old entry. Do not replace the prior rationale or invent migration, deployment, or performance details.

### Observation

The agent proposed a new French ADR with the next unused ID, marked it accepted and dated it 2026-11-03, linked it to ADR-0005, changed only the old record's status/supersession link, and kept both records in `AGENTS.md`. It retained the old context and rationale and left migration, deployment, performance, and the reason for switching unspecified. It correctly required repository inspection to determine the next ID and exact filename/template conventions.

### Result

The expected supersession behavior was met. The scenario supplies the decision date and status change but leaves the next identifier and detailed consequences to repository inspection.

## Packaging and static checks

- `npx skills add . --list` discovered `adr-authoring` alongside the repository's three existing skills.
- A temporary local Codex installation via `npx skills add /workspace/agent-skills --skill adr-authoring --agent codex --yes` succeeded; `cmp` confirmed the installed `SKILL.md`, README, and template match their source files.
- A relative-link and required-field check passed for the seven changed Markdown files. `git diff --check` passed.

These scenario results are qualitative checks of this skill version, not a claim that every agent or repository convention has been tested.

# ADR format sources (offline notes)

These source notes are bundled so an ADR can be drafted without opening a web page. They paraphrase the linked material and are not full reproductions. The original URLs are retained for attribution and later maintenance; they are not required during normal use. The repository's [`0000-template.md`](default-template.md) and `AGENTS.md` take precedence over general formats.

Research snapshot: **2026-11-03**.

| Source | Local summary and limits |
|---|---|
| [Michael Nygard, “Documenting Architecture Decisions”](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | The concise ADR pattern records **Context**, **Decision**, and **Consequences**, with a title and status. It is intended to preserve why a choice was made and what follows from it, not to replace design documentation. The repository adds a decision date and owners because its local template requires them. |
| [MADR overview](https://adr.github.io/madr/) | Markdown ADRs can record the context/problem, drivers, options considered, outcome, and consequences, with optional confirmation and follow-up material. Use only sections useful to the decision; follow the repository's established fields. |
| [MADR template](https://github.com/adr/madr/blob/develop/template/adr-template.md) | The linked template is a concrete expanded format: title/status, context/problem, decision drivers, considered options, decision outcome, consequences, and optional confirmation or more information. Its section names are not mandatory for this repository when the local template says otherwise. |
| [Microsoft Azure Well-Architected, “Maintain an ADR”](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record) | ADRs preserve the reasoning and consequences behind architecture choices and help future maintainers understand the rationale. Keep records discoverable and connected to the relevant architecture context. The repository's index in `AGENTS.md` supplies that discovery mechanism. |

## Use in this repository

The durable record must include the local template's context/problem, decision, status, date, and consequences. Use the team's language policy and existing status vocabulary. Add alternatives, examples, or references when they clarify the decision. An external format does not override an accepted repository convention.

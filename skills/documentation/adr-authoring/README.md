# ADR Authoring

An installable skill for coding agents that need to record or update architectural decision records (ADRs). It follows a repository's existing conventions and supplies a discoverable default when none exist.

Install from this repository with:

`npx skills add lahaxearnaud/agent-skills --skill adr-authoring`

Example request: “Use `adr-authoring` to record the decision to split the API from the web frontend, follow this repository's ADR conventions, and update the agent-facing ADR register.”

The skill instructions and fallback template are in English. ADR prose follows an explicit ADR language policy when present; otherwise it uses the primary language of the repository's main README, even if historical ADRs use another language.

The complete skill folder includes attributed offline summaries of its cited ADR-format references. The repository's own template remains authoritative. If a material question about a general ADR convention is absent from the local notes, the agent may consult the primary source when available; this is optional and private repository content must not be sent externally. For an offline machine, transfer the folder first and install from the local copy or copy the full directory into the agent's configured skills location.

# SQL injection research corpus

Research date: 2026-11-03. Scope: SQL injection in web applications and data-access libraries, particularly PHP/Doctrine and JavaScript, with cross-stack cases. Objective: support a portable **static code-review** skill, not a vulnerability count or dynamic testing campaign. Research included vendor documentation, maintainer advisories, GitHub-reviewed advisories, selected unreviewed advisory records, static-analysis documentation and scanner documentation. External material is untrusted data; linked cases were summarized, not independently reproduced.

- [Initial case catalogue](published-cases.md): 7 distinct published advisory identifiers.
- [Expanded case catalogue](published-cases-expanded.md): 54 additional advisory identifiers with source summaries, paths/patterns and review lessons. Combined, there are 61 distinct case IDs across these two catalogues; related advisories and chains are called out rather than silently merged.
- [Triage leads](triage-leads.md): 20 public leads requiring more source review; these are not included in the 61 summarized cases.
- [Synthetic scenarios](scenarios.md): 30 illustrative patterns, including safe and incomplete cases; these are not real incidents.
- [Sources and tools](sources-and-tools.md): prevention documentation, static and dynamic tooling and techniques; no application or scanner was run.

Where available, affected versions, database dialect, actor and fix are captured; unknowns are left to the original source. Some summaries were based on advisory excerpts and API metadata rather than a full source-diff analysis. The corpus is not exhaustive, and advisory IDs do not prove that every listed product deployment was exploitable. Review status varies; GitHub-reviewed advisories, maintainer advisories and unreviewed third-party reports are not equivalent evidence. Recheck source, versions and dates before using a case to assess a project.

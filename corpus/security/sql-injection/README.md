# SQL injection research corpus

Research date: 2026-11-03. Scope: SQL injection in web applications and data-access libraries, particularly PHP/Doctrine and JavaScript, with cross-stack cases. Objective: support a portable **static code-review** skill, not a vulnerability count or dynamic testing campaign. Search combined vendor documentation, primary maintainer advisories, static-analysis documentation and scanner documentation; linked pages were consulted, not reproduced. External content is untrusted research data. Publication dates are listed where directly checked; unknown versions, actors and technical details remain unknown. Each advisory is one documented report, not evidence that an application using the component is exploitable.

- [Published cases](published-cases.md): 7 distinct advisory IDs, checked at their linked primary sources; some descriptions are limited to the advisory and not independently reproduced.
- [Synthetic scenarios](scenarios.md): 20 invented review patterns, including safe and ambiguous cases; not real incidents.
- [Sources and tools](sources-and-tools.md): prevention documentation, static and dynamic tooling and techniques; no application or scanner was run.

Known gaps: no exhaustive advisory, bug-bounty or technology coverage; no independent execution or fix verification; no statistical measurement of detection performance. Advisory IDs may describe related underlying patterns without establishing duplicates. Update versions and dates from the original source before use; details below are a snapshot.

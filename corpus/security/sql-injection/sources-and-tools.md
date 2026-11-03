# Sources, observations and tools

Consulted 2026-11-03. Links are to source owners; source language and identifiers are preserved. Documentation can change. Version-specific assertions must be checked against the target's pinned version.

| Source | Kind and use | Limit |
|---|---|---|
| [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) | Primary project guidance: binding values, safe dynamic structure, stored procedures, least privilege. | General guidance; verify library and dialect. |
| [Doctrine DBAL 4.4 Query Builder](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/query-builder.html) | Maintainer documentation: only pagination methods are automatically protected; parameters for values. | Applies to documented DBAL version, not automatically to all ORMs. |
| [PortSwigger SQL injection](https://portswigger.net/web-security/sql-injection) | Provider's intentional training material; explains in-band/blind patterns and impacts. | Labs are hypothetical; runtime testing is outside this skill. |
| [CodeQL JS SQL injection query](https://codeql.github.com/codeql-query-help/javascript/js-sql-injection/) | GitHub documentation: static path analysis and parameterization. | Language, framework, models and build coverage matter; findings require review. |
| [sqlmap usage](https://github.com/sqlmapproject/sqlmap/wiki/Usage) | Maintainer documentation of a dynamic scanner; boolean, error, union, stacked and time techniques are different observations. | Tool actively sends probes and may perform intrusive actions; neither installed nor run here, and its result would not replace source tracing. |

Payload families can help reason about quote contexts, boolean predicates, error messages, UNION, timing and out-of-band channels. These are observation techniques, not separate root causes; their viability depends on dialect, grammar position, privileges and external behavior. The skill does not request or execute probes. No raw scanner corpus, exploit payload, third-party page or secret was copied into this corpus. Consult original tool documentation for exact version, current capabilities and terms.

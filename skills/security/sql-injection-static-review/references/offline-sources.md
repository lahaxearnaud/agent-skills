# SQL injection sources (offline notes)

These attributed paraphrases provide the source details needed for ordinary offline static review; they are not full copies. Read them first. When online, consult a suitable primary source only if a material version, dialect, configuration, or API detail is not established by these notes or the reviewed repository. This is optional; offline, state the unknown. Never send private code or repository data to an external service. Version-specific claims apply only to the version named below.

Research snapshot: **2026-11-03**.

## Query-builder and prevention guidance

| Source | Local summary and limits |
|---|---|
| [Doctrine DBAL 4.4 Query Builder](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/query-builder.html) | In documented DBAL 4.4, only `setFirstResult()` and `setMaxResults()` have built-in protection for their arguments. Most methods accept SQL expressions; bind data values, and map structural choices such as column names and sort directions to fixed code-owned values. Do not generalize this version-specific statement to Doctrine ORM, other DBAL versions, or other query builders. |
| [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) | Prefer parameterized queries for values. When SQL structure must vary, choose from an allowlist of code-owned identifiers or expressions. Stored procedures require safe parameter use internally; escaping is a fallback tied to a specific database/dialect, not a universal substitute. Least privilege reduces consequences but does not remove an injection flaw. |
| [CodeQL JavaScript SQL injection query help](https://codeql.github.com/codeql-query-help/javascript/js-sql-injection/) | The `js/sql-injection` query uses taint tracking to find an untrusted value that can affect a SQL query string passed to a modeled database API. Query source/sink models and library coverage vary by CodeQL pack and version. Inspect the reported path, query-building code, database API and reachable execution. An empty result does not establish safety, and a finding is a lead rather than proof that a particular deployment is exploitable. |

## Published examples

| Advisory | Local case summary |
|---|---|
| [Django ORM alias issue, GHSA-hpr9-3m2g-3j9p](https://github.com/advisories/GHSA-hpr9-3m2g-3j9p) | Crafted dictionary keys expanded as keyword arguments to ORM methods such as `annotate`, `alias`, `aggregate`, or `extra` could affect column-alias SQL on MySQL/MariaDB. The relevant lesson is dialect-specific structural escaping: trace the key into the generated query and do not assume the same behavior on every backend. |
| [Admidio stored list configuration, GHSA-3x67-4c2c-w45m](https://github.com/admidio/admidio/security/advisories/GHSA-3x67-4c2c-w45m) | Authenticated list column names, sort directions, and filter conditions were stored using prepared statements, then interpolated into generated SQL later. Safe persistence did not make later structural use safe; trace second-order values through storage to their eventual query sink. |
| [NocoBase workflow SQL template, GHSA-vx58-fwwq-5g8j](https://github.com/nocobase/nocobase/security/advisories/GHSA-vx58-fwwq-5g8j) | Workflow template values were substituted into raw SQL passed to Sequelize without parameterization; the advisory identifies affected releases through 2.0.8. Inspect post-substitution text and the raw-query call: the driver cannot infer which parts of a completed SQL string were untrusted. |

The case summaries are examples of source-to-sink shapes, not claims about an audited repository. Confirm the exact package version, SQL dialect, caller control, and query execution path in the current source.

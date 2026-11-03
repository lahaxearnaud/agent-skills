# Published SQL injection cases

Consulted 2026-11-03. These are summaries of maintainer advisories, not independent reproductions. Each describes an SQL injection; exposure, actor, control flow and real-world exploitation are limited to what the linked source states. When reviewing another application, check deployed version, DBMS and relevant call path.

## P01 — Sequelize replacements, CVE-2023-25813

[Sequelize GHSA-wrh9-cjv3-2hpw](https://github.com/sequelize/sequelize/security/advisories/GHSA-wrh9-cjv3-2hpw), published 2023-02-22; npm sequelize < 6.19.1, fixed 6.19.1. A combination of a `where` option and replacements went through multiple query-processing steps: previously constructed SQL was reparsed for replacements, including placeholder-like content inside an already rendered value. Impact is SQL injection when the affected pattern and controllable inputs are present. Lesson: trace transformations across multiple passes; safe-looking ORM use depends on the library implementation and version. This summary does not establish application-level reachability.

## P02 — WordPress `author__not_in`, CVE-2026-60137

[WordPress GHSA-fpp7-x2x2-2mjf](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-fpp7-x2x2-2mjf), published 2026-07-17. Affected 6.8.0–6.8.5, 6.9.0–6.9.4, 7.0.0–7.0.1; fixes 6.8.6, 6.9.5, 7.0.2. Advisory identifies SQL injection in `WP_Query` parameter `author__not_in`; it also describes an RCE chain with a separate batch-route issue in 6.9+. Input control and exact call path are application-dependent; the RCE chain is not implied by this SQLi alone. Treat the API parameter as a lead and inspect caller, version and advisory details.

## P03 — Drupal database abstraction, CVE-2026-9082

[Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004), published 2026-05-20, updated 2026-05-22. Maintainer reports SQL injection in Drupal core database abstraction for PostgreSQL sites and anonymous exploitation; advisory states information disclosure and conditional escalation or RCE. Version ranges and fixes are in the source. The maintainer notes attempts in the wild; that does not establish compromise of any specific installation. Review database backend and relevant application exposure; don't assume the abstraction is a guarantee.

## P04 — Vendure language code in SQL expression, CVE-2026-40887

[Vendure GHSA-9pp3-53p2-ww9v](https://github.com/vendurehq/vendure/security/advisories/GHSA-9pp3-53p2-ww9v). The advisory identifies request-context `languageCode` interpolated into a SQL CASE expression before TypeORM's query builder receives it. Check the advisory for exact ranges, fix and attacker requirements. The central detection pattern is data → template interpolation → raw `addSelect` expression: later ORM processing cannot retroactively bind the embedded value. Impact is specific to the affected call and configuration.

## P05 — ElectricSQL ORDER BY parser, GHSA-h5rg-pxx7-r2hj

[ElectricSQL maintainer advisory](https://github.com/electric-sql/electric/security/advisories/GHSA-h5rg-pxx7-r2hj). The authenticated Shape API accepted an `order_by` expression; permissive AST validation was followed by passing the original raw string into PostgreSQL. The advisory describes error-based injection and broad database impact. The fix applies a deny-by-default AST allowlist and rebuilds SQL from the validated AST. Verify version and privileges in the source. Lesson: validating a parsed representation but executing the original text can break the intended security boundary.

## P06 — MISP ordering, GHSA-4cxp-22wm-j6jr

[MISP maintainer advisory](https://github.com/MISP/MISP/security/advisories/GHSA-4cxp-22wm-j6jr) describes unvalidated ordering parameters in event and shadow-attribute listings. Its remediation validates fields against allowed model fields/schema and normalizes ordering directions before building SQL. Review the advisory for releases, access requirements and full impact; no independent exploit validation. Lesson: trace both field and direction and check the database execution boundary.

## P07 — TypeORM update/soft-delete ordering, GHSA-9ggv-8w38-r7pm

[TypeORM maintainer advisory](https://github.com/typeorm/typeorm/security/advisories/GHSA-9ggv-8w38-r7pm) identifies SQL injection in update/soft-delete query-builder ordering for MySQL/MariaDB. The exact affected versions, required controllability and patch must be checked in the advisory. This is a dependency implementation issue; do not conclude a project is exploitable from the presence of TypeORM or `orderBy` alone.

# Frameworks, controls and limitations

## Separate values and SQL structure

Use the database library's parameter binding for each untrusted value, matching placeholder syntax and number to the API. Verify the text was not assembled unsafely *before* prepare or execute. Parameter placeholders normally represent values, not identifiers, keywords, directions or arbitrary expressions; map external choices to fixed code-owned constants and reject unknown values. For variable-size lists use documented array/list parameters or one placeholder per item and bind every item; empty-list behavior is a separate branch. Use native identifier quoting only when appropriate for the specific dialect, API and configuration; a strict allowlist is preferable where options are known.

Numeric parsing can prevent injection in a specific numeric position if the conversion is effective, dominates all paths and outputs only an integer; range, overflow and application semantics still require review. Escaping and blacklist filters depend on dialect, encoding and context; avoid treating a generic escaping function or WAF as universal SQL protection. A bound LIKE pattern preserves wildcard behavior; escape pattern characters separately if literal matching is required. Parameter binding does not itself enforce authorization or tenant isolation.

## PHP and Doctrine

- Inspect `PDO::prepare` plus `execute`/`bindValue`; a placeholder in the text does not protect another concatenated fragment. Check emulation, driver and configuration before making version-specific assertions. Doctrine DBAL `executeQuery`/`executeStatement` accept parameters; confirm the exact installed version and types.
- Doctrine DBAL's query builder accepts SQL expressions in most methods. In documented 4.4, only `setFirstResult` and `setMaxResults` have built-in injection protection; `where`, `orderBy`, identifiers and raw expressions require specific care. Use parameters for values and code-owned maps for identifiers. DQL/ORM queries and native SQL are distinct languages with different APIs: check each builder and escape hatch. See the bundled [offline Doctrine note](offline-sources.md).
- Stored procedures are not automatically safe: inspect dynamic SQL inside the procedure and whether values are bound there.

## Other stacks

- JavaScript/TypeScript: distinguish node-postgres parameter arrays, ORM bind/replacement modes and raw/literal APIs. Verify tagged template APIs versus unsafe variants and whether interpolation represents a value or a raw fragment. ORM version bugs can break expected guarantees; applicability requires versions and relevant call pattern.
- Python: DB-API placeholder conventions differ by driver; passing an SQL string constructed with `%`, f-strings or `.format()` before `execute` is not binding. Examine raw ORM queries and SQL expression helpers.
- Java/.NET: trace JDBC `PreparedStatement` or ADO.NET parameters and stored procedure internals; `Statement`, native queries, concatenated HQL/JPQL and dynamic expression APIs warrant review. A finding in HQL/JPQL should be named for its actual query language rather than assumed to be raw SQL.
- Use [offline source notes](offline-sources.md) for the cited OWASP and Doctrine guidance. For version-specific behavior not covered locally, inspect documentation or source already present in the dependency; do not require network access during a review.

SQLi impact is conditional: query type, database account permissions, DBMS features, network and deployment affect whether reading, modifying, deleting or further escalation is possible. Do not claim operating-system execution from SQL injection alone. WAF or error suppression can affect observability but does not repair an unsafe SQL boundary.

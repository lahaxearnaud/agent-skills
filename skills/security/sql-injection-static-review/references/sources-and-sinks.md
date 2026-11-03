# Sources, sinks, and tracing

## Sources and boundaries

Inspect HTTP route/query/body, headers, cookies, route parameters, uploads, GraphQL variables, webhook data, CLI arguments and imported files. Data from another service, cache, message queue, configuration editable by users or database rows can be attacker-influenced. Identify who can write each input; authenticated, privileged and anonymous access are different preconditions. Persisting or HTML-escaping a value does not make it safe as SQL.

Track normalization, parsing, decoding, type changes, mapping, validation and branch conditions. Follow wrapper functions, repository layers, custom query builders, job handlers and stored procedures. For second-order injection establish both storage and later retrieval with the same field; do not assume a link that code does not show.

## Candidate sinks and SQL construction

Search names relevant to the actual stack; hits are leads, not findings:

```bash
rg -n -i 'executeQuery|executeStatement|createQueryBuilder|createQuery|prepare\(|query\(|raw\(|execute\(|executemany|orderBy|addOrderBy|whereRaw|selectRaw|literal\(|sequelize\.query|\$queryRawUnsafe|\$executeRawUnsafe|cursor\(|DB::(select|statement|unprepared)' .
```

Inspect also functions that construct SQL passed to the above, stored procedures with `EXECUTE`/`EXEC`/`sp_executesql`, ORM native query APIs, migrations, search filters, reporting and admin tooling. Names have different meanings in different stacks; resolve imports, wrappers and versions. Review SQL-generating code and dataflow, including dynamically selected identifiers, joins, ORDER BY/GROUP BY, LIMIT/OFFSET, LIKE, IN lists and bulk operations. A prepared query can still contain unsafe interpolated syntax.

Static analyzers can provide leads and paths, but missing framework models, code generation, dynamic dispatch, interprocedural and storage boundaries cause gaps. Validate each finding against source, binding and reachable execution. An empty scan is not proof of safety. [CodeQL JavaScript SQL injection query](https://codeql.github.com/codeql-query-help/javascript/js-sql-injection/) documents a path query and associated remediation; check availability and models for the actual language and version.

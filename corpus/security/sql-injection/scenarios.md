# Synthetic SQL review scenarios

These examples are illustrative, not observed incidents. For each, reachability, actor, validation, DB dialect and version must be verified in the code under review. Technique names do not prove any runtime oracle or impact.

| ID | Source → construction → destination | Review condition and remedy |
|---|---|---|
| S01 | HTTP id → string concatenation → executed WHERE | Grammar may be controlled; bind id. |
| S02 | JSON search → interpolation into quoted string → raw query | Quotes do not protect interpolated input; bind value. |
| S03 | Sort key → Doctrine `orderBy` → execute | Map key to fixed column; trace execution and validation. |
| S04 | Sort direction → SQL suffix | Map independently to fixed ASC/DESC constants. |
| S05 | User-selected table → interpolated FROM | Bind parameters cannot normally represent table names; map identifiers. |
| S06 | Filter operator → raw WHERE expression | Restrict to fixed operator mapping; bind operand. |
| S07 | Array → comma-joined IN clause | Bind each element using documented list expansion; handle empty list. |
| S08 | Request → stored record → cron query concatenation | Trace both storage and consumption; bind at later sink. |
| S09 | Queue message → reporting template → execute | Treat queue producer/control as a trust boundary; bind fields. |
| S10 | GraphQL variable → resolver → raw SQL | GraphQL is transport, not a SQL sanitizer; trace resolver. |
| S11 | Binding plus interpolated ORDER BY | Binding one value does not protect another SQL fragment. |
| S12 | Fixed prepare with bound name | Negative for that value if API actually binds; inspect rest separately. |
| S13 | SQL string assembled before PDO prepare | Preparing after interpolation is too late for the already inserted fragment. |
| S14 | Stored procedure parameter → dynamic EXEC inside procedure | Inspect internal dynamic SQL and internal binding; calling a procedure alone is not proof of safety. |
| S15 | Bound LIKE with wildcard characters | SQL grammar safe for that value; wildcard behavior may be a separate business-logic risk. |
| S16 | Validated integer → fixed `%d` numeric slot | Negative for SQL grammar injection at that slot if conversion dominates all paths; prefer binding, check range. |
| S17 | Parser allowlists AST but executes original input | Inspect mismatch between validated and executed representation; reject or generate from safe AST. |
| S18 | Dependency advisory + version unknown | Candidate dependency exposure only; establish version and affected use. |
| S19 | Trusted constant SQL → query executor | No attacker control established; search caller only if value is actually variable. |
| S20 | User input → unobserved wrapper → SQL sink | Candidate until wrapper behavior, source control and execution are demonstrated. |

## Additional synthetic review patterns

These additions are also hypothetical and do not increase the published-incident count.

| ID | Pattern | Static review question |
|---|---|---|
| S21 | Django `**kwargs` dictionary built from request keys and passed to `values()`/`annotate()` | Can keys become SQL aliases, relation paths or operators? Restrict to fixed field mappings. |
| S22 | JSON object key passed to ORM JSON path or cast helper | Can the key encode a type, identifier or SQL fragment in the dialect adapter? |
| S23 | Request `sort` has validated column but unvalidated direction | Is the direction a closed enum before the SQL builder? |
| S24 | A sanitized search term is interpolated into a raw ORDER BY similarity expression | Does sanitization happen before interpolation and for the exact SQL context? Bind values; allowlist structure. |
| S25 | Workflow editor stores a SQL template with expression placeholders | Which roles can edit/trigger it, and are substitutions bound values or raw fragments? |
| S26 | Signed-looking pagination token is decoded into sort/limit/offset fields | Is it authenticated and are fields range-checked or mapped before SQL use? |
| S27 | Generated application template concatenates a web request's sort parameter | Does the vulnerability exist in already generated output as well as the generator source? |
| S28 | Database helper quotes an identifier but dialect escape character is not escaped | Verify identifier quoting rules and version, or use a strict allowlist. |
| S29 | Parser validates a query AST then executes the original raw string | Is the validated representation the one serialized and sent to the database? |
| S30 | SQL comment or query-tag helper rewrites SQL before binding | Can comment formatting or placeholder parsing change lexical boundaries in this driver version? |

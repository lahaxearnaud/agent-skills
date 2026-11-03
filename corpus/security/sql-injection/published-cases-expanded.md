# Expanded catalogue of published SQL injection reports

Research date: 2026-11-03. The original [seven-case set](published-cases.md) remains intact. This catalogue adds **54 distinct advisory identifiers** whose title and technical description were examined in linked project advisories or GitHub Advisory Database records. Some descriptions were read through search excerpts and advisory metadata rather than a full independent code review; these are sourced summaries, not reproduced exploits. Versions and preconditions are stated only when the consulted source established them; consult the linked advisory for exact ranges and patches. Each identifier is a published report, not proof that every application using that product is vulnerable.

A further [triage register](triage-leads.md) preserves **15 additional leads** from public advisory search results. Those entries are explicitly marked unreviewed or incompletely examined and are not included in the 54 checked cases. Related advisories are retained when they document distinct code paths or affected releases, with relationships noted; search-result duplicates are not counted twice.

## Frameworks, ORMs and query construction

### Django: SQL structure hidden in ORM metadata

**A01 — CVE-2026-1207, RasterField band index.** [GHSA-mwm9-4648-f68q](https://github.com/advisories/GHSA-mwm9-4648-f68q). Django's PostGIS-only raster lookup accepted a band-index value that could reach SQL construction. The advisory states remote SQL injection and lists affected Django release branches. **Review:** ORM lookup arguments can become SQL syntax even when ordinary filter values are bound; trace specialized field/lookups and backend-specific methods.

**A02 — CVE-2026-1312, `order_by()` and `FilteredRelation` aliases.** [GHSA-6426-9fv3-65x8](https://github.com/advisories/GHSA-6426-9fv3-65x8). A crafted dictionary expanded as kwargs can create column aliases containing periods, then flow through `FilteredRelation` and `QuerySet.order_by()`. Affected supported branches and fixed releases are listed in the source. **Review:** follow attacker-shaped dictionary keys through `**kwargs`, aliases, relation metadata and later ordering.

**A03 — CVE-2026-1287, aliases containing control characters.** [GHSA-gvg8-93h5-g6qq](https://github.com/advisories/GHSA-gvg8-93h5-g6qq). Crafted alias keys passed via dictionary expansion to `annotate`, `aggregate`, `extra`, `values`, `values_list` or `alias` can affect SQL in a `FilteredRelation` path. The advisory covers supported Django branches and notes unsupported historical branches were not evaluated. **Review:** control-character handling and normalization in generated aliases; do not treat ORM-generated names as inherently safe.

**A04 — CVE-2025-64459, `Q`/QuerySet `_connector`.** [GHSA-frmv-pr5f-9mcr](https://github.com/advisories/GHSA-frmv-pr5f-9mcr). A crafted dictionary expanded into `_connector` on `Q` and `filter`, `exclude` or `get` could influence SQL. The advisory lists affected Django 4.2, 5.1 and 5.2 releases. **Review:** internal-looking kwargs and dictionary expansion at ORM boundaries; validate the shape and origin of dynamic kwargs.

**A05 — CVE-2025-59681, MySQL/MariaDB column aliases.** [GHSA-hpr9-3m2g-3j9p](https://github.com/advisories/GHSA-hpr9-3m2g-3j9p). Crafted dict keys expanded as kwargs to `annotate`, `alias`, `aggregate` or `extra` could inject through column aliases on MySQL/MariaDB. **Review:** backend-specific alias escaping; the same code may behave differently by SQL dialect.

**A06 — CVE-2025-13372, PostgreSQL `FilteredRelation` aliases.** [GHSA-rqw2-ghq9-44m7](https://github.com/advisories/GHSA-rqw2-ghq9-44m7). Dictionary-expanded alias values used with `FilteredRelation` in `annotate`/`alias` could reach SQL unsafely on PostgreSQL. The advisory names affected Django branches. **Relationship:** same broad alias family as A05, but distinct backend/release advisory; confirm whether another identifier covers the same underlying fix before counting incidents.

**A07 — CVE-2024-42005, `JSONField` values aliases.** [GHSA-pv4p-cwwg-4rph](https://github.com/advisories/GHSA-pv4p-cwwg-4rph). `QuerySet.values()` and `values_list()` on models with a `JSONField` were vulnerable through a crafted JSON object key supplied as a positional argument. **Review:** user-influenced JSON keys can enter SQL identifier/alias positions even when JSON values are data.

**A08 — CVE-2022-28347, `QuerySet.explain()` option names.** [GHSA-w24h-v9qh-8gxj](https://github.com/advisories/GHSA-w24h-v9qh-8gxj). A crafted dictionary expanded as `**options` could place an attacker-controlled option name into `QuerySet.explain()` SQL. **Review:** option names and mapping keys can matter as much as values when APIs translate them into syntax.

**A09 — Laravel SQL Server `LIMIT`/`OFFSET`.** [GHSA-4mg9-vhxq-vm7j](https://github.com/laravel/framework/security/advisories/GHSA-4mg9-vhxq-vm7j). Laravel's `limit`, `offset`, `skip` and `take` paths were vulnerable on SQL Server when request input reached them directly; the advisory says MySQL and PostgreSQL were not affected. **Review:** pagination safety is dialect-specific; inspect coercion and the actual driver rather than assuming a query builder sanitizes numeric clauses.

**A10 — Mautic Contact Activity API sort direction.** [GHSA-r5j5-q42h-fc93](https://github.com/mautic/mautic/security/advisories/GHSA-r5j5-q42h-fc93). Authenticated API input controlling sort direction was not strictly allowlisted in contact activity query construction. Fixed releases are listed by the maintainer. **Review:** validate direction as a closed enum independently of the column name.

**A11 — Hi.Events repository `sort_by`.** [GHSA-2qcp-24fh-fx6p](https://github.com/HiEventsDev/Hi.Events/security/advisories/GHSA-2qcp-24fh-fx6p). Multiple PHP repository classes passed a user-supplied `sort_by` directly to Eloquent `orderBy`. **Review:** search all repository implementations; similar unsafe call sites may be replicated across entities.

**A12 — Cacti automation tree rules.** [GHSA-f9c7-7rc3-574c](https://github.com/Cacti/cacti/security/advisories/GHSA-f9c7-7rc3-574c). Incompletely checked values persisted in automation tree-rule configuration later reached SQL concatenation in `build_rule_item_filter()`. The advisory describes secondary impact through database modification and potentially file access/write paths. **Review:** trace stored configuration into later SQL; do not stop at safe parameterized persistence.

**A13 — CakePHP query pagination.** [CakePHP advisory GHSA-2qh5-382h-3jpc](https://github.com/cakephp/cakephp/security/advisories/GHSA-2qh5-382h-3jpc). The project advisory reports SQL injection through `Database\Query::offset()` and `limit()`. **Review:** verify the exact CakePHP version, connection dialect, and whether external values reach pagination methods without bounded numeric conversion.

**A14 — Mautic API Contact Filtering, CVE-2026-4776.** [GHSA-fcmw-wx57-9p75](https://github.com/advisories/GHSA-fcmw-wx57-9p75). The advisory reports SQL injection in API contact filtering. The search record did not expose the exact filter expression or complete preconditions; use as a lead for query-filter parser review and consult the source before asserting reachability details.

**A15 — OpenEMR Patient REST API `_sort`.** [GHSA-rcc2-45v3-qmqm](https://github.com/openemr/openemr/security/advisories/GHSA-rcc2-45v3-qmqm). The advisory identifies authenticated API access and request `_sort` reaching a SQL sort path in `SearchConfigClauseBuilder.php`; it notes a column-name escape helper used elsewhere. **Review:** a helper's existence elsewhere does not prove this path invokes it; compare same-feature safe siblings and trace the specific caller.

**A16 — OpenEMR recall/reminder preferences.** [GHSA-6vx2-w9hw-prqj](https://github.com/openemr/openemr/security/advisories/GHSA-6vx2-w9hw-prqj). Maintainer report identifies SQL injection through unsanitized variables in recall/reminder processing and database-stored admin preferences (second-order). **Review:** persisted configuration may cross a privilege boundary; establish who can write settings and what scheduled/UI operation later consumes them.

**A17 — FreePBX CDR report ORDER BY.** [GHSA-p9fq-fmpw-2h9x](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-p9fq-fmpw-2h9x). The advisory explains that input interpolated into an unquoted ORDER BY context remained unsafe after `escapeSimple()` escaped single quotes. **Review:** string-literal escaping does not secure structural or unquoted SQL grammar positions.

**A18 — phpMyFAQ BuiltinCaptcha User-Agent.** [GHSA-289f-fq7w-6q2w](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-289f-fq7w-6q2w). The maintainer advisory describes unauthenticated remote SQL injection through the User-Agent header against the application's primary datastore. **Review:** headers are attacker-controlled sources too; include them in route/source tracing.

**A19 — PHP ext-pgsql `E'...'` escaping.** [GHSA-7qpv-r5mr-78m4](https://github.com/php/php-src/security/advisories/GHSA-7qpv-r5mr-78m4). PHP's PostgreSQL helper had an SQL injection issue involving a backslash breakout from `E'...'` string syntax; the fix changed generated parameter literals. **Review:** escaping rules depend on dialect modes and the precise string-literal syntax; prefer native binding over hand-built literals.

**A20 — PHP PDO Firebird NUL-byte quoting.** [GHSA-w476-322c-wpvm](https://github.com/php/php-src/security/advisories/GHSA-w476-322c-wpvm). The PHP core advisory identifies SQL injection involving NUL bytes in quoted strings in the Firebird PDO driver. **Review:** boundary/encoding characters can invalidate assumptions in quote-based defenses; verify specific driver behavior and use binding.

**A21 — Flight `SimplePdo` identifiers.** [GHSA-xwqr-rcqg-22mr](https://github.com/flightphp/core/security/advisories/GHSA-xwqr-rcqg-22mr). Unvalidated identifiers passed to `SimplePdo::insert`, `update` and `delete` were reported as injectable. The advisory describes a live reproduction on an in-memory SQLite setup. **Review:** helper APIs that accept column/table identifiers need an allowlist or correct dialect-aware identifier handling, distinct from value binding.

### JavaScript and TypeScript libraries / workflow systems

**A22 — Sequelize v6 JSON cast type, CVE-2026-30951.** [GHSA-6457-6jrx-69cr](https://github.com/advisories/GHSA-6457-6jrx-69cr). Sequelize v6 JSON path processing interpreted `::` in JSON keys as a cast type, then interpolated it into a SQL `CAST` expression. The advisory states v6 through 6.37.7 affected, v7 not affected. **Review:** keys and path metadata can become SQL structure; inspect dialect query-generator code and pinned package version.

**A23 — TypeORM `repository.save`/`update`, CVE-2025-60542.** [GHSA-q2pj-6v73-8rgj](https://github.com/advisories/GHSA-q2pj-6v73-8rgj). The reviewed advisory identifies a MySQL SQL injection in TypeORM before 0.3.26 involving crafted input and `sqlstring` behavior (`stringifyObjects` configuration). **Review:** normal ORM persistence APIs can be affected by serialization/configuration interactions; verify exact dependency configuration and version.

**A24 — Kysely JSON path keys, CVE-2026-33442.** [GHSA-fr9j-6mvq-frcv](https://github.com/advisories/GHSA-fr9j-6mvq-frcv). The reviewed advisory describes MySQL SQL injection through attacker-controlled keys passed to a non-type-safe JSON `.key()` path builder, involving a backslash-escape bypass. **Review:** type-safe APIs and non-type-safe escape hatches can have different guarantees; trace key data and connection escape behavior.

**A25 — Drizzle ORM identifier escaping, CVE-2026-39356.** [GHSA-gpj5-g38j-94v9](https://github.com/advisories/GHSA-gpj5-g38j-94v9). GitHub reviewed advisory identifies SQL injection through improperly escaped SQL identifiers. **Review:** identifiers are syntax; inspect all dialect-specific quoting implementations and dynamic identifier sources rather than value parameterization.

**A26 — `@payloadcms/drizzle` JSON/RichText queries, CVE-2026-25544.** [GHSA-xx6w-jxg9-2wh8](https://github.com/advisories/GHSA-xx6w-jxg9-2wh8). Advisory identifies SQL injection in JSON/RichText queries on PostgreSQL and SQLite adapters. The search excerpt did not establish the precise source-to-sink flow; consult full advisory and affected versions before applying it to a project. **Review:** adapter and query shape matter; compare database-specific query builders.

**A27 — Payload CMS query handling.** [GHSA-7xxh-373w-35vg](https://github.com/payloadcms/payload/security/advisories/GHSA-7xxh-373w-35vg). Maintainer advisory says certain request inputs were insufficiently validated and could influence SQL handling in collections; fixed in 3.79.1. **Review:** follow query operators and nested request objects into adapter execution; do not treat input validation as a replacement for safe query construction.

**A28 — n8n Data Table `orderByColumn`.** [GHSA-98c2-4cr3-4jc3](https://github.com/n8n-io/n8n/security/advisories/GHSA-98c2-4cr3-4jc3). An authenticated workflow author could influence a Data Table Get node ordering expression. The advisory distinguishes default SQLite limitations from PostgreSQL multi-statement impact. **Review:** workflow definitions are code-like inputs; model workflow editor privileges and configured DB backend.

**A29 — n8n Postgres v1/TimescaleDB nodes.** [GHSA-c37g-w77q-m4vp](https://github.com/n8n-io/n8n/security/advisories/GHSA-c37g-w77q-m4vp). Authenticated workflow authors could supply crafted parameters to affected nodes, with SQL executed using configured database credentials. **Review:** trace expressions and workflow-controlled fields through connector construction, and report impact bounded by credential privileges.

**A30 — n8n Microsoft SQL expression interpolation.** [GHSA-5qpp-pqww-h7fp](https://github.com/n8n-io/n8n/security/advisories/GHSA-5qpp-pqww-h7fp). A workflow using untrusted input in a Microsoft SQL node's query field can permit SQL execution against the connected database. **Review:** expression templating must not be conflated with query parameter binding; find whether dynamic fields are literal interpolation or values passed to bind APIs.

**A31 — n8n OracleDB vector-store metadata filter keys.** [GHSA-2x68-96jw-5r6c](https://github.com/n8n-io/n8n/security/advisories/GHSA-2x68-96jw-5r6c). The advisory says Vector Store OracleDB metadata filter keys were not validated and could reach SQL. **Review:** metadata keys are structural identifiers, even when metadata values are bound.

**A32 — n8n PostgresTrigger identifiers.** [GHSA-jqwr-vx3p-r266](https://github.com/n8n-io/n8n/security/advisories/GHSA-jqwr-vx3p-r266). The maintainer advisory says user-supplied channel, function and trigger names were interpolated into PostgreSQL statements without proper escaping; authenticated users could use connected credentials. **Review:** SQL identifier injection can appear in setup/DDL and trigger lifecycle code, not only SELECT paths.

**A33 — NocoBase workflow SQL template variables.** [GHSA-vx58-fwwq-5g8j](https://github.com/nocobase/nocobase/security/advisories/GHSA-vx58-fwwq-5g8j). Workflow template values were substituted into raw SQL and passed to Sequelize without parameterization; the advisory names affected releases through 2.0.8. **Review:** trace template processor output after substitution; a downstream raw-query API cannot infer which fragments were untrusted.

### Other languages, query protocols and database drivers

**A34 — JHipster generated WebFlux/R2DBC `sort`.** [GHSA-r223-96jv-q533](https://github.com/jhipster/generator-jhipster/security/advisories/GHSA-r223-96jv-q533). Generator versions 7.0.0–9.2.0 emitted reactive SQL list endpoints that concatenated the request `sort` parameter into ORDER BY. This is a generator/template flaw with generated-app impact, not a defect limited to the generator's own runtime. **Review:** inspect scaffolding templates and generated source as well as hand-written code; fix existing generated applications too.

**A35 — Spring AI MariaDB filter expression, CVE-2026-22730.** [GHSA-c267-rfvc-mvpm](https://github.com/advisories/GHSA-c267-rfvc-mvpm). Reviewed advisory identifies SQL injection in `MariaDBFilterExpressionConverter`. The search excerpt did not establish attacker source or versions; inspect the advisory before assigning application impact. **Review:** query translators and vector/database filters are SQL sinks even when the product feature is described as AI search.

**A36 — PostgreSQL JDBC line comment generation, CVE-2024-1597.** [GHSA-24rp-q3w6-vc56](https://github.com/advisories/GHSA-24rp-q3w6-vc56). Reviewed driver advisory reports SQL injection via generated line comments under affected driver/query conditions. **Review:** libraries that rewrite queries or attach comments may alter lexical boundaries; inspect exact driver API, version and query construction context.

**A37 — Navidrome URL parameters and ORM leakage.** [GHSA-58vj-cv5w-v4v6](https://github.com/navidrome/navidrome/security/advisories/GHSA-58vj-cv5w-v4v6). The advisory describes URL parameter names entering SQL LIKE query construction, unintended ORM field exposure, and wildcard behavior that could match password-like data. It covers multiple related weaknesses; the parameter-name injection and data exposure are separate findings. **Review:** inspect dynamic map keys and ORM serialization/field selection; distinguish SQLi from wildcard and data exposure issues.

**A38 — Navidrome artist `role` filter.** [GHSA-5wgp-vjxm-3x2r](https://github.com/navidrome/navidrome/security/advisories/GHSA-5wgp-vjxm-3x2r). Maintainer report for the `/api/artist` role filter, with SQLite-specific conditions in the report. **Relationship:** a later separate advisory, A39, documents a remaining sorting path after filter-side validation; these are related remediation paths, not proof of identical exploitability.

**A39 — Navidrome artist `role` in ORDER BY.** [GHSA-hm54-32q6-3rcr](https://github.com/navidrome/navidrome/security/advisories/GHSA-hm54-32q6-3rcr). Authenticated `/api/artist` callers could control `role` inside a sort mapping for song count, album count or size; affected versions are 0.55.0 through 0.63.x, fixed in 0.64.0. The advisory says the filter path was fixed earlier but this sort path remained unvalidated. **Review:** test the same field at every use site after partial remediation.

**A40 — Decidim admin similarity sorting, CVE-2026-45376.** [GHSA-jvqq-cvh4-xm37](https://github.com/advisories/GHSA-jvqq-cvh4-xm37). Search terms in an admin organization-user search reached raw SQL ORDER BY expressions before Rails sanitization. **Review:** transformation order matters; escaping applied after interpolation may act on a different representation or context.

**A41 — Fleet `order_key` and quoted identifiers.** [GHSA-49xw-vfc4-7p43](https://github.com/fleetdm/fleet/security/advisories/GHSA-49xw-vfc4-7p43). Authenticated software API users could escape identifier quoting in a MySQL ORDER BY path using a specially formed key and `goqu.I()`, yielding blind SQL expression behavior per the advisory. **Review:** identifier quote wrappers can have edge cases; inspect escaping rules and dialects, not just helper names.

**A42 — Ory Keto forged pagination token.** [GHSA-c38g-mx2c-9wf2](https://github.com/ory/keto/security/advisories/GHSA-c38g-mx2c-9wf2). Advisory identifies SQL injection through flaws in GetRelationships pagination. **Review:** encoded/opaque cursors may be attacker-controlled if unsigned or insufficiently validated; trace decoded token fields into LIMIT/OFFSET/filter SQL.

**A43 — Ory Kratos forged pagination token.** [GHSA-hgx2-28f8-6g2r](https://github.com/ory/kratos/security/advisories/GHSA-hgx2-28f8-6g2r). The ListCourierMessages admin API had SQL injection tied to pagination implementation. **Review:** same broad cursor pattern as A42 in a different product/API; do not merge as one incident, but reuse the token-to-query dataflow test.

**A44 — Parse Server PostgreSQL aggregate/distinct fields, CVE-2026-33539.** [GHSA-p2w6-rmh7-w8q3](https://github.com/advisories/GHSA-p2w6-rmh7-w8q3). Advisory reports SQL injection through aggregate and distinct field names in the PostgreSQL adapter. **Review:** query field names are structural, and adapter-specific operations can bypass otherwise safe value binding.

**A45 — Parse Server PostgreSQL dot-notation fields, CVE-2026-31871.** [GHSA-gqpp-xgvh-9h7h](https://github.com/advisories/GHSA-gqpp-xgvh-9h7h). A dot-notation sub-key in an `Increment` operation was reported to permit SQL injection in PostgreSQL; advisory points to additional `distinct` and `where` contexts. **Review:** nested key paths and update operators require field-name validation at their SQL translation boundary.

**A46 — CKAN `datastore_search_sql`, CVE-2026-42031.** [GHSA-h7j7-3rx6-xvcg](https://github.com/advisories/GHSA-h7j7-3rx6-xvcg). Advisory reports unauthenticated SQL injection combined with an authorization bypass in this datastore endpoint. **Review:** identify whether the endpoint intentionally accepts SQL and whether authorization controls are correctly applied; an SQL-capable API has a different security contract from a normal search filter.

**A47 — Metabase unauthenticated session-reset SQLi.** [GHSA-vwf4-m7j8-wcjf](https://github.com/metabase/metabase/security/advisories/GHSA-vwf4-m7j8-wcjf). The maintainer reported unauthenticated SQL injection into the application DB that could yield admin access and access to configured data sources; the advisory reported active exploitation. **Review:** chain SQL impact only through documented application-specific conditions; separately audit exposed reset endpoints and stored connector credentials.

**A48 — Chatwoot blind filter SQLi.** [GHSA-g8f9-hh83-rcq9](https://github.com/chatwoot/chatwoot/security/advisories/GHSA-g8f9-hh83-rcq9). Authenticated input in conversation/contact filters reached query construction and enabled blind SQL injection according to the advisory. **Review:** response differences need not display database errors; a source review should look for the unsafe query path without attempting time/boolean probes.

**A49 — Admidio stored list configuration.** [GHSA-3x67-4c2c-w45m](https://github.com/admidio/admidio/security/advisories/GHSA-3x67-4c2c-w45m). Authenticated list column names, sort directions and filter conditions were written with prepared statements to `adm_list_columns`, then later interpolated into generated SQL. **Review:** safe persistence is orthogonal to safe later use; trace each stored structural field to its consumer.

**A50 — Piwigo album sorting, second-order.** [GHSA-jhp4-7f82-8f6q](https://github.com/Piwigo/Piwigo/security/advisories/GHSA-jhp4-7f82-8f6q). Maintainer report describes a stored album sort-order value later used in SQL; an authenticated administrator was required per the advisory. It reports conditional data extraction/modification impact. **Review:** follow admin configuration writes into later sorting statements.

**A51 — ZoneMinder `getNearEvents()`, second-order.** [GHSA-r6gm-478g-f2c4](https://github.com/ZoneMinder/zoneminder/security/advisories/GHSA-r6gm-478g-f2c4). Stored event Name/Cause fields were later concatenated into a new SQL query in `getNearEvents()`. **Review:** ordinary business data can become query syntax in a later helper; trace record fields that are reused as query fragments.

**A52 — Zammad ticket overview sorting, second-order.** [GHSA-h5pm-rjvp-fr47](https://github.com/zammad/zammad/security/advisories/GHSA-h5pm-rjvp-fr47). Maintainer advisory identifies SQL injection when ticket overview sorting later consumes stored ordering configuration. The exact access and version conditions are in the source. **Review:** trace the setting write and the later overview query; include users who can edit saved views in the attacker model.

**A53 — DataEase group-field binning bounds, stored SQL.** [GHSA-gcr3-cj2q-gj4q](https://github.com/dataease/dataease/security/advisories/GHSA-gcr3-cj2q-gj4q). Advisory says values saved as chart grouping/binning bounds were later spliced unescaped into generated SQL when a chart rendered. **Review:** chart/dashboard configuration and visualization rendering create a persistence-to-query flow.

**A54 — Evershop URL rewrite from category URL key, second-order.** [GHSA-3h84-9rhc-j2ch](https://github.com/evershopcommerce/evershop/security/advisories/GHSA-3h84-9rhc-j2ch). Maintainer report ties stored category URL keys to later path/request-path values used in query construction. **Review:** trace slug/URL configuration into rewrite lookup queries; escaping for URL contexts does not imply SQL safety.

## Related published reports to use with care

These additional reports are useful pattern references but overlap an existing case or are close enough that incident counts should not add them blindly:

- [Shlink tag-statistics ORDER BY, CVE-2026-18737](https://github.com/advisories/GHSA-2jhc-j623-f52p): blind SQLi through an unvalidated direction string in a Doctrine QueryBuilder; conceptually overlaps structural ordering cases and the existing Doctrine material.
- [Navidrome later artist-role sorting](https://github.com/navidrome/navidrome/security/advisories/GHSA-hm54-32q6-3rcr) is separately catalogued as A39 but related to A38's earlier filter fix; count as a separate vulnerable path, not an unrelated product.
- [WordPress REST batch route and SQLi chain](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-ff9f-jf42-662q) is a chain involving existing case P02, not another standalone SQL injection.
- Cacti search returned another advisory described as the same tree-rule issue as A12; it is not counted as a distinct incident here.

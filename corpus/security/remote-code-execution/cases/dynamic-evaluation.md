# dynamic evaluation

### CVE-2025-55346 — Flowise custom MCP dynamic Function constructor

**Family:** Dynamic JavaScript evaluation
**Product / versions:** Flowise <= 2.2.7-patch.1; no patched version listed in the advisory at consultation
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2025-55346 advisory](https://github.com/advisories/GHSA-hmgh-466j-fx4c)
**Published:** 2025-10-03
**Consulted:** 2026-11-03
**Remote input / path to execution:** A string-valued MCP configuration reaches a dynamic Function constructor while Flowise loads custom MCP actions through the node-load-method endpoint.
**Preconditions:** The endpoint and custom MCP loader must be reachable; the advisory does not establish a universal authentication state for every deployment.
**Impact reported:** JavaScript executes in the unsandboxed host process and can reach server capabilities.
**Fix:** No fixed package version was listed in the advisory as of consultation; disable or restrict the custom MCP loading path and verify an upstream release before re-enabling it.
**Evidence limits:** The advisory concerns server-side JavaScript evaluation, not browser-side script execution.

### CVE-2024-21534 — JSONPath Plus unsafe expression evaluation

**Family:** Dynamic JavaScript evaluation through vm
**Product / versions:** jsonpath-plus metadata lists versions < 10.2.0 as affected and 10.2.0 as fixed; advisory prose identifies earlier vulnerable versions before 10.0.7
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2024-21534 advisory](https://github.com/advisories/GHSA-pppg-cpfq-h7wr)
**Published:** 2024-10-11
**Consulted:** 2026-11-03
**Remote input / path to execution:** An application-supplied JSONPath expression reaches the library's unsafe evaluation mode using Node vm behavior.
**Preconditions:** A server application must forward attacker-controlled expressions to the vulnerable library configuration; the library advisory alone does not prove a particular HTTP route.
**Impact reported:** Arbitrary code execution in the host process when the unsafe evaluation mode is reachable.
**Fix:** Upgrade to 10.2.0 or later and disable unsafe expression evaluation for untrusted queries.
**Evidence limits:** The advisory contains a mismatch between the package-range metadata and prose about the earliest affected release; confirm the exact lockfile version and mode.

### CVE-2025-68613 — n8n workflow expression isolation failure

**Family:** Workflow expression evaluation
**Product / versions:** n8n >= 0.211.0 < 1.120.4 and >= 1.121.0 < 1.121.1 in advisory metadata; body also recommends >= 1.122.0
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2025-68613 advisory](https://github.com/advisories/GHSA-v98v-ff95-f3cp)
**Published:** 2025-12-19
**Consulted:** 2026-11-03
**Remote input / path to execution:** Expression text saved during workflow configuration is evaluated in a context insufficiently isolated from the n8n runtime.
**Preconditions:** An authenticated user needs workflow configuration privileges and must reach the affected expression path.
**Impact reported:** Code execution with n8n process privileges, potentially exposing workflow data and operations.
**Fix:** The advisory metadata lists 1.120.4 and 1.121.1, while the narrative recommends 1.122.0 or later; verify vendor release notes and use a version explicitly confirmed fixed.
**Evidence limits:** The advisory leaves the phrase under certain conditions broad; do not report this solely because a project has an expression field.

### CVE-2024-5565 — Vanna prompt-driven visualization evaluation

**Family:** Prompt-to-code execution
**Product / versions:** Vanna <= 0.5.5; no patched version listed in the advisory at consultation
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2024-5565 advisory](https://github.com/advisories/GHSA-7735-w2jp-gvg6)
**Published:** 2024-05-31
**Consulted:** 2026-11-03
**Remote input / path to execution:** External input to the ask method can affect generated visualization code, which the library executes as Python when visualize is true.
**Preconditions:** The application must call ask with externally influenced input and retain the default visualization behavior; deployment exposure and authentication depend on the wrapper application.
**Impact reported:** Python code execution in the process hosting Vanna.
**Fix:** No fixed package version is listed in the advisory; disable unsafe visualization execution or isolate it behind a reviewed non-executable representation.
**Evidence limits:** The advisory describes a library call; a remote RCE finding requires tracing a remote request into this call.

### CVE-2026-54569 — SENAITE JSON API eval and authorization chain

**Family:** Python eval injection
**Product / versions:** senaite.core >= 2.0.0 <= 2.6.0; no patched version listed in the advisory at consultation
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-54569 advisory](https://github.com/advisories/GHSA-jrw6-7x4q-w25j)
**Published:** 2026-07-10
**Consulted:** 2026-11-03
**Remote input / path to execution:** An anonymous JSON API update route resolves an object and evaluates raw RecordsField or RecordField request strings before the write-permission check.
**Preconditions:** The @@API update route is exposed and anonymous-readable stock objects can be reached; the documented chain uses two requests. The same eval sink is separately reachable to authenticated users with field write permission.
**Impact reported:** Python code execution in the Zope worker process.
**Fix:** No patched version was listed as of consultation; add the missing API permission gate and replace eval with a typed data parser, while fixing the sink path as well.
**Evidence limits:** The advisory identifies two independent defects; fixing only authorization breaks the anonymous chain but leaves an authenticated eval path.

### CVE-2026-61539 — Xinference Llama 3 tool-call parser

**Family:** Unsafe Python eval on model output
**Product / versions:** Xinference <= 2.5.0; fixed 2.7.0
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-61539 advisory](https://github.com/advisories/GHSA-x2rj-828p-hx9m)
**Published:** 2026-07-13
**Consulted:** 2026-11-03
**Remote input / path to execution:** A model response to chat input is parsed with Python eval when the request includes tool calls; the model output is attacker-influenced through prompts.
**Preconditions:** The Transformers backend and Llama 3 parser path must be used. In the reported default deployment authentication was disabled; authenticated deployments still require endpoint access.
**Impact reported:** Arbitrary Python expression execution with Xinference process privileges.
**Fix:** Upgrade to 2.7.0 or later and parse a data format with a non-executable parser.
**Evidence limits:** Prompt influence is an input-control path, but severity still depends on model, backend, request parameters and authentication.

### CVE-2025-0868 — DocsGPT remote endpoint JSON eval

**Family:** Python eval used as a JSON parser
**Product / versions:** DocsGPT >= 0.8.1 <= 0.12.0; no patched version listed in the advisory at consultation
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2025-0868 advisory](https://github.com/advisories/GHSA-9gff-5v8w-x922)
**Published:** 2025-02-20
**Consulted:** 2026-11-03
**Remote input / path to execution:** The /api/remote endpoint parses attacker-supplied JSON-like data using eval, so Python code is interpreted instead of data.
**Preconditions:** The endpoint must be network reachable; the advisory describes exploitation without authentication.
**Impact reported:** Arbitrary Python code execution in the DocsGPT server process.
**Fix:** No patched release is listed in the advisory as of consultation; use a strict JSON parser and restrict or disable the affected endpoint until a fixed release is verified.
**Evidence limits:** The source gives affected versions and endpoint but no detailed release remediation; confirm project status before recommending an upgrade number.

### CVE-2017-9841 — Exposed PHPUnit eval-stdin utility

**Family:** Remote PHP code evaluation through a development utility
**Product / versions:** PHPUnit >= 4.8.19 < 4.8.28 and >= 5.0.10 < 5.6.3; fixed in 4.8.28 and 5.6.3
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2017-9841 advisory](https://github.com/advisories/GHSA-r7c9-c69m-rph8)
**Published:** 2022-03-26
**Consulted:** 2026-11-03
**Remote input / path to execution:** HTTP POST data reaches the eval-stdin.php utility shipped in PHPUnit.
**Preconditions:** The application must expose the vendor PHPUnit utility path to the web server; a normal installation that does not publish the vendor path is not affected by this remote route.
**Impact reported:** Arbitrary PHP code execution under the web process identity.
**Fix:** Upgrade to a fixed PHPUnit release and ensure development dependencies and vendor utility files are not web-accessible.
**Evidence limits:** This is an old package advisory; current dependency or web-root layout may differ. Do not infer reachability from PHPUnit being present alone.

### CVE-2022-26134 — Confluence OGNL expression injection

**Family:** Server-side expression evaluation
**Product / versions:** Confluence Server and Data Center versions after 1.3.0 before the fixed releases 7.4.17, 7.13.7, 7.14.3, 7.15.2, 7.16.4, 7.17.4 or 7.18.1
**Source status:** Vendor advisory
**Source:** [CVE-2022-26134 advisory](https://confluence.atlassian.com/doc/confluence-security-advisory-2022-06-02-1130377146.html)
**Published:** 2022-06-02
**Consulted:** 2026-11-03
**Remote input / path to execution:** A request-controlled OGNL expression reaches Confluence expression evaluation and permits arbitrary code execution.
**Preconditions:** Unauthenticated network access to an affected self-managed Confluence Server or Data Center instance; Atlassian Cloud-hosted sites were stated not affected.
**Impact reported:** Arbitrary code execution on the Confluence host.
**Fix:** Upgrade to one of the fixed releases or a later supported release.
**Evidence limits:** The vendor described active exploitation and later clarified the affected release range; use the advisory's server-versus-cloud distinction.


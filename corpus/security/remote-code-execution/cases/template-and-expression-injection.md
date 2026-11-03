# template and expression injection

### GHSA-7pwj-xvc2-hfpc — MockServer response template execution

**Family:** Template engine class loading and command execution
**Product / versions:** mockserver-core <= 7.4.0; fixed 7.5.0
**Source status:** Maintainer advisory on GitHub
**Source:** [GHSA-7pwj-xvc2-hfpc advisory](https://github.com/mock-server/mockserver-monorepo/security/advisories/GHSA-7pwj-xvc2-hfpc)
**Published:** 2026-07-30
**Consulted:** 2026-11-03
**Remote input / path to execution:** An expectation registered through the management API supplies a Velocity or JavaScript response template; the template engine can load host classes and execute commands.
**Preconditions:** The management API must be reachable by the attacker. Velocity is shipped in every distribution with class loading enabled by default; the GraalJS engine is limited to the GraalJS variant or manually added dependencies.
**Impact reported:** Code execution in the MockServer process with that deployment's privileges.
**Fix:** Upgrade to 7.5.0 or later and restrict template capabilities and management API reachability.
**Evidence limits:** The maintainer corrected the original report: Velocity affects every distribution; GraalJS is optional. Do not assume all template engines are installed.

### GHSA-w28w-gp39-m4p6 — Prompty Nunjucks template evaluation

**Family:** Server-side template injection
**Product / versions:** @prompty/core <= 0.1.4 and <= 2.0.0-beta.4; fixed in 0.1.5 and 2.0.0-beta.5
**Source status:** Maintainer advisory on GitHub
**Source:** [GHSA-w28w-gp39-m4p6 advisory](https://github.com/microsoft/prompty/security/advisories/GHSA-w28w-gp39-m4p6)
**Published:** 2026-07-20
**Consulted:** 2026-11-03
**Remote input / path to execution:** An untrusted .prompty template body is rendered by the TypeScript Nunjucks renderer with unrestricted JavaScript member access.
**Preconditions:** An application must render untrusted, community-supplied, cloned or generated template files using the TypeScript runtime.
**Impact reported:** Arbitrary JavaScript execution with the Node.js host privileges.
**Fix:** Upgrade to 0.1.5 or 2.0.0-beta.5 or later; restrict inputs to own-data values and reject dangerous member traversal and function calls.
**Evidence limits:** The package API is vulnerable when the caller accepts untrusted template source; trusted static templates are a different trust model.

### GHSA-vwf3-4xxj-qg6h — MCP Context Forge prompt template rendering

**Family:** Unsandboxed Jinja2 server-side template injection
**Product / versions:** mcp-contextforge-gateway < 1.0.0; fixed 1.0.0
**Source status:** GitHub Reviewed advisory
**Source:** [GHSA-vwf3-4xxj-qg6h advisory](https://github.com/advisories/GHSA-vwf3-4xxj-qg6h)
**Published:** 2026-06-15
**Consulted:** 2026-11-03
**Remote input / path to execution:** PromptService renders stored user prompt-template text through plain Jinja2 Environment and then returns rendered output; the same code has a formatting fallback.
**Preconditions:** An authenticated user with permission to register or update prompt templates must be able to cause a later prompt render.
**Impact reported:** Python code execution with gateway process privileges.
**Fix:** Upgrade to 1.0.0 or later and use a constrained template environment; remove unsafe fallbacks that reinterpret source.
**Evidence limits:** The advisory verifies version 0.9.0 and infers earlier published releases from the main-branch fix; verify exact release provenance.

### CVE-2024-28116 — Grav Twig sandbox bypass

**Family:** Twig sandbox bypass leading to server-side execution
**Product / versions:** Grav <= 1.7.44; fixed 1.7.45
**Source status:** Maintainer advisory on GitHub
**Source:** [CVE-2024-28116 advisory](https://github.com/getgrav/grav/security/advisories/GHSA-c9gp-64c4-2rrh)
**Published:** 2024-03-21
**Consulted:** 2026-11-03
**Remote input / path to execution:** Twig template expressions can reach unsafe PHP callbacks through a custom sandbox that blocks a blacklist of dangerous function names.
**Preconditions:** An authenticated user with editor permission is sufficient; the template features and relevant Grav configuration must be enabled.
**Impact reported:** Arbitrary code execution on the Grav server.
**Fix:** Upgrade to 1.7.45 or later and replace blacklist-based exposure with a narrow allowlist and safe template capability model.
**Evidence limits:** The advisory describes sandbox bypass behavior; verify installed plugins and Twig configuration before transferring the exact path.

### CVE-2025-66294 — Grav later Twig sandbox validation bypass

**Family:** Twig template sanitizer bypass
**Product / versions:** Grav < 1.8.0-beta.27; fixed in 1.8.0-beta.27
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2025-66294 advisory](https://github.com/advisories/GHSA-662m-56v4-3r8f)
**Published:** 2025-12-01
**Consulted:** 2026-11-03
**Remote input / path to execution:** Weak regular-expression validation in cleanDangerousTwig allows attacker-controlled template syntax to survive sanitization and execute during processString or form rendering.
**Preconditions:** The primary path requires an authenticated editor and the official Form and Admin plugins. The advisory's guest path requires a pre-existing public form that passes submitted input to evaluation; the report also discusses a separate access-control weakness for editing process settings.
**Impact reported:** Arbitrary command execution in the Grav server context.
**Fix:** Upgrade to the fixed beta or a later stable release and avoid treating regex cleanup as a template sandbox.
**Evidence limits:** This is a later product-specific bypass, not the same report as the 2024 Grav issue; guest reachability depends on the form configuration and a separate condition.

### CVE-2024-45053 — Fides Jinja email templates

**Family:** Unsandboxed Jinja2 template execution
**Product / versions:** ethyca-fides >= 2.19.0 < 2.44.0; fixed 2.44.0
**Source status:** Maintainer advisory on GitHub
**Source:** [CVE-2024-45053 advisory](https://github.com/ethyca/fides/security/advisories/GHSA-c34r-238x-f7qx)
**Published:** 2024-09-04
**Consulted:** 2026-11-03
**Remote input / path to execution:** A message template saved through the Admin UI or messaging-template API is rendered by unrestricted Jinja2 when a privacy-request email is composed.
**Preconditions:** Default Owner or Contributor roles can modify templates; OAuth clients with messaging-template:update may also use the API. A later message render is required.
**Impact reported:** Python code execution in the Fides webserver container.
**Fix:** Upgrade to 2.44.0 or later and restrict template editing to trusted authors using a safe rendering environment.
**Evidence limits:** The advisory identifies a delayed execution trigger: saving a template is separate from the later email render.

### GHSA-5f29-2333-h9c7 — OpenMetadata FreeMarker email templates

**Family:** FreeMarker server-side template injection
**Product / versions:** OpenMetadata <= 1.11.3; fixed 1.11.4
**Source status:** Maintainer advisory on GitHub
**Source:** [GHSA-5f29-2333-h9c7 advisory](https://github.com/open-metadata/OpenMetadata/security/advisories/GHSA-5f29-2333-h9c7)
**Published:** 2026-01-07
**Consulted:** 2026-11-03
**Remote input / path to execution:** EmailTemplate content stored in the document store is passed directly to a new FreeMarker Template with a default Configuration and is evaluated when an email is rendered.
**Preconditions:** An account able to modify the email template through the documented API is required; a later email event must invoke the rendering path.
**Impact reported:** Arbitrary server-side code execution and file operations under the OpenMetadata process account.
**Fix:** Upgrade to 1.11.4 or later and configure FreeMarker with a restrictive class resolver and API access disabled.
**Evidence limits:** The advisory includes proof-of-concept material that is intentionally omitted here; assess the actual template-editing authorization.

### GHSA-cfr2-mp74-3763 — Agenta evaluator Jinja2 template

**Family:** Unsandboxed Jinja2 evaluation in API workflow
**Product / versions:** agenta-api <= 0.86.7; fixed 0.86.8
**Source status:** Maintainer advisory on GitHub
**Source:** [GHSA-cfr2-mp74-3763 advisory](https://github.com/Agenta-AI/agenta/security/advisories/GHSA-cfr2-mp74-3763)
**Published:** 2026-02-25
**Consulted:** 2026-11-03
**Remote input / path to execution:** An evaluator template is created from supplied content and rendered with Jinja2 Template(content).render without a sandbox in the server API process.
**Preconditions:** An authenticated user must configure an evaluator with template_format set to jinja2 and trigger that evaluator in a self-hosted or managed Agenta deployment.
**Impact reported:** Arbitrary Python execution in the API server process.
**Fix:** Upgrade to 0.86.8 or later and render untrusted input only as data through a constrained environment.
**Evidence limits:** Standalone SDK use is not the affected deployment described by the advisory; the vulnerable code executes in the platform API.

### GHSA-8wxj-vghp-jpcq — OpenBoxes Zebra label templates

**Family:** Groovy expression evaluation in document rendering
**Product / versions:** OpenBoxes before v0.9.8; fixed v0.9.8
**Source status:** Maintainer advisory on GitHub
**Source:** [GHSA-8wxj-vghp-jpcq advisory](https://github.com/OpenBoxes/OpenBoxes/security/advisories/GHSA-8wxj-vghp-jpcq)
**Published:** 2026-07-07
**Consulted:** 2026-11-03
**Remote input / path to execution:** A document selected by ID is passed to GroovyPagesTemplateEngine for Zebra rendering without verifying the document type; expressions execute as Groovy code.
**Preconditions:** A Manager-level user can upload a document; any authenticated user with Browser role can trigger rendering by document ID.
**Impact reported:** Remote code execution on the server, potentially triggered by a less-privileged user than the uploader.
**Fix:** Upgrade to v0.9.8; validate document type and replace the general Groovy engine with a restricted property resolver.
**Evidence limits:** The advisory documents a two-role chain: uploader and renderer can be different users.

### CVE-2026-28695 — Craft CMS Twig create function and Symfony Process

**Family:** Twig template plus object-instantiation gadget chain
**Product / versions:** Craft CMS >= 5.8.7 < 5.9.0-beta.1 and >= 4.0.0-RC1 < 4.17.0-beta.1; fixed in those beta releases
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-28695 advisory](https://github.com/advisories/GHSA-94rc-cqvm-m4pw)
**Published:** 2026-03-02
**Consulted:** 2026-11-03
**Remote input / path to execution:** The create Twig function exposes arbitrary object construction; a template author can instantiate the bundled Symfony Process class and invoke it during entry-title rendering.
**Preconditions:** Administrator privileges or access to the System Messages utility is required; production allowAdminChanges is one documented configuration enabling the settings route.
**Impact reported:** Command execution with web server privileges.
**Fix:** Upgrade to the patched 5.9.0-beta.1 or 4.17.0-beta.1 line or later; restrict or remove the create function for templates.
**Evidence limits:** The advisory identifies this as a bypass of a previous Twig-related fix in 5.8.7; keep the later issue distinct and do not infer an anonymous path.

### CVE-2026-28697 — Craft CMS Twig filesystem write chain

**Family:** Twig template execution followed by PHP file execution
**Product / versions:** Craft CMS >= 5.0.0-RC1 < 5.9.0-beta.1 and >= 4.0.0-RC1 < 4.17.0-beta.1; fixed in those beta releases
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-28697 advisory](https://github.com/advisories/GHSA-v47q-jxvr-p68x)
**Published:** 2026-03-02
**Consulted:** 2026-11-03
**Remote input / path to execution:** A Twig template can reach craft.app filesystem APIs, write a PHP file into a web-accessible directory, then the web server loads that file on a later request.
**Preconditions:** An authenticated administrator with allowAdminChanges enabled or access to the System Messages utility is required; a filesystem or volume handle must expose a writable web-served path.
**Impact reported:** The template render provides a write primitive; later access to the written PHP file yields command execution as the web process.
**Fix:** Upgrade to the patched Craft line or later and remove filesystem write capability from attacker-editable Twig templates.
**Evidence limits:** Execution is a two-stage chain; the filesystem handle, web-root mapping and process permissions affect reachability.

### CVE-2023-46245 — Kimai uploaded Twig file during invoice rendering

**Family:** Twig source injection through upload and PDF rendering
**Product / versions:** Kimai < 2.1.0; fixed 2.1.0
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2023-46245 advisory](https://github.com/advisories/GHSA-fjhg-96cp-6fcw)
**Published:** 2023-10-27
**Consulted:** 2026-11-03
**Remote input / path to execution:** A malicious Twig file uploaded into a rendering path is used as template source during invoice or PDF/HTML rendering.
**Preconditions:** An authenticated account able to upload or influence the Twig file and a later invoice render are required; exact role details are not stated in the advisory.
**Impact reported:** Server-side code execution in the Kimai process.
**Fix:** Upgrade to 2.1.0 or later and ensure uploaded content is never passed as trusted template source.
**Evidence limits:** The advisory describes an uploaded template path; confirm that the reviewed application exposes the same upload and render permissions.

### CVE-2024-45747 — GeoServer FreeMarker output templates

**Family:** FreeMarker template sandbox bypass
**Product / versions:** GeoServer packages < 2.27.0; fixed 2.27.0
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2024-45747 advisory](https://github.com/advisories/GHSA-wf6j-gr27-g7ch)
**Published:** 2026-06-11
**Consulted:** 2026-11-03
**Remote input / path to execution:** An uploaded FreeMarker template is evaluated for WMS GetFeatureInfo HTML/JSON or GetMap KML/GeoRSS output; a denylist on class resolution can be bypassed through method chaining.
**Preconditions:** An authenticated administrator can upload templates; these formats are present in a plain GeoServer without extensions.
**Impact reported:** Arbitrary operating-system command execution and server file read/write under GeoServer privileges.
**Fix:** Upgrade to 2.27.0 or later and configure object allow/block lists and API exposure restrictions.
**Evidence limits:** The advisory notes an administrator requirement; this is a privileged RCE path, not unauthenticated template injection.

### CVE-2024-2952 — LiteLLM completion endpoint tokenizer template

**Family:** Jinja template injection from model metadata
**Product / versions:** LiteLLM < 1.34.42; fixed 1.34.42
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2024-2952 advisory](https://github.com/advisories/GHSA-46cm-pfwv-cgf8)
**Published:** 2024-04-10
**Consulted:** 2026-11-03
**Remote input / path to execution:** The hf_chat_template method processes chat_template content from tokenizer_config.json with Jinja without sufficient restriction, reachable through the completions path.
**Preconditions:** The application must accept or select model metadata controlled by an attacker and invoke the affected endpoint; API authentication depends on deployment configuration.
**Impact reported:** Arbitrary code execution in the LiteLLM server process.
**Fix:** Upgrade to 1.34.42 or later and treat tokenizer configuration as executable template source unless parsed in a restricted environment.
**Evidence limits:** The advisory describes attacker-crafted model metadata; it does not establish that every ordinary completion request supplies attacker-controlled template content.


# Server-side template and expression injection

## Distinguish source from rendered data

Identify whether remote input is:

- **Template source:** parsed/compiled as a template or expression; this is the core candidate for server-side template injection.
- **Template data:** inserted into a fixed trusted template using the engine's normal data binding; this is not SSTI by itself.
- **A delayed source:** stored as a template/configuration and rendered by a later email, report, export, webhook, workflow or worker.

Trace the authoring permission separately from the rendering trigger. A low-privilege renderer may consume source saved by a different user, and a publicly reachable render route can change the exposure. HTML auto-escaping protects output contexts; it is not a server-side template sandbox. See [OS-03](offline-sources.md#os-03), [OS-11–OS-12](offline-sources.md#os-11), and [template patterns](case-patterns.md#template-and-expression-injection).

## Inspect the execution surface

Record engine and version, sandbox enabled state, sandbox policy, loader selection, included/imported templates, custom functions/filters/tags, available objects, property/method access, global variables and fallback paths. Check framework-specific wrappers: they can recompile rendered output or bypass a configured environment. Regex blacklists and checks of a few dangerous names are not equivalent to an allowlisted capability policy.

For Twig, the current 3.x docs describe a dedicated sandbox for untrusted authors and a strict policy; APIs differ by release. For Jinja, review `SandboxedEnvironment`, its restrictions, and objects/functions supplied by the application. Neither engine name alone proves a secure sandbox.

## Candidate threshold

The attacker can supply template/expression source which is later evaluated in a server context. Identify what capability makes the evaluation an RCE (e.g. class loading, host method access, process invocation, arbitrary code evaluation) and under which role/configuration it is reachable. Template rendering that only evaluates trusted source with remote values as data is a negative case.

## Controls

- Keep source in trusted, reviewed files and pass user-controlled values only as data.
- If user-defined templates are a feature, render them in a dedicated sandbox environment with an explicit allowlist and minimal plain-data context.
- Remove unneeded extension functions and object capabilities; verify included templates cannot switch contexts.
- Test framework wrappers by reading their code/version and trace every fallback; do not infer runtime behavior from a configuration flag name.
- Keep rendering identity and side effects constrained; no ambient credentials or unrestricted process APIs should be available to the rendering service.

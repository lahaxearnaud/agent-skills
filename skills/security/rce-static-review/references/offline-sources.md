# Offline source notes

This file contains attributed paraphrases for ordinary offline use of the installed skill; it is not a mirror of upstream documentation. Read these notes first. If online, consult an exact primary source only when a material version, runtime, configuration, or impact detail is missing here and in the reviewed repository. This is optional. If unavailable, state the uncertainty. Never send private code externally. Sources were consulted **2026-11-03**; versions are identified as stated by the source and must be matched to the reviewed project.

## Injection and weakness taxonomies

<a id="os-01"></a>
### OS-01 — OWASP Injection Prevention Cheat Sheet

- **Source/version:** OWASP Cheat Sheet Series, current web edition; [original](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html).
- **Guidance:** Injection occurs when untrusted data reaches an interpreter. Prefer a structured API that keeps code and data separate; otherwise use correct context-specific validation/escaping. It treats OS command injection and argument injection as distinct categories.
- **Conditions/limits:** A generic sanitizer is not universal across interpreters. Application reachability and actual API semantics remain code-review questions.

<a id="os-02"></a>
### OS-02 — OWASP OS Command Injection Defense Cheat Sheet

- **Source/version:** OWASP Cheat Sheet Series, current web edition; [original](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html).
- **Guidance:** Command injection changes the meaning of a command constructed from external input. Prefer APIs with structured parameters and avoid shells. Least privilege reduces damage if execution occurs.
- **Conditions/limits:** Structured arguments still need review for argument/option semantics in the child. Least privilege limits impact; it does not repair tainted executable behavior.

<a id="os-03"></a>
### OS-03 — OWASP Server-Side Template Injection Prevention

- **Source/version:** OWASP Cheat Sheet Series, current web edition; [original](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Template_Injection_Prevention_Cheat_Sheet.html).
- **Guidance:** Review whether user data is placed into template source or passed as data to a trusted template. Treat user-authored template source as executable input and use a constrained rendering model.
- **Conditions/limits:** HTML escaping is an output-context control and does not define server-side template sandbox capabilities. Engine extensions and application objects require separate review.

<a id="os-14"></a>
### OS-14 — CWE-78, OS command injection

- **Source/version:** MITRE CWE online definition; [original](https://cwe.mitre.org/data/definitions/78.html).
- **Guidance:** Improper neutralization of command syntax can let an attacker execute unauthorized commands, read/modify data, or affect service availability.
- **Conditions/limits:** CWE is a weakness taxonomy. It does not prove that a particular process call uses a shell or is remotely reachable.

<a id="os-15"></a>
### OS-15 — CWE-88, argument injection/modification

- **Source/version:** MITRE CWE online definition; [original](https://cwe.mitre.org/data/definitions/88.html).
- **Guidance:** A program may receive attacker-controlled arguments that change its behavior even without shell parsing.
- **Conditions/limits:** Determine the target application's own option and secondary-language semantics; do not equate this with shell metacharacter injection.

<a id="os-16"></a>
### OS-16 — CWE-94, code injection

- **Source/version:** MITRE CWE online definition; [original](https://cwe.mitre.org/data/definitions/94.html).
- **Guidance:** Improperly controlled generation or interpretation of code can let data alter executable logic.
- **Conditions/limits:** The API name alone is insufficient; show attacker control over evaluated code and a reachable execution context.

<a id="os-17"></a>
### OS-17 — CWE-502, deserialization of untrusted data

- **Source/version:** MITRE CWE online definition; [original](https://cwe.mitre.org/data/definitions/502.html).
- **Guidance:** Reconstructing objects from untrusted input can invoke behavior or produce unsafe states; exact impact depends on language and types.
- **Conditions/limits:** It is not automatically RCE. Establish input control, object behavior/gadget, runtime class set and application reachability.

## Process APIs

<a id="os-04"></a>
### OS-04 — Python `subprocess`

- **Source/version:** Python 3.15 library documentation; [original](https://docs.python.org/3/library/subprocess.html).
- **Guidance:** The library does not implicitly choose a system shell; with explicit `shell=True`, quoting is the application's responsibility. The docs note platform-specific batch-file parsing on Windows.
- **Conditions/limits:** Exact Python version, `shell` option, executable, platform, batch-file behavior and child-program argument parsing matter.

<a id="os-05"></a>
### OS-05 — Node.js `child_process`

- **Source/version:** Node.js v26 API documentation; [original](https://nodejs.org/api/child_process.html).
- **Guidance:** Child-process functions have different shell behavior. The API documentation warns against passing unsanitized user input when a shell is enabled.
- **Conditions/limits:** Review the exact function/options and Node version; argv separation cannot prevent a child program's option or script semantics.

<a id="os-06"></a>
### OS-06 — Symfony Process

- **Source/version:** Symfony Process component current documentation; [original](https://symfony.com/doc/current/components/process.html).
- **Guidance:** Prefer an array of command/argument values; `fromShellCommandline()` is for shell features and makes platform-specific escaping the caller's responsibility.
- **Conditions/limits:** Confirm installed component version and whether the application selects the shell factory or string API. Array arguments do not neutralize target-program options.

<a id="os-07"></a>
### OS-07 — Java `ProcessBuilder`

- **Source/version:** Java SE 26 API documentation; [original](https://docs.oracle.com/en/java/javase/26/docs/api/java.base/java/lang/ProcessBuilder.html).
- **Guidance:** The builder starts the program and arguments represented in its command list and carries a separately configurable working directory and environment.
- **Conditions/limits:** It is not a shell by itself, though a shell or wrapper may be the selected executable. Check executable path, arguments, environment, directory and child semantics.

## Interpreters, templates, and object formats

<a id="os-13"></a>
### OS-13 — Node.js `vm`

- **Source/version:** Node.js v26 documentation; [original](https://nodejs.org/api/vm.html).
- **Guidance:** The documentation explicitly says `node:vm` is not a security mechanism and must not be used to run untrusted code.
- **Conditions/limits:** A separate V8 context/global is not an isolation boundary. Review the host process and available capabilities.

<a id="os-11"></a>
### OS-11 — Twig sandbox

- **Source/version:** Twig 3.x documentation; dedicated `Sandbox` API introduced in Twig 3.29; [original](https://twig.symfony.com/doc/3.x/sandbox.html).
- **Guidance:** Untrusted template authors require a dedicated sandbox environment and explicit allowed tags, filters, methods, properties, functions and tests. Current docs describe a strict policy.
- **Conditions/limits:** Version-specific API changes matter. Review the exact environment, policy, registered extensions and objects; trusted application templates should not be indiscriminately put into the same sandbox.

<a id="os-12"></a>
### OS-12 — Jinja sandbox

- **Source/version:** Jinja 3.1.x documentation; [original](https://jinja.palletsprojects.com/en/stable/sandbox/).
- **Guidance:** Jinja exposes a sandboxed environment with customization of attribute access and callable behavior for untrusted templates.
- **Conditions/limits:** Inspect supplied objects, filters, globals, operators, resource limits and the deployed version. A sandbox is not proof of safety for an application-specific object model.

<a id="os-08"></a>
### OS-08 — PHP `unserialize`

- **Source/version:** PHP manual, current documentation; [original](https://www.php.net/manual/en/function.unserialize.php).
- **Guidance:** Do not pass untrusted input even when `allowed_classes` is set. Object reconstruction and autoloading can load or execute code; JSON is recommended for data interchange.
- **Conditions/limits:** Verify the call, PHP version, autoloader, object hooks and remote input. Integrity checks help only when the key and signing path are trusted.

<a id="os-09"></a>
### OS-09 — Java `ObjectInputFilter`

- **Source/version:** Java SE 26 API documentation; [original](https://docs.oracle.com/en/java/javase/26/docs/api/java.base/java/io/ObjectInputFilter.html).
- **Guidance:** A filter can constrain classes and object-graph/resource metrics during deserialization. Oracle warns that untrusted deserialization is inherently dangerous and calls for context-appropriate filters.
- **Conditions/limits:** Filtering does not occur unless configured. Confirm the specific stream receives an effective allowlist and limits; check composition/factory behavior.

<a id="os-10"></a>
### OS-10 — Python `pickle`

- **Source/version:** Python 3.15 library documentation; [original](https://docs.python.org/3/library/pickle.html).
- **Guidance:** Crafted pickle data can execute code; the documentation says not to unpickle untrusted or tampered data.
- **Conditions/limits:** Verify the remotely reachable loader and actual data provenance. A signature is meaningful only if untrusted actors cannot obtain valid signed inputs or control the key.

## Static-analysis documentation

<a id="os-18"></a>
### OS-18 — CodeQL Python command-line injection

- **Source/version:** CodeQL query help for `py/command-line-injection`; [original](https://codeql.github.com/codeql-query-help/python/py-command-line-injection/).
- **Guidance:** A path query flags user input reaching process-execution routines; its example recommends selecting from fixed command literals.
- **Conditions/limits:** Query coverage depends on language modeling and source/sink paths. It does not establish deployment exposure or all wrapper/option behavior.

<a id="os-19"></a>
### OS-19 — CodeQL Python code injection

- **Source/version:** CodeQL query help for `py/code-injection`; [original](https://codeql.github.com/codeql-query-help/python/py-code-injection/).
- **Guidance:** Describes user input reaching dynamic expression/code evaluation and recommends avoiding generated source.
- **Conditions/limits:** Manually review interpreter bindings, application-level reachability and transformations not captured by query models.

<a id="os-20"></a>
### OS-20 — CodeQL Java command-line injection

- **Source/version:** CodeQL query help for `java/command-line-injection`; [original](https://codeql.github.com/codeql-query-help/java/java-command-line-injection/).
- **Guidance:** Documents a query for user input passed into process execution and recommends fixed command choices where possible.
- **Conditions/limits:** Validate the actual command parser, wrappers and argument semantics. Query output is not a runtime exploit confirmation.

<a id="os-21"></a>
### OS-21 — CodeQL JavaScript command-line injection

- **Source/version:** CodeQL query help for `js/command-line-injection`; [original](https://codeql.github.com/codeql-query-help/javascript/js-command-line-injection/).
- **Guidance:** Shows remote query-derived values incorporated in a shell command as a source-to-sink flow.
- **Conditions/limits:** Check actual `child_process` options, route reachability and whether the argument is interpreted by a shell or the child program.

<a id="os-22"></a>
### OS-22 — CodeQL JavaScript second-order command-line injection

- **Source/version:** CodeQL query help; [original](https://codeql.github.com/codeql-query-help/javascript/js-second-order-command-line-injection/).
- **Guidance:** Documents that values such as a URL/argument may be stored or passed into a secondary command whose option changes command behavior.
- **Conditions/limits:** Trace the persistent value and later consumer in application code; do not assume all URL arguments trigger secondary execution.

<a id="os-23"></a>
### OS-23 — CodeQL JavaScript indirect command-line injection

- **Source/version:** CodeQL query help; [original](https://codeql.github.com/codeql-query-help/javascript/js-indirect-command-line-injection/).
- **Guidance:** Documents indirect paths where a wrapper script invoked by a process API interprets attacker-influenced input.
- **Conditions/limits:** Locate the wrapper and its interpreter semantics; dataflow to the first process API may not describe the full chain.

<a id="os-24"></a>
### OS-24 — CodeQL path queries

- **Source/version:** CodeQL query-writing documentation; [original](https://codeql.github.com/docs/writing-codeql-queries/creating-path-queries/).
- **Guidance:** Path queries can show a modeled route from a source to a sink.
- **Conditions/limits:** Reported paths depend on models and database extraction. A path is a lead for manual context validation, not proof of remote reachability in a deployed service.

<a id="os-25"></a>
### OS-25 — CodeQL data-flow analysis limits

- **Source/version:** CodeQL query-writing documentation; [original](https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/).
- **Guidance:** Explains local/global dataflow tradeoffs and notes that flow through library functions without available source may not be computable.
- **Conditions/limits:** Unmodeled frameworks, custom serialization, reflection, storage/queue edges and missing library models can hide paths. No-result does not prove safety.

<a id="os-26"></a>
### OS-26 — Semgrep taint rule authoring

- **Source/version:** Semgrep rule-ideas documentation; [original](https://semgrep.dev/docs/writing-rules/rule-ideas).
- **Guidance:** Taint rules can specify patterns for sources, propagators, sanitizers and sinks to find modeled flows.
- **Conditions/limits:** Coverage depends on rule patterns, language, configuration and engine edition. Review custom sanitizers and interprocedural behavior; a documented rule was not run here.

<a id="os-27"></a>
### OS-27 — Semgrep taint glossary

- **Source/version:** Semgrep documentation glossary; [original](https://semgrep.dev/docs/writing-rules/glossary).
- **Guidance:** Defines taint concepts and distinguishes intraprocedural from cross-file analysis capabilities.
- **Conditions/limits:** Tool edition and language support vary. Static rules model only the paths they describe and can miss application-specific storage or worker flow.

## Corpus advisory sources

The research corpus files include a direct, source-specific citation and source-status label on each case. Their original sources are not duplicated here because the installable skill uses the limited representative paraphrases in its [case-pattern reference](case-patterns.md), not the full 55-case corpus. If a package reference is expanded to rely on another external source, add a locally attributed note here before citing it in operational guidance.

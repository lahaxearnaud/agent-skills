# Reusable RCE review patterns and controls

This file synthesizes code-review questions from the qualified records. A pattern is a lead, not a verdict: confirm the actual source, transformations, sink semantics, version, authorization, configuration, and execution trigger in the application under review.

## Command and process execution

**Pattern.** A network, webhook, message, or stored user value changes a shell program, executable path, command option, working directory, environment variable, or wrapper-script behavior. The key boundary is whether a shell parses a combined command string. A fixed executable and an argument vector can avoid shell metacharacter parsing, but the invoked program may still interpret a value as an option, path, script, URL, configuration, or secondary command. See the process cases in [the corpus](cases/command-and-process-execution.md), including indirect Git option behavior and the simple-git include chain.

**Controls.** Prefer a library API over a child process. If a process is necessary, keep the executable and option structure fixed, pass arguments as separate values, validate each value against the expected domain, use a trusted working directory, and avoid shell mode. Argument separation addresses shell syntax only; it does not neutralize option injection or a wrapper's own language. Restrict process permissions and environment as impact containment, not as a substitute for input-to-sink control.

**Counterexample.** `ProcessBuilder("tool", "--format", validatedFormat)` is not by itself shell injection. It may still be unsafe if `validatedFormat` can name a plugin or input file that the tool interprets as executable behavior. A local process call whose command is a constant and whose input only selects among hard-coded safe argument values is not a remote RCE flow unless another execution boundary is shown.

**Enabling conditions to prove.** Identify the shell/no-shell mode, argument boundaries, platform and quoting semantics, option parsing behavior, wrapper script, process identity, caller privileges, and remote route or job path. Do not assume a sanitizer is effective without checking its exact command grammar and platform.

## Dynamic code and interpreter evaluation

**Pattern.** Remote data is parsed as source code or an expression and reaches `eval`, `exec`, a script engine, expression interpreter, dynamic query evaluator, or equivalent. Look for code assembled through concatenation, formatting, decoding, templating, reflection, or a queue/database before evaluation. Cases include [dynamic evaluation reports](cases/dynamic-evaluation.md) and [template/expression reports](cases/template-and-expression-injection.md).

**Controls.** Keep code fixed and pass user values as typed data. Replace evaluation with a parser for the intended data format or an allowlisted operation map. If the product intentionally executes user-authored code, establish a real isolation boundary and its resource and host-access policy; a separate language context or restricted globals should not be assumed to be a security boundary without supporting documentation and version evidence.

**Counterexample.** A fixed expression such as `eval("1 + 2")`, an evaluator receiving a parsed numeric value rather than user-controlled source, or a branch selecting a fixed function is not an established remote code-injection path. Still check whether later concatenation, custom functions, or object methods reopen execution.

**Enabling conditions to prove.** Establish who controls the source text, which interpreter and mode is active, what host APIs or bindings are exposed, whether the code path is reachable, and what privilege the interpreter inherits. A prompt-injection finding is not RCE unless untrusted content crosses into a real execution-capable sink.

## Template and expression injection

**Pattern.** Attacker-controlled template *source* is compiled or interpreted. This is different from trusted template source that renders an untrusted value as data. A stored template may execute on a later notification, report, export, or job. Check the authoring route, render trigger, template engine, custom functions/filters, object model, sandbox mode, and engine version. Examples include Grav/Twig, Jinja2, FreeMarker, Nunjucks, Velocity, and Groovy records in [the template corpus](cases/template-and-expression-injection.md).

**Controls.** Keep template source trusted and pass user values only through the renderer's data model. If user-authored templates are a product feature, use the engine's documented sandbox on a dedicated environment with a narrow allowlist of tags, functions, filters, methods, properties, and objects. Review every custom extension and wrapper; escaping HTML output does not constrain server-side expression execution. Avoid regex blacklists and do not assume a sandbox from the engine name alone.

**Counterexample.** Rendering `trustedTemplate` with a remote string in a plain text field is ordinarily data rendering, not SSTI. It becomes a candidate only if that value is subsequently reinterpreted as template source, an expression, or executable configuration.

**Enabling conditions to prove.** Show where template text originates, where compilation/rendering happens, which principal can author it, when rendering occurs, the sandbox policy in the deployed version, exposed object capabilities, and the process identity.

## Unsafe deserialization

**Pattern.** Remote bytes or objects are passed to a format that reconstructs executable object types or invokes hooks, constructors, proxy resolution, callbacks, or gadget behavior. Review Java native serialization, PHP object serialization, Python pickle, YAML object constructors, framework serializers, and RPC/session formats. The [deserialization cases](cases/unsafe-deserialization.md) show why the type set, library version, reachable gadget or callback path, and actual input route matter.

**Controls.** Prefer data-only formats and schemas; reject unexpected fields and types. Avoid unsafe object formats across trust boundaries. When unavoidable, apply a strict type allowlist and resource limits using the relevant library's supported mechanism, keep gadgets/dependencies patched, authenticate data before parsing where the protocol permits, and do not treat integrity checks as proof that a source is trustworthy.

**Counterexample.** A JSON decoder producing primitive data, or a Java serialization call with an effective restrictive filter and no alternate deserialization path, is not automatically an RCE. A call to `unserialize` or `ObjectInputStream` is a high-priority candidate, but RCE requires evidence for controllable input and an executable behavior path in the target dependency set.

**Enabling conditions to prove.** Trace attacker bytes to the deserializer; identify accepted classes/tags, callbacks and reachable gadgets, dependency versions and classpath, filters, authentication, and what operation consumes the reconstructed object. Do not infer a gadget from a package name alone.

## Dynamic loading and later-executed chains

**Pattern.** A remotely influenced name, path, URL, archive, plugin, model, module, or file reaches a loader/compiler/include/require/import mechanism, or can overwrite an artifact later loaded by a service, worker, scheduler, or administrator action. See [loading and execution-chain cases](cases/dynamic-loading-and-execution-chains.md).

**Controls.** Resolve identifiers through fixed registries; constrain file access to trusted immutable directories; separate upload/storage locations from executable code and configuration; validate type and origin; use atomic writes and least privilege; protect later load/job triggers. Treat an arbitrary file write as a primitive whose impact depends on path, permissions, loader, and timing.

**Counterexample.** Uploading a file into a non-executable isolated object store, where no loader, include path, template renderer, startup scan, worker, or privileged operator later consumes it, does not establish RCE. A service that imports only a compile-time fixed module is not dynamically loading attacker-selected code.

**Enabling conditions to prove.** Trace the remote write or identifier to the actual load; establish path normalization and symlink behavior, file ownership/permissions, extension or content checks, runtime module search paths, worker reachability, execution identity, and delay/trigger conditions. Mark later execution as conditional when the source does so.

## Cross-family chain review

Real incidents can combine families: template evaluation may instantiate a process object; deserialization may invoke a loader; upload may become a plugin import; a stored task may later run in a worker. Model each edge separately and cite the code that connects it. Do not collapse “remote input exists” and “RCE exists” into one inference. If any required link is absent, report a candidate with the exact missing edge rather than confirmed RCE.

## Impact and confidence

Report the process/container/service identity, reachable privileges, secrets and files within its access, network reachability, persistence, and affected tenant boundary only when the source or reviewed deployment evidence supports them. A CWE, CVSS score, or advisory's “critical” label does not fill in unknown runtime configuration. Restrictive permissions and sandboxing can bound impact; they do not erase an unsafe remote execution path.

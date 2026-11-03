# Static RCE review workflow

Use this sequence for repository code review. The result is a source-supported assessment of a possible remote path; it is not a runtime exploit confirmation.

## 1. Establish repository and deployment scope

- Read repository instructions, security notes, deployment manifests, routes, service definitions, queue/worker configuration and feature flags.
- Record languages, frameworks, interpreter/process versions and operating-system assumptions from manifests and configuration. Mark unavailable runtime facts unknown.
- Include HTTP, RPC, webhook, network consumer and network-configured management paths. Include a worker only when code/configuration shows how remote-controlled input or job state reaches it. Keep standalone local CLI/CI abuse separate unless an application remotely controls or triggers the path.
- Do not run the application, payloads, scanners, build hooks with untrusted data, or target network requests.

## 2. Find remote sources and follow the data

Inventory request bodies, route/query/header values, uploaded files, remote model/configuration imports, webhook events, queue messages, database-backed settings, templates, job descriptors and values received from other services. Note authentication, ownership checks and the principal that can modify each value.

Trace values through parsing, canonicalization, encoding, validation, string/AST construction, object conversion, persistence, queueing, callbacks and wrapper functions. Search cross-file and delayed paths: the write route and execution route may be different. An identifier, file path or database row may be the bridge between them.

## 3. Locate and classify execution boundaries

Use family guides to find process APIs, interpreters, template compilers/renderers, object deserializers, dynamic loaders, module imports, plugin systems and later-consumed files/jobs. Record what the API actually interprets: shell text, argv, code, expression, template source, serialized object, module name or file.

A sink name is not enough. Decide whether remote data changes executable semantics or only becomes data. For process execution, distinguish shell syntax from argument/option interpretation. For templates, distinguish template source from a value rendered by trusted source. For deserialization, identify object behaviors and a reachable executable path. For file writes, find a later loader/consumer.

## 4. Verify conditions and controls

Check affected library versions, platform, feature flags, configuration, route reachability, role/permissions, object or plugin availability, queue trigger, process identity, working directory and environment. Inspect validators and “sanitizers” in their exact context; a generic escaping function may protect one parser while leaving another parser or option grammar exposed.

Prefer code/data separation: safe library APIs, fixed operations or executable allowlists, typed data parsing, trusted template source with untrusted values, data-only serialization and constrained loader registries. Treat sandboxes, filters and argument arrays as controls to verify in the actual version and call path, not as automatic proof of safety. See the [offline source notes](offline-sources.md) for the local documentation basis.

## 5. Assign evidence status

- **Not an RCE path:** source is not attacker controlled, no execution boundary is reached, or values remain data under the actual API semantics.
- **Candidate / incomplete:** a relevant sink or unsafe primitive exists but source reachability, version, gadget, configuration, authorization, trigger or later execution is not established. Name the missing edge.
- **Static flow established:** reviewed source code connects a remotely influenced value to an execution-capable boundary and the necessary conditions are visible in the repository. State deployment facts that remain unknown; do not claim runtime reproduction.
- **Reported vulnerability pattern:** a corpus advisory documents a similar product issue. This helps prioritize a search but does not establish that this repository shares the bug.

Do not call a static review “exploited,” “confirmed in production,” or “RCE achieved.” Severity should reflect the evidence and the execution identity, reachability and privilege actually supported by code/configuration.

## 6. Produce a reviewable result

Follow the [report standard](report-standard.md). Include a concise source-to-sink path, file:line evidence for every edge, preconditions, relevant version/configuration, impact boundaries, remediation, confidence, and unknowns. Include a short safe or incomplete counterexample when it clarifies a false-positive distinction.

## Tool use

Static analyzers can help locate paths when their language, source/sink models, query pack and analysis scope fit the code. Treat missing results as inconclusive and findings as leads requiring manual review. The documented models and limits are summarized in [offline sources](offline-sources.md); the corpus lists additional query references in its separate research files. No scanner is required to apply this workflow.

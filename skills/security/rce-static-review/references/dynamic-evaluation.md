# Dynamic code and interpreter evaluation

## What to trace

Search for code-generation and evaluation APIs: `eval`/`exec` variants, script engines, expression-language parsers, runtime compilation, command interpreters, dynamic query languages, and framework helpers that convert text into executable expressions. Include wrappers, string formatting, decoding, database storage and message/job state between source and evaluator.

Prove that an attacker can influence the program/expression text or executable object accepted by the evaluator. Then inspect what the runtime exposes: host functions, modules, filesystem, process APIs, reflection, custom functions, globals, class loaders, callbacks and resource limits. A prompt or natural-language instruction is not itself code execution: locate the explicit tool/compiler/interpreter edge.

Node's `vm` contexts are explicitly not a security mechanism. A separate context, restricted globals, or a framework-specific “sandbox” label must not be credited without documentation for the exact runtime and code path. See [OS-13](offline-sources.md#os-13), [CWE-94](offline-sources.md#os-16), and the [evaluation patterns](case-patterns.md#dynamic-evaluation).

## Candidate threshold

Remote input reaches code or expression compilation/evaluation, including deferred evaluation after persistence or queuing. A fixed expression, numeric parser, or typed AST from a safe grammar is not enough to establish code injection. Check whether custom operators, function bindings, reflective lookups or string interpolation turn the parsed value back into code.

## Controls to verify

- Do not generate executable source from remote values. Call a fixed function with typed arguments or map a small user-selected action to fixed implementations.
- Use a data-only parser with an explicit schema and size/depth limits.
- If user-authored code is a necessary product feature, isolate it outside the main service with least privilege, restricted capabilities, resource ceilings and no ambient secrets. Verify the isolation boundary; a language context alone may not provide one.
- Review runtime version, registered bindings and any helper that transforms values before evaluation.

## Common false positives

- Fixed code passed to an evaluator is not user-controlled code merely because the evaluator is powerful.
- A safe expression DSL is not equivalent to a general-purpose interpreter; enumerate allowed syntax and functions.
- A dynamic query or template may read data or trigger side effects without reaching OS-level code execution. Label the supported impact precisely.
- “AI agent can execute tools” requires a remotely reachable, attacker-influenced instruction path and an enabled execution-capable tool; do not infer it from an LLM dependency.

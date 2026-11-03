# Unsafe deserialization and object reconstruction

## What to trace

Find object-capable formats at network boundaries and through intermediate storage: Java native serialization, PHP serialized objects, Python pickle/shelve, YAML object constructors, framework-specific session or RPC codecs, and dependencies that deserialize on behalf of the application.

For each path, establish:

- which remote bytes or object graph are parsed and whether authentication/signature checks happen before parsing;
- which types, classes, constructors, hooks, proxies, callbacks or class-resolution paths are allowed;
- whether a compatible executable gadget or callback exists in the actual dependency/classpath/version;
- which endpoint, queue, webhook, cache, cookie, session or background job reaches it;
- whether a strict filter is installed on this specific deserialization operation and whether any alternate path bypasses it.

PHP documents that `unserialize` of untrusted input can load/execute code through object construction and autoloading, even with `allowed_classes`; Python warns that malicious pickle data can execute code. Java's `ObjectInputFilter` can restrict classes and graph resources, but must actually be configured. See [OS-08–OS-10](offline-sources.md#os-08), [CWE-502](offline-sources.md#os-17), and [deserialization patterns](case-patterns.md#unsafe-deserialization).

## Candidate versus RCE

An untrusted object-capable deserializer is a high-priority candidate. Do not claim RCE from the API alone. Show how remote bytes reach it and identify the executable callback/gadget or behavior path in the application's dependency set. If no gadget is identified, use “unsafe deserialization candidate; RCE not established.” If there is an independent denial-of-service or type-confusion impact, report that separately and only if supported.

JSON data deserialization is not equivalent to arbitrary object reconstruction. Still inspect custom JSON hooks, polymorphic type metadata, constructors or downstream dispatch that might create an executable path.

## Controls

- Prefer schema-validated data-only formats; reject unknown types/fields.
- Avoid native object serialization across trust boundaries.
- When legacy use is unavoidable, apply the runtime's strict class/type allowlist plus graph, depth, size and reference limits; verify filter installation at every entry point.
- Authenticate signed data before deserialization only when key ownership and canonicalization are sound; integrity does not help when an attacker can submit valid signed objects or compromise the signing key.
- Remove vulnerable gadget dependencies and review callbacks that run during reconstruction.

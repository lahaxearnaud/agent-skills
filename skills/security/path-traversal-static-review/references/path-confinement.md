# Path confinement and normalization

## What a correct boundary means

The policy concerns the **resolved filesystem object**, not whether the original string looks harmless. For a trusted root and a candidate, the code must reject candidates outside the root by path components, on the platform and filesystem actually used, at the relevant read/write/delete operation.

An illustrative weak check is:

```js
const target = path.resolve(root, requestedName);
if (!target.startsWith(root)) throw new Error('outside root');
return fs.readFile(target);
```

The prefix can also match an adjacent directory whose name begins with the root string. This snippet is a pattern to recognize, not proof that every path API or deployment behaves identically.

## Common incomplete controls

- **Denylist only:** filtering `../`, `/`, or a list of sensitive prefixes misses alternate separators, absolute forms, encodings, platform namespaces, and paths created after the check.
- **Validate before decoding/canonicalization:** a later decoder or normalizer can introduce separators or parent segments. Decode once to the application's intended representation, then apply policy to that same representation.
- **Double decoding:** a framework may decode once and application code decode again. Trace raw and decoded values through proxies, router, framework, app, and filesystem.
- **String prefix/contains:** string prefix is not a path-component relation; `contains(root)` can accept even more unrelated values.
- **Normalization only:** lexical `normalize` can collapse dot segments but does not necessarily resolve symlinks or protect a later open from filesystem changes.
- **`basename()` only:** may reduce components for a flat name policy, but behavior is platform-dependent and it does not prove the final target is confined against symlinks/races.
- **Absolute input:** library-specific. A later absolute component may override a base in some `resolve`/join APIs; verify rather than infer.
- **`realpath()` success assumed:** PHP `realpath()` can fail for missing/unreadable paths. A false/empty fallback can make a check ineffective.
- **Check then use:** canonicalizing and checking before a later file open can leave a time-of-check/time-of-use window if an attacker can change links/directories.
- **One guarded route:** sibling endpoints, compressed variants, backup actions, fallbacks, or read/write/delete branches may bypass the stronger check.

## Safer design direction

1. Prefer an opaque file/object ID resolved through an authorization-aware server-side map over accepting a client path.
2. If relative paths are required, define an allowlisted grammar and reject absolute, drive/UNC, namespace, null-byte, and disallowed parent-segment forms before filesystem use. Denylists are not the boundary.
3. Resolve using the exact language/platform API and compare components with a maintained path-aware operation. Do not use raw string prefix as the only check.
4. For existing files, check the canonical target against the canonical root immediately at the access point.
5. For a non-existing write destination, validate a canonical existing parent, use exclusive creation and a private directory, and consider descriptor-relative/no-follow operations when hostile mutation is possible. Avoid a claim that `realpath()` alone makes a write race-free.
6. Keep sensitive files, executable application code, and attacker-writable content in separate directories and restrict process permissions. These measures reduce impact but do not make an unconstrained path safe.

Symfony `Path::canonicalize` and `Path::isBasePath`, Node `path.relative`, Java path APIs, and PHP `realpath()` provide different guarantees. Use the bundled [offline filesystem/API notes](offline-sources.md) first. If a behavior for the installed version is not covered there, inspect source or documentation already present in the dependency, or state it as unknown. Do not fetch external docs during a review. Lexical helpers do not automatically resolve symlinks or close race windows.

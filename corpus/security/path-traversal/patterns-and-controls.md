# Recurring patterns and controls

These rules are a synthesis of the [case register](published-cases.md) and the primary documentation in [sources](sources.md). They are review heuristics, not proof that a particular finding is exploitable.

## Repeating source-to-sink shapes

| Pattern | Code-review question | Cases that illustrate it |
|---|---|---|
| Request or API value becomes a path | Does a route parameter, header, URI, filename, tenant setting, archive field, or template name reach a filesystem operation? | PT-006, PT-010, PT-016, PT-018, PT-023, PT-040 |
| Lexical normalization mistaken for confinement | After normalization, is the result checked by path components, or only by raw `startsWith`, substring, or a denylist? Can an absolute path replace the root in this API? | PT-010, PT-027, PT-041, PT-043, PT-045, PT-047, PA-03 |
| Decode/normalize order differs | Which component decodes the value, how many times, and does validation happen on the same representation that reaches the OS? | PT-010, PT-011–014, PT-020, PT-026, PA-13 |
| Separator/platform mismatch | Does URL path normalization recognize backslash while the target OS treats it as a separator? Are drive, UNC, or namespace-prefixed paths possible? | PT-002, PT-028, PT-046, PA-12 |
| Symlink following or race | Does a static handler, template loader, archive extractor, or file sink resolve links? Can an attacker create/change a link between check and use? | PT-019, PT-022, PT-025, PT-044, PA-05, PA-08 |
| Archive entry becomes output path | Are ZIP/TAR names validated individually before creating any file? Can links, absolute names, parent segments, backslashes, or extraction order escape the destination? | PT-017, PT-028–029, PT-036, PT-038, PT-050, PA-04–10 |
| Template/resource name becomes a file lookup | Can an untrusted value select a Twig/FreeMarker/script template or a framework resource path? Does the loader enforce its configured directory after namespace and separator processing? | PT-002, PT-007–009 |
| Similar handlers have inconsistent protections | Are sibling routes, extensions, compressed variants, fallback branches, or write/read/delete paths checked independently? | PT-004, PT-012–014, PT-016, PT-022, PT-032–034 |

## Static review method

1. **Inventory file sinks and path helpers.** Search for framework download/static/template handlers and filesystem APIs such as reads, writes, moves, deletes, metadata checks, archive extraction, path joins/resolution, and file-backed resource/cache APIs. Follow wrappers rather than stopping at the first helper.
2. **Trace a source to a real sink.** Record the exact untrusted source and transformations. A path-related route string alone is not a finding if it selects a fixed server-owned identifier and never controls a path component.
3. **Establish reachability and prerequisites.** Inspect routing, middleware/authorization, feature flags, configuration, dependency versions, allowed content writers, filesystem layout, OS/container assumptions, and process permissions. Keep unknowns explicit.
4. **Reconstruct each representation.** Note URL decoding, framework route extraction, application decoding, Unicode/string conversion, separator normalization, `join`/`resolve`, canonicalization, symlink resolution, and the final file API. Validation before a later transform may not protect the sink.
5. **Prove or reject confinement at the sink.** Ask whether the exact final object is inside the intended root by path-component boundary and filesystem resolution, not whether an input string looks clean. For non-existing write targets, inspect how the parent is created and whether symlinks or races can intervene.
6. **Assess each operation independently.** Read, write/overwrite, delete, existence/metadata checks, template lookup, and archive export have different impacts and preconditions. Do not infer code execution from a write unless the destination and execution path are established.
7. **Classify the result.** Use confirmed source-to-sink path escape, candidate requiring stated conditions, no issue shown due fixed mapping/allowlist, or insufficient evidence. State confidence separately from severity.

## Defensive design

- Prefer opaque server-owned object identifiers mapped to authorized storage records. Do not accept a raw path where an identifier or fixed route/template key suffices.
- If a relative path is required, decode according to the protocol exactly once, reject absolute/drive/UNC and disallowed namespace forms, normalize using the target platform's path API, and verify the resolved path remains within the canonical root using a path-aware boundary check. Do not use a string prefix as the boundary.
- For existing read targets, canonicalize the actual target and compare it with the canonical root at the final access. Account for symlinks. For write/delete targets that may not exist, canonicalize the existing parent and use race-resistant, descriptor-relative or platform-appropriate operations where hostile filesystem mutation is possible. `realpath()` and a later open are not automatically race-free.
- For archive extraction, inspect every member before writing; reject absolute paths and any member whose resolved destination escapes the extraction root. Define an explicit symlink/hardlink policy, avoid following pre-existing links, and extract into a fresh private directory. A filename sanitizer or a library default is not proof: inspect the library version, options, platform behavior, and wrapper code.
- In static-file and template frameworks, prefer built-in handlers with tested root confinement, keep roots limited to intended public files, disable options that deliberately follow outside symlinks, and use a fixed allowlist of templates/resources rather than user-derived names.
- Keep route and filesystem path interpretation aligned across proxy, router, framework, application, and OS. Do not rely on a WAF or one layer's decoding behavior to compensate for unsafe sink handling.
- Apply authorization before sensitive lookup and independently to every sibling route and fallback. Authorization does not replace path confinement, and confinement does not replace object-level authorization.
- Minimize process filesystem permissions and keep secrets, executable code, and mutable uploads outside each other's trust boundaries. This reduces consequences but does not repair the path flaw.

## Impact language

Report only impact supported by the source and inspected code:

- **Read:** files reachable by the process; sensitivity depends on deployment and file permissions.
- **Write/overwrite:** integrity impact; execution is conditional on a written file being later interpreted or loaded.
- **Delete:** availability or data-integrity impact, depending on the target.
- **Existence oracle:** metadata disclosure; do not call it file-content disclosure.
- **Template/resource access:** clarify whether the result is file disclosure, template rendering, or code execution; these are not interchangeable.
- **Zip Slip archive output:** state whether the server writes outside its extraction root or instead distributes a dangerous archive for a recipient to extract.

The repository does not assign a universal severity from a CVE score. In a review, tie severity to the current actor, authentication, route exposure, data, process permissions, target paths, and any proven follow-on chain.

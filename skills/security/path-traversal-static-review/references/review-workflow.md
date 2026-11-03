# Review workflow

Use this sequence for a repository review. The corpus is research material, not proof that the current project is vulnerable.

## 1. Define the surface

Identify the relevant application entry points and trust boundaries: HTTP routes, background jobs triggered by uploads/imports, file download endpoints, static handlers, template loaders, resource caches, API file identifiers, restore flows, and build/server-side rendering tools. Determine whether a path is local filesystem state, a virtual filesystem, an archive member, or an object-store key; do not treat these as interchangeable.

## 2. Build the flow

For each candidate, record:

| Element | Questions |
|---|---|
| Actor/source | Who controls it: anonymous request, authenticated user, project member, administrator, remote file server, imported archive, tenant setting, or only a local operator? |
| Value | Is it a raw path, identifier, URI, filename, template name, archive entry, or metadata field? |
| Transformations | Which router/framework decodes it? Is there a second decode, string conversion, separator conversion, case fold, normalization, or `join`/`resolve`? |
| Guard | What is checked, on which representation, and before or after which transformation? Does it compare path components or raw strings? |
| Sink | Which exact read/write/delete/metadata/serve/extract call receives the resulting path? |
| Conditions | Which route, middleware, config flag, version, OS, container, directory layout, symlink, permission, or later action is required? |

Follow tainted values through wrappers and callbacks. A route name or path parameter is not enough; a valid fixed identifier map may break the taint path. Conversely, do not stop at a method named `sanitizePath` or `safeJoin`: inspect its exact semantics and the later sink.

## 3. Reconstruct path semantics

Trace URL parsing and filesystem interpretation separately. Note raw versus decoded path components, framework route decoding, application decode calls, proxy/CDN normalization, URL-versus-OS path libraries, platform separators, absolute paths, drives/UNC forms, and symlink handling. Check whether later code or the OS resolves parent segments after a guard.

For an existing file, determine whether the checked canonical target is the same target subsequently opened. For a new write target, inspect failure handling for missing paths, canonicalization of existing parents, directory creation, symlink handling, exclusivity, and whether an attacker can modify a parent between check and use.

## 4. Test the counterexample in source reasoning

Do not generate or send a payload. Instead, use source-derived examples to see whether the guard logically accepts a path outside the root:

- Does a sibling path share the root's character prefix?
- Does an absolute path override a base in this language/API?
- Can a request be decoded again after validation?
- Does the target OS recognize a separator the validator does not?
- Does a symlink or archive-created link change the target after lexical checking?
- Does a fallback, extension variant, or sibling route skip the main handler's guard?

Only report a candidate if the code's semantics and required conditions support it. If exact runtime/parser behavior is unknown, describe what source/configuration would resolve the uncertainty; do not claim to have tested it.

## 5. Establish impact and status

Classify the final operation and the highest supported consequence. Read access is limited by process permissions and route exposure. A write may become code execution only if it lands in a location later interpreted/loaded; a delete may affect availability; an existence check can leak metadata without returning contents. Archive generation may endanger a recipient during extraction rather than write on the server.

Use one status:

- **Source-supported path escape:** source, transformations, missing/ineffective boundary, and sink are visible.
- **Candidate, conditions missing:** source path is plausible but reachability/deployment/version/filesystem condition is not established.
- **No traversal shown:** fixed identifiers or trusted server-side mapping prevent the untrusted value from selecting a path in the reviewed scope.
- **Insufficient evidence:** essential source, helper, configuration, or sink is absent.

Severity remains unassigned unless the project defines a rubric and the evidence supports the relevant inputs.

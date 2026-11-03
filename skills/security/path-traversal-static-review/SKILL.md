---
name: path-traversal-static-review
description: Use when reviewing Web or server-side code for directory/path traversal, unsafe file download or static paths, template/resource lookup escapes, archive extraction (Zip Slip), symlink escapes, or user-controlled filesystem names.
---

# Static path traversal review

Review how an untrusted value can influence a filesystem path, then determine whether the final filesystem operation is confined to its intended root. A suspicious path string is not enough: connect the source, transformations, guards, sink, and reachability before reporting an issue.

## Scope

This is a source-only review. Do not launch the target application, browser, payload, dynamic scanner, or network request. Inspect source, templates, routes, middleware, configuration, dependency declarations, and existing static evidence. Local code search, repository indexing, and configured static-analysis findings may help locate candidates; trace every candidate to source and sink. Vue code is in scope only where SSR, a server route, build tool, or native WebView performs filesystem operations; browser-only path manipulation is not a server filesystem traversal.

Review read, write/overwrite, delete, static/download, template/resource, archive import/restore, archive generation, symlink, and metadata/existence paths. Generic upload validation without a path escape is separate.

## Review method

1. Inventory path sources and file sinks, then trace the exact source-to-sink flow. Follow helper methods, framework handlers, archive libraries, and all fallback branches.
2. Record each representation change: request parsing, percent decoding, string conversion, separator changes, normalization, canonicalization, link resolution, and path joining. Validation must apply to the representation that reaches the sink.
3. Check that the resolved target stays inside the intended root using path-component boundaries. A raw `startsWith`, `contains`, denylist, `basename`, `normalize`, or successful route match alone does not prove confinement.
4. Inspect symlinks and time-of-check/time-of-use gaps. Existing-file canonicalization does not automatically protect a later open/write, and a not-yet-existing target needs a safe parent/create strategy.
5. Establish route reachability, actor permissions, feature/configuration requirements, operating system/container, filesystem layout, and process permissions. Keep missing conditions explicit.
6. Assess read, write, delete, metadata, template, and archive consequences separately. Treat execution as conditional unless the path to an executable/loadable destination and its later use are evidenced.

Use the detailed [review workflow](references/review-workflow.md), [source/sink catalog](references/source-sink-catalog.md), [confinement guide](references/path-confinement.md), [archive/link guide](references/archive-and-symlink.md), and [offline filesystem/API notes](references/offline-sources.md) as needed. Do not fetch API documentation during a review. If the local notes do not establish behavior for the installed version, inspect source already present in the repository or state the behavior as unknown.

## Finding standard

Report a **source-supported path escape** when visible code constructs an out-of-root target and reaches a file operation. Call it a **candidate** when a required route, version, deployment, filesystem, or permission condition is not shown. Report **no traversal shown** when a fixed server-owned map or allowlist prevents the request value from becoming a path. Use **insufficient evidence** when the source-to-sink link cannot be completed.

Do not infer arbitrary-file access from an existence check, a write from a read, RCE from a write, or exposure of every host file from one disclosed file. Do not assign severity without the repository rubric and evidence for actor, reachability, data, and impact. Use the [report template](references/report-template.md) and state that no runtime test was performed.

## Quick checks

| Pattern | Review question |
|---|---|
| User-controlled filename/template/URI | Does it reach `open`, `read`, `write`, `delete`, `sendFile`, resource lookup, or extraction? |
| Prefix/denylist guard | Is the final canonical path inside the root at the filesystem boundary? |
| URL decoding or path normalization | Can another layer decode or reinterpret the value after the check? |
| Archive member | Is every output path confined, including links and extraction order? |
| Sibling route or fallback | Does it use the same protection as the better-defended endpoint? |

## Common mistakes

- Treating cleaned input as proof of confinement.
- Treating lexical normalization as symlink-safe or race-free.
- Treating authorization, a WAF, or a static root setting as a substitute for final path validation.
- Claiming RCE or unrestricted disclosure without evidence of the destination, process permissions, and follow-on behavior.

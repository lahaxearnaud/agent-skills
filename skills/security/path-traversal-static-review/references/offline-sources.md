# Path and filesystem sources (offline notes)

Use these bundled summaries instead of fetching external pages during an offline source review. They are paraphrases, not full copies or substitutes for the exact installed implementation. The URLs preserve attribution and support later maintenance. Consult local dependency source when a version-specific behavior is not covered; otherwise state the uncertainty.

Research snapshot: **2026-11-03**.

## Weakness and protocol references

| Source | Local summary and limits |
|---|---|
| [CWE-22](https://cwe.mitre.org/data/definitions/22.html), [CWE-23](https://cwe.mitre.org/data/definitions/23.html), and [CWE-36](https://cwe.mitre.org/data/definitions/36.html) | CWE-22 covers improper restriction of a pathname to a restricted directory; CWE-23 and CWE-36 distinguish relative and absolute traversal. Use these labels to classify a demonstrated path boundary failure, not to infer exploitability or impact. |
| [CWE-59](https://cwe.mitre.org/data/definitions/59.html) | Covers improper link resolution before file access. A lexical path check can pass while a symlink resolves outside the intended root. Verify whether the sink follows links and whether an attacker can create or replace them. |
| [CWE-180](https://cwe.mitre.org/data/definitions/180.html) and [CWE-174](https://cwe.mitre.org/data/definitions/174.html) | CWE-180 addresses validating before canonicalization; CWE-174 addresses double decoding. Trace the exact representation checked and the representation later interpreted by the framework, library, or filesystem. These categories do not prove a particular transformation occurs. |
| [RFC 3986, URI normalization](https://www.rfc-editor.org/rfc/rfc3986) | Percent-encoding and URI dot-segment removal are URI-layer rules. They do not define operating-system filesystem canonicalization, symlink resolution, or how every framework decodes a request. Trace each parser boundary separately. |
| [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) | Prefer server-generated storage names, storage outside executable/public roots where appropriate, layered validation, and safe archive handling. Filename validation alone is not path confinement; archive entries and the final filesystem destination still need a safe policy. |

## API behavior notes

| Source | Local summary and limits |
|---|---|
| [Symfony Filesystem Path component](https://symfony.com/doc/current/components/filesystem.html) | `Path` helpers perform path manipulation and lexical canonicalization according to their documented platform rules. `isBasePath()` is intended to check a path-component base relation, but lexical helpers do not resolve filesystem symlinks or make a later open race-free. Check the installed Symfony version and exact helper used. |
| [PHP `realpath()`](https://www.php.net/manual/en/function.realpath.php) | Resolves `.`/`..` and symbolic links for an existing accessible path and returns `false` when resolution fails, including for some missing or inaccessible paths. A check followed by a later open/write can race; a non-existing destination needs a safe parent/create strategy. |
| [PHP `ZipArchive::extractTo()`](https://www.php.net/manual/en/ziparchive.extractto.php) | The method extracts archive members into a destination, but applications must not assume every PHP/ZIP version, wrapper, or caller-managed extraction flow provides the required confinement. Check the exact version and destination behavior; validate members and links at the write boundary. |
| [Node.js `path` API](https://nodejs.org/api/path.html) | `resolve`, `join`, `normalize`, and `relative` are lexical operations with platform-specific separators and absolute-path behavior. They do not resolve symlinks. `relative(root, target)` can support component-aware checks, but the result and final filesystem object still need to be examined at the sink. |
| [Java `SecureDirectoryStream`](https://docs.oracle.com/en/java/javase/27/docs/api/java.base/java/nio/file/SecureDirectoryStream.html) | Provides directory-relative operations intended to reduce races while accessing entries beneath an open directory. Provider support is optional; do not assume it is available or used without source and runtime-provider evidence. |
| [Python `zipfile`](https://docs.python.org/3/library/zipfile.html) | Standard extraction helpers apply documented path cleanup, but that does not automatically protect caller-managed paths, custom extraction code, link handling, every version, or later writes. Inspect the exact API call and the application wrapper. |

## Review consequence

Treat this file as an offline reference aid. If the reviewed package version differs from a version-specific note, inspect the locally installed source or record the behavior as unknown. Never replace source-to-sink evidence with a CWE label, standard, or documentation summary.

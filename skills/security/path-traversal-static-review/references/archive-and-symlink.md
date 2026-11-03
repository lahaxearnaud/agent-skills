# Archive extraction, symlinks, and races

Treat every archive entry as an untrusted path. A destination root argument does not prove that each output stays inside that root.

## Archive review checklist

- Find every extraction, restore, import, unpack, and archive-to-filesystem operation, including transitive library wrappers.
- Trace each member name from the archive/manifest through decode, separator conversion, normalization, path join, and final create/open.
- Establish whether absolute paths, parent segments, drive/UNC prefixes, backslashes, alternate separators, or platform-specific names are accepted.
- Inspect link entries (symbolic or hard links), pre-existing destination links, archive ordering, and whether a later member writes through an earlier-created link.
- Check the canonical destination at creation time. Reject entries whose final path escapes by path components. Do not validate one normalized string then open a differently normalized value.
- Determine whether extraction overwrites, creates parent directories, preserves mode, or deletes existing files. Check the actor's import permissions and application process privileges.
- Distinguish server-side Zip Slip from unsafe archive generation. A generated archive with an escaping member may affect a user who later extracts it, even if the server never writes outside its root.
- Review resource limits separately; archive bombs are not path traversal unless a path escape is also present.

## Symlinks and time-of-check/time-of-use

Lexical path containment does not resolve a link target. Search whether an upload/build/deployment/archive path can create a symlink under a trusted directory, whether static/template handlers follow links, and whether compressed variants or fallback routes reopen a different path. If code checks a canonical path and later opens by name, assess whether an attacker can replace a path component in between. State the filesystem-writer and timing conditions; do not claim a race without an actor able to mutate the relevant path.

For hostile directories, prefer fresh private extraction directories, reject or safely handle link entries, use no-follow/exclusive creation where available, and avoid serving from directories writable by untrusted users. Exact protections differ by OS and library; inspect their version-specific behavior.

## Impact distinctions

- Server extraction outside a restore/upload directory: potential arbitrary file write/overwrite, bounded by process permissions and archive-trigger authorization.
- Symlink-following read: potential disclosure of files readable by the process.
- Archive generated for later extraction: client-side or recipient-side write risk; identify who downloads/extracts it.
- A write into executable/configuration code may enable later execution, but only if the deployment loads that file and the attacker can cause that follow-up.

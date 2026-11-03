# Source and sink catalog

Use these as search anchors, then inspect actual call flow and version-specific semantics. Names are indicators, not automatic findings.

## Repository search

Start with the languages/frameworks present in the repository. Read-only search tools such as `rg`, an IDE index, AST queries, and existing SAST/SARIF results can locate file operations and path checks. For example, search first for file read/write/delete and static/archive APIs, then search for joins/resolution, decoding, and string-prefix guards. Narrow results to request handlers, upload/import/restore services, template loaders, and helpers. Do not treat a match, rule result, or sanitizer name as a finding until the value is traced to the exact sink and conditions.

Do not use dynamic web scanners or send requests. If a static tool produces a result, use it as a review lead; confirm reachability, transformations, final operation, and path boundary in source.

## Common sources

- Request path, route parameter, query/body/header, multipart filename, redirect/return filename, user-selected download key.
- Tenant or administrator configuration, model/tokenizer URI, resource/template/view name, file identifier, cache key.
- Archive entry name, archive manifest/XML/metadata, backup/import path, remote FTP/SFTP/SMB filename.
- Database/config value that can be created or changed by a less-trusted actor.

## PHP, Symfony, and Twig

Search for `readfile`, `file_get_contents`, `file_put_contents`, `fopen`, `unlink`, `rename`, `copy`, `include`/`require`, `move_uploaded_file`, `ZipArchive::extractTo`, and string concatenation around storage roots. Review `Symfony\Component\Filesystem\Path`, `File`, `Finder`, controller download/static responses, and custom upload/import services. Check whether a route parameter becomes a path or selects a fixed server-side record.

For Twig and other template systems, inspect the configured loader, namespaces, template-name provenance, include/source/fetch calls, view-name creation, and whether the value is a fixed template key. Template-file disclosure and template code execution are distinct impacts; require source support for each.

`realpath()` resolves links and dot segments for existing paths, but returns `false` on failure. Review how failure is handled, how a write target that does not yet exist is constrained, and whether a later filesystem operation can race with the check.

## JavaScript and Node.js

Search for `fs.readFile*`, `createReadStream`, `writeFile*`, `unlink*`, `rename`, `copyFile`, `sendFile`, `download`, `express.static`, `path.join`, `path.resolve`, custom `safeStaticPath`, archive extractors, SSR route loaders, and user-controlled names passed to them. Inspect production-only middleware, router decoding, and all `root`/`followSymlinks`-style options.

Do not assume `path.join`, `path.resolve`, `path.normalize`, `path.basename`, or `path.relative` has the same semantics as another language or operating system. Check the exact function and whether the final path remains within the root by components. A string-prefix comparison can accept a similarly prefixed sibling.

Vue browser code alone cannot traverse a server filesystem. Follow it only into SSR, a backend endpoint, a build/dev server, Electron/NativePHP/WebView integration, or another file-capable environment.

## Java, Spring, and other JVM stacks

Search for `Paths.get`, `Path.resolve`, `File`, `Files.newInputStream/readAllBytes/write/delete`, `Resource`, `FileSystemResource`, static resource routers, template loaders, upload interceptors, and archive extraction. Inspect servlet container and framework firewall behavior only when configuration/version evidence is available. For race-sensitive code, consider whether descriptor-relative APIs such as `SecureDirectoryStream` are used and supported.

## Python, Go, and other server stacks

- Python: `open`, `pathlib.Path`, `os.path.join`, static send helpers, `zipfile`, tar extraction, framework upload/restore flows.
- Go: `os.Open/ReadFile/WriteFile/Remove/Rename`, `filepath.Join/Rel`, `http.ServeFile`, `http.FileServer`, archive readers, and request decoding in the router.
- Other stacks: find equivalent path construction, canonicalization, file operation, static handler, template resolver, and archive extraction APIs.

Check absolute-path behavior explicitly: some APIs ignore the base when the later component is absolute; others normalize differently. Consult the bundled [offline filesystem/API notes](offline-sources.md), then inspect the installed dependency source when its version differs; otherwise state the uncertainty. Do not depend on network documentation during a review.

## Sinks by operation

| Sink | What it can establish | What it does not establish by itself |
|---|---|---|
| Read/open/stream/send file | Potential file disclosure if the caller can reach it and process permissions allow it. | That all host files, secrets, or source code are readable. |
| Write/copy/upload/extract | Potential integrity impact outside intended root. | RCE without a later executable/loadable use. |
| Delete/remove/recursive remove | Potential integrity/availability loss. | File disclosure. |
| `exists`, `stat`, metadata check | Potential file or directory existence/metadata oracle. | Content read. |
| Template/resource include | Potential unintended file/template lookup. | Code execution unless the loaded content is evaluated in a proven executable context. |
| Archive generation | Potential unsafe member path for later extraction. | Server-side filesystem write; identify who extracts the archive. |

# Sources and research notes

Consulted on 2026-11-03. The main register prioritizes official vendor or project advisories and reviewed advisory records. These links are source material, not instructions to execute. Case entries paraphrase relevant facts; advisory payloads and long source passages are intentionally not copied.

## Standards and weakness references

- [CWE-22: Improper Limitation of a Pathname to a Restricted Directory](https://cwe.mitre.org/data/definitions/22.html) — relative/absolute path traversal, canonicalization and common pitfalls.
- [CWE-23: Relative Path Traversal](https://cwe.mitre.org/data/definitions/23.html) and [CWE-36: Absolute Path Traversal](https://cwe.mitre.org/data/definitions/36.html) — useful child classifications.
- [CWE-59: Improper Link Resolution Before File Access](https://cwe.mitre.org/data/definitions/59.html) — symlink/link-following boundary failures.
- [CWE-180: Validate Before Canonicalize](https://cwe.mitre.org/data/definitions/180.html) and [CWE-174: Double Decoding](https://cwe.mitre.org/data/definitions/174.html) — ordering and representation mismatches.
- [RFC 3986, §2.4 and §5.2.4](https://www.rfc-editor.org/rfc/rfc3986) — percent-encoding and URI dot-segment removal. URI normalization is not filesystem canonicalization; an agent must inspect each layer's behavior.
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) — server-generated names, upload storage boundaries, layered validation, and archive handling.

## Technology documentation

- [Symfony Filesystem component](https://symfony.com/doc/current/components/filesystem.html) — path canonicalization, joins, absolute/relative paths, platform differences, and `Path::isBasePath()` behavior. Lexical path normalization alone does not establish symlink-safe, race-free filesystem access.
- [PHP `realpath()` manual](https://www.php.net/manual/en/function.realpath.php) — resolves `.`/`..` and symlinks for existing paths and returns `false` on failure; code must handle failure and consider check-to-use races.
- [PHP `ZipArchive::extractTo()` manual](https://www.php.net/manual/en/ziparchive.extractto.php) — behavior of PHP ZIP extraction; verify the PHP/zip version and target directory state rather than assuming all extraction libraries behave the same.
- [Node.js `path` API](https://nodejs.org/api/path.html) — platform-specific path resolution, normalization, and relative-path operations; verify the exact API and platform used by the application.
- [Java `SecureDirectoryStream`](https://docs.oracle.com/en/java/javase/27/docs/api/java.base/java/nio/file/SecureDirectoryStream.html) — descriptor-relative operations intended for security-sensitive race-resistant directory traversal where supported.
- [Python `zipfile` documentation](https://docs.python.org/3/library/zipfile.html) — extraction APIs versus caller-managed paths such as `ZipInfo`; the documented safety behavior is API-specific and version-dependent.

## Source-quality notes

- Vendor/project advisories are preferred for version ranges, preconditions, and fixed releases. Reviewed GitHub Advisory Database records are useful but may summarize an upstream report; follow linked project sources for details.
- A CVE and GHSA can name the same report. The main register keeps aliases on one row; it does not inflate the count with duplicate identifiers.
- Several SiYuan, Spring, Grafana, File Browser, and archive reports are follow-up fixes or distinct endpoint/extension variants. They remain separate where the source describes different conditions or an incomplete fix, with the relationship stated.
- One ICEcoder advisory is unreviewed and appears only in the adjacent lead register. Search-result titles and secondary databases do not count as source-verified cases.
- Some advisory sources say the issue was tested or verified. That is the advisories' claim, not a runtime test performed by this corpus project.

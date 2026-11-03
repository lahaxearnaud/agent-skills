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
- [Symfony 5.x Filesystem documentation](https://symfony.com/doc/5.x/components/filesystem.html) — versioned `Path` behavior; the class was introduced in Symfony 5.4, and this page documents canonicalization and `isBasePath()` examples for the 5.x line.
- [PHP `realpath()` manual](https://www.php.net/manual/en/function.realpath.php) — resolves `.`/`..` and symlinks for existing paths and returns `false` on failure; code must handle failure and consider check-to-use races.
- [PHP `ZipArchive::extractTo()` manual](https://www.php.net/manual/en/ziparchive.extractto.php) — behavior of PHP ZIP extraction; verify the PHP/zip version and target directory state rather than assuming all extraction libraries behave the same.
- [PHP 5 changelog](https://www.php.net/ChangeLog-5.php), [PHP 7 changelog](https://www.php.net/ChangeLog-7.php), [PHP 8 changelog](https://www.php.net/ChangeLog-8.php), [CVE-2021-21706 record](https://www.cve.org/CVERecord?id=CVE-2021-21706), and [PECL `zip` 1.19.5 Windows package](https://pecl.php.net/package/zip/1.19.5/windows) — official upstream fix releases, package-level extension fix, and Windows-specific affected version lines for the ZIP extraction issues. The corresponding PHP issue pages are linked from adjacent case records.
- [PHP bug #70350 / CVE-2014-9767](https://bugs.php.net/bug.php?id=70350), [bug #81420 / CVE-2021-21706](https://bugs.php.net/bug.php?id=81420), and [bug #73910](https://bugs.php.net/bug.php?id=73910) — PHP's own issue records document distinct historical `ZipArchive::extractTo()` path behaviors, platform/argument conditions, and fixes. Exact release mapping remains unknown where the issue does not state it.
- [Node.js `path` API](https://nodejs.org/api/path.html) — platform-specific path resolution, normalization, and relative-path operations; verify the exact API and platform used by the application.
- [Java `SecureDirectoryStream`](https://docs.oracle.com/en/java/javase/27/docs/api/java.base/java/nio/file/SecureDirectoryStream.html) — descriptor-relative operations intended for security-sensitive race-resistant directory traversal where supported.
- [Python `zipfile` documentation](https://docs.python.org/3/library/zipfile.html) — extraction APIs versus caller-managed paths such as `ZipInfo`; the documented safety behavior is API-specific and version-dependent.

## Source-quality notes

- Vendor/project advisories are preferred for version ranges, preconditions, and fixed releases. Reviewed GitHub Advisory Database records are useful but may summarize an upstream report; follow linked project sources for details.
- A CVE and GHSA can name the same report. The main register keeps aliases on one row; it does not inflate the count with duplicate identifiers.
- Several SiYuan, Spring, Grafana, File Browser, and archive reports are follow-up fixes or distinct endpoint/extension variants. They remain separate where the source describes different conditions or an incomplete fix, with the relationship stated.
- One ICEcoder advisory is unreviewed and appears only in the adjacent lead register. Search-result titles and secondary databases do not count as source-verified cases.
- Some advisory sources say the issue was tested or verified. That is the advisories' claim, not a runtime test performed by this corpus project.

# Contexts, sanitization, and protections

## Decision by destination

| Final destination | Check and suggested remediation |
|---|---|
| HTML text / quoted ordinary attribute | Effective HTML autoescaping or a correct HTML encoder, with quotes retained; do not apply `raw` to untrusted data. |
| URL attribute / redirect | Parse, validate allowed schemes and, when needed, origin/host/path, then encode for the attribute; distinguish relative URLs, navigation destinations, and script loads. |
| JavaScript in HTML | Avoid generating code; prefer separate JSON transport. Otherwise verify both JS serialization **and** the enclosing HTML document, including script delimiters. HTML escaping alone is insufficient. |
| Rich HTML / SVG | Identify the sanitizer, version, configuration, accepted context, and all transformations after sanitization. Favor the minimum policy or isolation when active content is required. |
| Vue | Text interpolation is normally escaped; `v-html` and HTML render functions are sinks. `:href` requires URL validation. Do not compile a controlled template or mount onto pre-existing untrusted DOM. |
| Standalone document / `srcdoc` | Determine origin, MIME type, disposition, sandbox, CSP, and navigation. SVG used as an image and SVG opened as a document are not equivalent. |

## Conditional guarantees

- **Twig:** confirm the template's autoescape strategy, exception blocks, macros/includes, `raw`, `Markup`, `is_safe`, and custom filter `pre_escape`. `is_safe` is a declaration to verify, not proof. HTML autoescaping does not validate a URL scheme.
- **PHP:** `htmlspecialchars` with appropriate flags and charset protects some HTML contexts, not all JS, URL, CSS, or unquoted HTML contexts. Consider the PHP version and context; do not recommend code concatenation.
- **Sanitizers:** for `DOMPurify`, Symfony HtmlSanitizer, or equivalents, verify version, options, allowlist, hooks, and input/output types. Assess sanitization after the last HTML-producing transformation; untrusted concatenation after sanitization is not covered. Do not assume a permissive configuration is safe. For an advisory, verify the affected range, usage, and fix; dependency presence alone does not prove the flow.
- **URLs:** searching for the `http` substring or HTML encoding is not scheme validation. Compare the value actually used after parsing; a valid HTTPS URL can still lead to an untrusted site.
- **CSP:** inspect visible headers/configuration and the actual applicable value when available; distinguish `Report-Only`, `script-src`, `script-src-elem`, `script-src-attr`, nonce/hash, `unsafe-inline`, `unsafe-eval`, and `strict-dynamic`. Multiple policies apply together. CSP can block vectors without fixing injection; code injected into a legitimate nonce-bearing script may be authorized. Do not guess an unknown final header.
- **Trusted Types:** inspect effective enforcement, browsers, and `createPolicy`/default policies. A policy that returns its input unchanged does not demonstrate safety; sink coverage and browser support are limited.
- **Cookies and session:** `HttpOnly` limits direct access to some cookies without automatically preventing authenticated actions. Scope depends on the origin and actual controls. Do not claim cookie theft when cookie properties are unknown.
- **WAF/proxy:** neither proves safety nor vulnerability. Rules, normalization, exceptions, origin paths, and body limits may be outside the repository. Document uncertainty without suggesting probes against the application.

Sources: [Twig escape](https://twig.symfony.com/doc/3.x/filters/escape.html), [Vue security](https://vuejs.org/guide/best-practices/security), [Symfony HtmlSanitizer](https://symfony.com/doc/current/html_sanitizer.html), [OWASP XSS](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html), [MDN CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP). Start with the paraphrased [offline source notes](offline-sources.md). When online, consult a suitable primary source only if a material version, configuration, or browser detail is missing; otherwise the bundled notes are sufficient. Never transmit private reviewed code to an external service.

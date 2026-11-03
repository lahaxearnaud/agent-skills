# Destination policy, frameworks, OAuth, and CSP

## Safe destination policies

Prefer a **fixed internal route identifier** mapped to server-defined route names/paths. It avoids accepting a general URL for a “return to” feature. Verify that the map is fixed and that the route itself cannot redirect externally.

If arbitrary same-origin paths are a product requirement, resolve and validate them at the trust boundary using a parser whose semantics match the final consumer. Compare the canonical origin (scheme, host, effective port) to a fixed expected origin, then emit the canonical checked value. Where practical, reduce it to a canonical relative path. Do not validate one string and later decode, normalize, prepend a host, concatenate, store/retrieve, or parse it differently before the sink.

For an external OAuth redirect URI, compare the supplied URI to a URI registered for that client using the applicable protocol rule. OAuth 2.0 Security Best Current Practice (RFC 9700) requires exact string matching for registered redirect URIs, with the stated loopback-port exception for native apps. Do not replace this with host suffix checks, broad wildcards, or “same domain” logic. Validate before every branch that returns a redirect, including errors, denial, unsupported response types, callback overrides, and logout.

## Common checks that fail

- `startsWith('/')`, “starts with our domain”, regular expressions, or stripping a scheme/host do not establish same-origin navigation. Scheme-relative URLs can begin with `/`; browser and framework parsers can normalize slashes, backslashes, dot segments, and encoded characters after a check.
- `parse_url`, a generic “local URL” helper, or a sanitizer is not automatically an authorization policy. Read its semantics and version, inspect the returned value, and compare it with the final consumer's interpretation.
- Comparing only a host suffix can accept a different host. Compare parsed components against an exact allowlist and decide explicitly which scheme and port are allowed.
- A valid URL syntax check does not prove the destination is trusted. Encoding/escaping prevents syntax injection in a context; it does not authorize an external origin.
- `Referer`, `Host`, or forwarded headers are not trustworthy because they are headers. Validate the proxy boundary and configured host list; do not infer ingress behavior from application code alone.
- “Relative” is not a security property unless the exact browser/server resolution is established. Track all parsing, decoding, path joining, and framework transformations in order.

## PHP, Symfony, and Twig

- Trace request data through controller/service/auth handlers to `header('Location: ...')`, `RedirectResponse`, or direct response headers. Confirm that the response status and header are reachable; inspect framework and PHP versions where helpers may normalize or reject values.
- Treat `RedirectResponse` as a sink, not a validator. Look for a fixed-route choice or explicit policy before it. Do not assume Symfony's response behavior from current documentation when the application may use another installed version or a wrapper.
- Symfony `path()`/`url()` and Twig route helpers generate route URLs. Their output alone is not an open redirect. Trace to a redirect/navigation sink; review route requirements and any raw-regex alternatives when generated paths are attacker-influenced.
- Twig autoescaping is unrelated to whether a destination is an allowed origin. A correctly escaped URL can still navigate to an untrusted site.
- `filter_var(..., FILTER_VALIDATE_URL)` or `parse_url()` can help parse/syntax-check but do not establish that the destination is safe for the application's redirect policy.

## JavaScript and Vue

- Trace `URLSearchParams`, `location.search`/`hash`, `document.referrer`, route state, storage, and API values through every transformation into a navigation API.
- Vue Router can take strings or route locations. A fixed named-route map is easier to reason about than passing a request value as a path. Check router major version, history/base configuration, route guards, and any wrapper before claiming how external-looking strings are resolved.
- Vue Router issue [#3946](https://github.com/vuejs/vue-router/issues/3946) is an issue-reporter lead for Vue 2.7.16 / Router 3.6.5 in HTML5 history mode with an empty/root base. It is not a maintainer advisory and does not establish behavior for all Vue Router versions. Treat similar code as a candidate until the installed implementation and actual code path are inspected.
- Nuxt `navigateTo()`/`reloadNuxtApp()` and other framework helpers must be checked by exact version, server/client mode, and options. A wrapper name or an `external` option does not by itself prove a validation guarantee.

## OAuth and identity

Trace the complete flow from client selection and registered redirect URIs through state/session creation, consent, error handling, callback, and code/token delivery. Establish which party controls each value and how a victim is induced into the flow. Base64 is encoding, not integrity. A token/code leak or account takeover is a conditional chain: state which validation, client configuration, victim interaction, and code-exchange protections are present or unknown.

## CSP limits

CSP is useful defense in depth, but do not treat `default-src` or `script-src` as a general allowlist for top-level HTTP(S) navigation. `form-action` constrains form submissions; `frame-ancestors` controls embedding. A restrictive script policy may affect some script-execution outcomes but does not fix an ordinary external redirect. Inspect the effective policy only to qualify a demonstrated chain, and do not claim that CSP prevents an open redirect. See the [CSP Level 3 specification](https://www.w3.org/TR/CSP3/) and [MDN `default-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/default-src).

## Primary references

- [OWASP Unvalidated Redirects and Forwards Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)
- [MITRE CWE-601](https://cwe.mitre.org/data/definitions/601.html)
- [RFC 9110 §10.2.2 — `Location`](https://datatracker.ietf.org/doc/html/rfc9110#section-10.2.2)
- [WHATWG URL Standard](https://url.spec.whatwg.org/)
- [RFC 9700 — OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/rfc9700)
- [Symfony HttpFoundation](https://symfony.com/doc/current/components/http_foundation.html) and [PHP `header()`](https://www.php.net/manual/en/function.header.php)
- [Vue Router navigation](https://router.vuejs.org/guide/essentials/navigation), [MDN `Location.assign()`](https://developer.mozilla.org/en-US/docs/Web/API/Location/assign), and [MDN `Window.location`](https://developer.mozilla.org/en-US/docs/Web/API/Window/location)

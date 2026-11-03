# Sources and automatic-navigation sinks

This is a search guide, not an exhaustive API list. Search wrappers, project helpers, response objects, and indirect callers as well as the names below. A source and sink found by text search do not prove that the value is connected or reachable.

## Sources to trace

### Server and request state

- Query, form, JSON, route, GraphQL, and callback fields such as `next`, `return`, `returnUrl`, `return_to`, `redirect`, `redirect_uri`, `from`, `continue`, `target`, `url`, `destination`, and `nextPage`.
- `Referer`, `Host`, `Forwarded`, `X-Forwarded-Host`, `X-Forwarded-Prefix`, and absolute-URL inputs. Treat these as attacker-influenced until trusted-proxy and allowed-host configuration is established for the relevant ingress.
- Cookies, session/flash state, database fields, OAuth `state`, queued jobs, and saved form state. Trace both the write and later read; prior persistence does not make a value trusted.

### Browser and SPA state

- `location.search`, `location.hash`, `document.referrer`, `URLSearchParams`, `window.name`, `postMessage`, local/session storage, route query/params, component props, stores, and API responses.
- Server-rendered values crossing Twig/HTML/JSON into JavaScript, then reaching a navigation helper. HTML escaping or JSON serialization does not itself define an allowed destination.

## Server-side sinks

- **PHP:** `header('Location: ...')`, direct `Location` response headers, framework response objects, and helpers that set redirect status/target.
- **Symfony:** `RedirectResponse`, controller `redirect()` helpers, authentication success/failure handlers, logout targets, locale/currency switches, and wrappers. Treat the API as a sink; inspect the installed `symfony/http-foundation` version and the exact checked value. Symfony Routing's `path()` and `url()` generate URLs; they become redirect sinks only if their result reaches automatic navigation.
- **Other PHP frameworks:** login/logout redirect helpers, “back” helpers using `Referer`, and `redirect()->away()`/external redirect methods. Confirm the framework's version and behavior from source or authoritative documentation.
- **Java/JVM and servers:** servlet `sendRedirect`, Spring `redirect:` view names and controller helpers, auth handlers, server valves, default-servlet canonicalization, and proxy/middleware redirects.
- **Other server stacks:** Flask/Django `redirect`, Express `res.redirect`/`res.location`, framework redirect responses, and auth callback handlers. Read the exact dependency version and wrapper implementation when behavior matters.

## Client-side sinks

- Assignments to `window.location`, `location.href`, `location.assign()`, `location.replace()`, `window.open()`, and `window.navigation.navigate()`.
- Vue Router `router.push()`/`replace()`, `<router-link>` and route guards; Nuxt `navigateTo()` and `reloadNuxtApp({ path })`.
- React Router `redirect()`, `<Link>`, `useNavigate()`, and loader/action return values; Next.js redirect configuration and `redirect()`; Qwik City redirect helpers.
- HTML meta refresh when an automatically rendered page sends the browser elsewhere. Classify it as HTML-driven navigation and inspect whether it is a redirect response, XSS, or a separate document-navigation issue.

## Distinguish these behaviors

- A click-only `<a href="...">` is not automatically a redirect. It may be an attacker-controlled external link, a separate trust issue, or a dangerous URL scheme.
- Generating an absolute URL with a request host or a Twig URL helper is not enough: trace it into an automatic-navigation sink.
- An external HTTP(S) navigation is distinct from `javascript:` or other executable URL schemes. If script execution is possible, classify and report the XSS/unsafe-scheme chain separately.
- A URL used by the server to fetch data may be SSRF rather than a redirect. Do not merge findings solely because a parameter is named `url`.

For framework navigation behavior, use [offline source notes](offline-sources.md) first. If connected and a missing version-specific behavior could change whether navigation is external or automatic, consult the exact primary documentation or implementation; otherwise inspect source already present in the repository or state the limitation. Never send private project code externally.

## Quick source search

Adapt excluded/generated paths to the repository. Search results are leads, not findings; `rg` respects ignore rules, so check whether hidden or ignored source/configuration is in scope.

```bash
rg -n -S --glob '!vendor/**' --glob '!node_modules/**' --glob '!dist/**' \
  'Location|RedirectResponse|sendRedirect|redirectTo|redirect\(|navigateTo|reloadNuxtApp|window\.location|location\.(assign|replace)|window\.open|router\.(push|replace)|router-link|redirect_uri|returnUrl|return_to|nextPage|HTTP_REFERER|HTTP_HOST|X-Forwarded-Host|X-Forwarded-Prefix' .
```

Search project wrappers and call sites manually after the first pass. Also trace source fields into helper arguments, returned response objects, route config, template-generated URLs, and persisted state; name-based matches cannot establish data flow or reachability.

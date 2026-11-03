# Reporting and example decisions

## Evidence states

- **Statically established flow:** visible code supports attacker control, path through checks and transformations, reachable automatic-navigation sink, and an external destination under the demonstrated conditions. This is still not observed runtime exploitation.
- **Candidate:** a plausible source or sink exists, but a connection, effective policy, version behavior, route/configuration, or actor capability is missing. State exactly what is unknown and what source to inspect next.
- **Not established for this path:** visible evidence shows a fixed internal choice, constant destination, unreachable path, or no automatic-navigation sink. Say why and avoid generalizing beyond the reviewed path.

Use the weaker status if browser/server parser behavior, dependency version, proxy rewriting, or route reachability is necessary but unavailable. A raw string check is evidence about code, not proof of how every consumer normalizes the value.

## Finding template

1. **Title and status:** server redirect or client-side automatic navigation; statically established flow or candidate.
2. **Source and actor:** file:line, who controls it, privilege and interaction required.
3. **Path:** file:line for transformations, allowlist/validation, persistence and reads; state if any edge is unknown.
4. **Sink:** exact response header/helper or browser navigation API and file:line; explain how the value becomes an external authority.
5. **Conditions:** framework/dependency version, route and auth configuration, SSR/client mode, host/proxy assumptions, browser/router semantics, and user interaction. Mark unavailable conditions unknown.
6. **Impact:** phishing or other source-supported outcome; describe OAuth/code/token or account-takeover chains only with their prerequisites. No severity without the repository's rubric and evidenced exposure/impact.
7. **Remediation:** prefer a fixed route map; otherwise enforce a strict origin/registered-URI policy and pass the checked canonical result to the sink. Include alternative branches.
8. **Coverage and limits:** files, configuration, and tools actually reviewed; missing surfaces; no claim of runtime testing or exhaustive absence.

## Mini verification grid

| Code pattern | Correct static conclusion |
|---|---|
| `$_GET['next']` flows to `header('Location: '.$next)` after a slash-prefix condition | Candidate or established based on visible reachability and consumer behavior; inspect scheme-relative and normalization semantics. |
| Symfony controller passes request data into `RedirectResponse` | Sink identified; check installed version and preceding policy. Do not label the helper intrinsically unsafe or safe. |
| Twig `path()` output becomes an `<a href>` requiring a click | External link or URL-generation question, not an automatic open redirect by itself. |
| Vue query value is passed to `router.replace(value)` | Candidate until route/router version and behavior establish whether it can leave the origin; trace wrapper and guard. |
| Vue `router.replace({ name: allowed })` where `allowed` comes from a fixed server-defined map | No external redirect is established on this path; inspect whether route registration or map is actually mutable. |
| `Referer` is saved in session and redirected to after login | Trace both requests and the header trust boundary; persistence does not validate the value. |
| OAuth `redirect_uri` reaches an error branch before client validation | Review every response branch; exact registration matching is required by RFC 9700. A title or grep fragment does not prove code theft. |
| CSP has `default-src 'self'; script-src 'self'` | This does not generally block a server `Location` or normal top-level HTTPS navigation. |
| Destination becomes `javascript:` and may execute script | Analyze as an unsafe-scheme/XSS chain as well as any navigation behavior; do not collapse it into ordinary HTTP open redirect. |

## Sourced patterns to compare

These examples guide variant search; they do not prove a matching project is vulnerable.

| Pattern | Public case | Static question |
|---|---|---|
| Browser/server URL parser differential | [Symfony HttpFoundation CVE-2024-50345](https://symfony.com/cve-2024-50345) | Does a server-side URL check accept a value the browser interprets with another authority? |
| Request value stored then used after an action | [Snipe-IT GHSA-mghp-5cq4-v6mg](https://github.com/grokability/snipe-it/security/advisories/GHSA-mghp-5cq4-v6mg) | Are session writes and later redirect reads both in scope? |
| `Referer` used by Symfony-based workflow | [Sylius GHSA-9ffx-f77r-756w](https://github.com/Sylius/Sylius/security/advisories/GHSA-9ffx-f77r-756w) | Which locale/currency/auth paths trust the header, and who can reach them? |
| Login destination and slash/backslash validation | [CakePHP GHSA-hhpq-7wg4-36jm](https://github.com/cakephp/authentication/security/advisories/GHSA-hhpq-7wg4-36jm) | Does validation happen before all normalization and final redirect handling? |
| Twig route generation affected by route regex behavior | [Symfony Routing CVE-2026-45065](https://symfony.com/cve-2026-45065) | Is a generated URL actually sent to an automatic-navigation sink? |
| Vue Router path normalization | [Vue Router issue #3946](https://github.com/vuejs/vue-router/issues/3946) | Does the installed version/config match the reporter's setup? This is an unreviewed issue lead, not a universal rule. |
| SSR `//` check before URL normalization | [Angular GHSA-w739-gvwx-grc3](https://github.com/angular/angular/security/advisories/GHSA-w739-gvwx-grc3) | Is validation performed before the same parser that resolves the final destination? |
| Framework redirect helper accepts protocol-relative path | [React Router GHSA-2j2x-hqr9-3h42](https://github.com/remix-run/react-router/security/advisories/GHSA-2j2x-hqr9-3h42) | Is the application using the affected framework mode/version and passing untrusted data? |
| Route-configuration redirect uses request host | [Next.js GHSA-p9j2-gv94-2wf4](https://github.com/advisories/GHSA-p9j2-gv94-2wf4) | Do config-level redirects interpolate a request-controlled host? Distinguish redirects from rewrites/SSRF. |
| OAuth callback concatenates origin and untrusted path | [Feathers GHSA-ppf9-4ffw-hh4p](https://github.com/feathersjs/feathers/security/advisories/GHSA-ppf9-4ffw-hh4p) | Can an external origin override the intended base, and is code/token delivery part of the chain? |
| OAuth denial branch uses an unvalidated registered URI | [n8n GHSA-f6x8-65q6-j9m9](https://github.com/advisories/GHSA-f6x8-65q6-j9m9) | Are URIs validated before consent, denial, callback, and error paths? |
| URL validation helper has incomplete leading-slash handling | [Redash GHSA-rfgc-hc86-pxrv](https://github.com/getredash/redash/security/advisories/GHSA-rfgc-hc86-pxrv) | Does “remove scheme/host” leave a value the browser treats as a different authority? |
| OAuth validation bypass through unsupported response branch | [Authlib GHSA-w8p2-r796-3vmq](https://github.com/advisories/GHSA-w8p2-r796-3vmq) | Does any early error branch redirect before client and URI validation? |

For additional cases and source notes, use the maintained open redirect corpus when working in the source repository. The installed skill and its bundled examples remain usable without that corpus.

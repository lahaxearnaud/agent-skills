# Published open redirect cases

The entries below are distinct public advisory/CVE records consulted for this corpus. Each summary preserves the source's stated conditions and avoids treating an advisory title as proof of an application-specific exploit. **One advisory can contain multiple sinks**, and related/fix-bypass records are called out rather than silently counted as independent root causes.

## PHP, Symfony, CMS and Java server frameworks

### OR-001 — Symfony HttpFoundation: browser/server URL parsing differential (CVE-2024-50345)

Affected Symfony HttpFoundation releases include `<5.4.46`, `6.0–6.4.13`, and `7.0–7.1.6`. A validator using `Request` can accept a URL containing special characters differently from a browser, then redirect to another domain. The fix rejects invalid characters according to the WHATWG URL rules. **Static signal:** a URL validator parses with Symfony request helpers, while the resulting value reaches `RedirectResponse` or another redirect sink without equivalent browser-compatible validation. [Symfony advisory](https://symfony.com/cve-2024-50345)

### OR-002 — Symfony Routing/Twig: unanchored route-regex alternation generates `//host` (CVE-2026-45065)

Symfony Routing versions before the fixed 5.4.52, 6.4.40, 7.4.12 and 8.0.12 releases could validate a route requirement such as a long `a|b|c` alternation using a pattern whose anchors did not bind every alternative. A parameter containing a matching substring could therefore generate a protocol-relative off-site path through Twig `path()`/`url()` helpers. This is **off-site URL generation**; confirm that the generated value reaches a redirect or browser-navigation sink before reporting an open redirect. [Symfony advisory](https://symfony.com/cve-2026-45065)

### OR-003 — Spring MVC/WebFlux: implicit view mapping interprets `redirect:` (CVE-2026-41844)

An application must configure a `/**` mapping without an explicit view name. Under that configuration, a crafted path can be treated as a view name with the `redirect:` prefix, yielding a 302 to an external host. The important condition is the application's mapping/view setup, not merely the dependency version. [Spring advisory](https://spring.io/security/cve-2026-41844)

### OR-004 — Sylius: locale, currency and impersonation flows trust `Referer` (CVE-2026-31819)

Several Symfony-based redirect paths used the request `Referer` directly: currency switching, locale switching, and admin user impersonation. Public switching routes did not require login; the impersonation route did. The report says the attacker can induce the browser to send an attacker-controlled referrer by linking through an external page. The maintainer fix redirects to a named internal route. [Sylius advisory](https://github.com/Sylius/Sylius/security/advisories/GHSA-9ffx-f77r-756w)

### OR-005 — CakePHP Authentication: backslash bypass in `getLoginRedirect()` (CVE-2026-55590)

The login redirect helper could accept a target whose backslash handling resulted in an attacker-controlled hostname. Affected branches are listed in the advisory; fixes were released in 2.11.1, 3.3.6 and 4.1.1. Trace the redirect query parameter through validation and any later URL normalization. [CakePHP advisory](https://github.com/cakephp/authentication/security/advisories/GHSA-hhpq-7wg4-36jm)

### OR-006 — TYPO3 Core: local-URL sanitizer used as a security decision (CVE-2026-47347)

The advisory warns that applications using `GeneralUtility::sanitizeLocalUrl()` to allow only local targets remain vulnerable when the URL is later used as a redirect after the check. It affects TYPO3 Core across several maintained branches and was fixed in the listed security releases. The advisory does not establish that every call to this helper is vulnerable; inspect the returned value, subsequent transformations, and actual redirect sink. [TYPO3 advisory](https://typo3.org/security/advisory/typo3-core-sa-2026-009)

### OR-007 — Snipe-IT: unvalidated `Referer` persisted in session (CVE-2026-44833)

Before 8.4.1, an HTTP `Referer` value could be stored in a session variable and later used as a redirect destination. The advisory describes the redirect occurring after a user saves an item and lists phishing among the impacts. This is a useful delayed-flow pattern: inspect session writes and later reads, rather than only same-request taint. [Snipe-IT advisory](https://github.com/grokability/snipe-it/security/advisories/GHSA-mghp-5cq4-v6mg)

### OR-008 — Drupal 6: double-decoded `destination` bypasses `drupal_goto()` (CVE-2016-3167)

Drupal 6 before 6.38, when running on PHP before 5.4.7, allowed a double-encoded URL in the `destination` parameter to bypass the `drupal_goto()` redirect protection and send users to arbitrary sites. The case is useful for tracing decode order across PHP and framework code. [Drupal security advisory](https://www.drupal.org/forum/newsletters/security-advisories-for-drupal-core/2016-02-24/drupal-core-critical-multiple)

### OR-009 — WeGIA: `nextPage` reaches `control.php` redirect logic (CVE-2025-24020)

The reported endpoint is `control.php`; the companion vendor advisory identifies the user-controlled `nextPage` parameter and says authenticated users can be sent to arbitrary external URLs. Versions through 3.2.10 are named by the CVE record. Preserve the authentication requirement when triaging reachability. [WeGIA advisory](https://github.com/LabRedesCefetRJ/WeGIA/security/advisories/GHSA-27g8-5q48-xmw6), [NVD record](https://nvd.nist.gov/vuln/detail/CVE-2025-24020)

### OR-010 — CouchCMS: crafted URL accepted by `sanitize_url()` (CVE-2023-41609)

CouchCMS v2.3's `sanitize_url()` parameter is named in the CVE record as the vulnerable surface; a crafted URL can redirect a victim to an arbitrary site. The public record gives limited call-site detail, so use it as a helper/validator lead and inspect the actual implementation before deriving a rule. [NVD record](https://nvd.nist.gov/vuln/detail/CVE-2023-41609)

### OR-011 — PowerCMS: crafted unauthenticated URL redirects externally (CVE-2023-50297)

PowerCMS 4, 5 and 6 series are affected according to the advisory record; a remote unauthenticated user can redirect victims through a specially crafted URL. The brief record does not identify the parameter or sink, so this is evidence for the product and behavior, not a precise static signature. [INCIBE-CERT advisory](https://www.incibe.es/en/incibe-cert/early-warning/vulnerabilities/cve-2023-50297)

### OR-012 — OpenCms Mercury template: unsanitized `URI` parameter (CVE-2023-6380)

OpenCms 14 and 15's Mercury template had an open redirect because the `URI` parameter was not properly sanitized. This is a clear query/path-to-redirect example in a Java CMS template layer. [INCIBE-CERT advisory](https://www.incibe.es/en/incibe-cert/notices/aviso/multiple-vulnerabilities-alkacon-software-opencms), [NVD record](https://nvd.nist.gov/vuln/detail/CVE-2023-6380)

### OR-013 — CDeX: crafted URL redirects to an arbitrary site (CVE-2024-2465)

CERT Polska coordinated disclosure for the CDeX application. The public description says versions through 5.7.1 accept a specially crafted URL that redirects users to arbitrary sites; endpoint and code-level details are sparse in the public summary. [CERT Polska advisory](https://cert.pl/en/posts/2024/03/CVE-2024-2463/)

### OR-014 — Umbraco Backoffice: authenticated endpoint bypasses redirect protection (CVE-2024-34071)

The vulnerable endpoint is protected by Backoffice authentication, so the issue requires a signed-in user. This record is useful for assessing authorization and reachability as part of a static finding; do not report it as unauthenticated. [Umbraco advisory](https://github.com/umbraco/Umbraco-CMS/security/advisories/GHSA-j74q-mv2c-rxmp)

### OR-015 — Umbraco Surface Controllers: query-derived Razor `RedirectUrl` (CVE-2026-46616)

Member-related Surface Controllers failed to validate redirect URLs. Razor templates deriving `RedirectUrl` from untrusted query parameters could therefore redirect externally. The advisory names `UmbLoginStatusController`, `UmbProfileController`, and `UmbRegisterController`; it recommends passing a concrete trusted route value. [Umbraco advisory](https://github.com/advisories/GHSA-2qjj-h6wp-c7h7)

### OR-016 — Apache Shiro: `Form` authentication open redirect (CVE-2023-46750)

The reported condition is use of Shiro's `Form` authentication feature. The public record identifies the feature and vulnerability class but offers little detail about the exact redirect parameter; inspect the configured authentication flow and the framework version before making a code-level claim. [Apache Shiro advisory](https://github.com/advisories/GHSA-hhw5-c326-822h)

## JavaScript, Vue and other client/server frameworks

### OR-017 — Next.js: static `pages/_error.js` and specially encoded paths (CVE-2021-37699)

Next.js 11.0.0–11.0.1 was affected when `pages/_error.js` was statically generated without `getInitialProps`. Specially encoded request paths could trigger an external redirect. The case depends on the page generation mode and should not be generalized to every Next.js route. [Next.js release notes](https://github.com/vercel/next.js/releases/tag/v11.1.0), [NVD record](https://nvd.nist.gov/vuln/detail/CVE-2021-37699)

### OR-018 — Next.js: request-derived hostname in configured redirects/rewrites (CVE-2026-64645)

If `redirects()` or `rewrites()` builds its external destination hostname from a request-controlled path or `has` capture, a redirect rule can send users to an arbitrary host. The analogous rewrite case is SSRF, not a browser open redirect, and must be reported separately. [Next.js advisory](https://github.com/advisories/GHSA-p9j2-gv94-2wf4)

### OR-019 — React Router: same-origin redirect helper accepts `//` path (CVE-2026-40181)

Certain URLs passed to `redirect()` can be interpreted as protocol-relative external destinations if application validation is insufficient. The advisory excludes Declarative Mode (`<BrowserRouter>`); its affected framework/data contexts and version ranges are documented in the source. [React Router advisory](https://github.com/remix-run/react-router/security/advisories/GHSA-2j2x-hqr9-3h42)

### OR-020 — React Router: untrusted loader/action navigation can escalate to JS execution (CVE-2026-22029)

Untrusted redirect paths in Framework Mode, Data Mode, or unstable RSC modes could lead to unsafe client-side navigation and unintended JavaScript execution. This is an **open-navigation-to-XSS chain**, not a reason to label every open redirect as XSS. Declarative `<BrowserRouter>` is excluded by the advisory. [React Router advisory](https://github.com/advisories/GHSA-2w69-qvjg-hvjx)

### OR-021 — React Router: backslash bypass of prior navigation fix (CVE-2026-53669)

This follow-up says attacker-supplied paths passed to `<Link>` and `useNavigate` could still cause unexpected external navigation after an earlier fix. It is best used as a patch-regression case and should be linked to CVE-2025-68470 in any analysis. [React Router advisory](https://github.com/advisories/GHSA-wrjc-x8rr-h8h6)

### OR-022 — Angular SSR: dot-segment normalization after a raw `//` check (GHSA-w739-gvwx-grc3)

Only SSR is affected. Angular checked a raw URL for a leading `//` before WHATWG URL normalization; paths containing a dot segment followed by slashes could normalize to a protocol-relative pathname and be emitted in a `Location` response. Client-only SPA operation is outside this advisory's scope. [Angular advisory](https://github.com/angular/angular/security/advisories/GHSA-w739-gvwx-grc3)

### OR-023 — Angular SSR: `X-Forwarded-Prefix` strips one slash only (CVE-2026-27738)

Requires SSR behind a proxy that forwards `X-Forwarded-Prefix` into application redirect construction. The implementation stripped only one leading slash; a value beginning with three left a `//host` destination in `Location`. This is also a trust-boundary/configuration case: establish whether the deployment trusts and sanitizes that header. [Angular advisory](https://github.com/advisories/GHSA-xh43-g2fq-wjrj)

### OR-024 — Angular SSR: encoded dot segments in trusted proxy prefix (CVE-2026-44437)

The `X-Forwarded-Prefix` check did not account for encoded dot segments that were later decoded/used. Exploitation requires SSR to trust the header and a proxy that forwards it without sanitization; the advisory also describes request steering. [Angular advisory](https://github.com/advisories/GHSA-69xr-m8h6-h664)

### OR-025 — Nuxt: `navigateTo`/`reloadNuxtApp` URL handling (GHSA-c9cv-mq2m-ppp3)

One advisory groups three public-API weaknesses: SSR `navigateTo()` checks raw paths before WHATWG normalization, so dot-segment paths may become `//host` in `Location` and a meta-refresh body; `reloadNuxtApp({path})` can accept protocol-relative destinations; and the `navigateTo({open})` client API has a script-scheme/XSS concern. Count this as **one advisory**, with multiple subfindings. The exact API and SSR/client context are essential. [Nuxt advisory](https://github.com/nuxt/nuxt/security/advisories/GHSA-c9cv-mq2m-ppp3)

### OR-026 — Express: malformed URL encoding crosses allowlist/redirect parser boundaries (CVE-2024-29041)

Express versions before 4.19.2 and the affected 5.0 prereleases could encode malformed URLs for `res.location()`/`res.redirect()` in a way that disagreed with application allowlist validation. The application must be redirecting a user-provided URL and must rely on an allowlist susceptible to that parsing mismatch. [Express advisory](https://github.com/advisories/GHSA-rv95-896h-c2vc)

### OR-027 — Waku: `unstable_redirect()` reflects arbitrary strings to `Location` (CVE-2026-49456)

The server helper accepted an arbitrary string and reflected it into the HTTP `Location` header without URL validation, scheme restriction, or path-only enforcement. An application is vulnerable when user-controlled data reaches that helper. Fixed in 1.0.0-beta.1. [Waku advisory](https://github.com/advisories/GHSA-43fc-v873-qw85)

### OR-028 — Qwik City: `fixTrailingSlash` emits a protocol-relative redirect (CVE-2026-25149)

The `fixTrailingSlash` redirect logic could construct an external `Location` from a path when the catch-all runtime did not normalize it in the expected way; the report discusses Bun deployments. This is conditional on adapter/runtime and route handling, not a blanket claim about all Qwik apps. [Qwik advisory](https://github.com/QwikDev/qwik/security/advisories/GHSA-92j7-wgmg-f32m)

### OR-029 — WebOb: request-URI plus `urljoin` normalization (CVE-2024-42353)

WebOb normalized a `Location` value relative to the request URI using `urllib.parse.urljoin`; a request URI beginning with a double-slash path could change the effective authority. The first fix encoded a leading slash pair. [WebOb advisory](https://github.com/Pylons/webob/security/advisories/GHSA-mg3v-6m49-jhp3)

### OR-030 — WebOb: Python 3.10 control-character stripping bypasses prior fix (CVE-2026-44889)

This follow-up explains that `urlsplit` strips ASCII tab, carriage return and newline characters; a slash-delimited target can therefore become a protocol-relative host after the previous mitigation. Requires the affected WebOb code and Python URL parsing behavior. Patched in WebOb 1.8.10. Treat it as a **fix-bypass in the same root-cause family** as OR-029. [WebOb advisory](https://github.com/advisories/GHSA-fh3h-vg37-cc95)

### OR-031 — Authlib: invalid `response_type` redirects before OAuth client validation (CVE-2026-41479)

In affected Authlib versions, the unsupported-`response_type` error branch used a supplied `redirect_uri` before client lookup and redirect-URI validation. The advisory describes an unauthenticated 302 without a valid client registration. [Authlib advisory](https://github.com/advisories/GHSA-w8p2-r796-3vmq)

### OR-032 — Spring Framework: `UriComponentsBuilder` host-validation parser differential (CVE-2024-22243 / CVE-2024-22259)

Applications using `UriComponentsBuilder` to parse an external URL (for example, a query parameter), validating the parsed host, and then using the URL may be vulnerable to an open redirect or SSRF. The two CVEs are different inputs for the same underlying issue and are represented **once** here. [Spring CVE-2024-22259 advisory](https://github.com/advisories/GHSA-hgjh-9rj2-g67j), [Spring CVE-2024-22243 advisory](https://github.com/advisories/GHSA-ccgv-vj62-xf9h)

### OR-033 — django-allauth: SAML IdP-initiated SSO redirect (CVE-2026-27982)

Versions before 65.14.1 were affected when SAML IdP-initiated SSO was enabled; it is disabled by default. A crafted URL could redirect to an arbitrary external site. Preserve that feature flag as a required precondition. [django-allauth advisory](https://github.com/advisories/GHSA-2jpr-83rg-v67j)

### OR-034 — Flask-AppBuilder: untrusted HTTP `Host` influences redirect (CVE-2025-32962)

Before 4.6.2, an unauthenticated actor could manipulate the Host header to trigger an open redirect. The fix added `FAB_SAFE_REDIRECT_HOSTS`, an explicit trusted-host setting. Inspect proxy host handling and any absolute-URL generation that incorporates request host data. [Flask-AppBuilder advisory](https://github.com/advisories/GHSA-99pm-ch96-ccp2)

### OR-035 — Flask-Security-Too: `next` login target validation (CVE-2021-32618)

The post-login flow honors `?next=` and attempts to allow only relative URLs or URLs with the same network location as the request. The advisory reports an open redirect in this validation path; the exact malformed input is not stated in the short impact section. Inspect the actual validator and patch rather than inferring a bypass string from the title. [Flask-Security advisory](https://github.com/advisories/GHSA-6qmf-fj6m-686c)

### OR-036 — Flask-Security: multiple-backslash bypass in login/logout redirect (CVE-2021-23385)

The `get_post_logout_redirect` and `get_post_login_redirect` functions could be bypassed with multiple backslashes. The issue is exploitable only with a WSGI server other than Werkzeug, or when Werkzeug's default `autocorrect_location_header` behavior is disabled. This demonstrates that the framework code and response-normalization server both affect reachability. [Flask-Security advisory](https://github.com/advisories/GHSA-cg8c-gc2j-2wf7)

### OR-037 — pyLoad: login redirect helper uses flawed `is_safe_url` validation (CVE-2024-24808)

The login flow calls `get_redirect_url`; the advisory identifies incorrect validation of input values in that helper and a fix in `0.5.0b3.dev79`. Use it as a validator-to-sink case, but consult the patch for exact transformations before writing a signature. [pyLoad advisory](https://github.com/pyload/pyload/security/advisories/GHSA-g3cm-qg2v-2hj5)

### OR-038 — web2py: specially crafted URL redirects to arbitrary site (CVE-2026-25198)

The advisory describes affected web2py releases through `2.27.1-stable+timestamp.2023.11.16.08.03.57` and phishing via a specially crafted URL. It does not provide a precise handler in its summary, so treat it as a published product case with limited code-level evidence. [web2py advisory](https://github.com/advisories/GHSA-rf8c-3f5p-xv45)

### OR-039 — Jupyter Server: open redirect when `base_url` has no prefix (CVE-2020-26275)

Jupyter Server before 1.1.1 was affected when run without a `base_url` prefix. A crafted link to a known server could appear to stay on the trusted host but send the browser elsewhere. The advisory notes that the related Notebook issue was separately fixed upstream. [Jupyter Server advisory](https://github.com/advisories/GHSA-9f66-54xg-pc2c)

### OR-040 — Jupyter Server: login redirect after authentication (CVE-2023-39968)

Before 2.7.2, a malicious login link could redirect a successfully authenticated or already logged-in user to an arbitrary site instead of a Jupyter Server URL. The advisory credits a report through the project's bug bounty/Intigriti process. This is an auth-flow and trusted-hostname chaining example. [Jupyter Server advisory](https://github.com/advisories/GHSA-r726-vmfq-j9j3)

### OR-041 — Jupyter Server: unvalidated `next` query parameter (CVE-2025-61669)

The login handler accepts a `next` query parameter; the source identifies a direct reference to `jupyter_server/auth/login.py`. Publicly served Jupyter deployments are a particular phishing context. Inspect the exact login handler and patched version before mapping the issue to another fork. [Jupyter Server advisory](https://github.com/advisories/GHSA-qh7q-6qm3-653w)

### OR-042 — JupyterHub: login redirect bypasses an internal restriction (CVE-2026-33709)

An attacker can construct a link that takes a victim to the JupyterHub login page and then redirects them to an external host rather than a JupyterHub page. Fixed in 5.4.4; the source suggests filtering `Location` at the reverse proxy as a workaround. [JupyterHub advisory](https://github.com/jupyterhub/jupyterhub/security/advisories/GHSA-3vff-hjqv-m7h8)

### OR-043 — Jenkins: `from` parameter after servlet-container login (CVE-2026-53440)

When the `Delegate to servlet container` security realm is used, affected Jenkins releases did not ensure that the `from` value was safe before redirecting after login. The report attributes phishing impact; the auth realm is a necessary condition. [Jenkins advisory](https://www.jenkins.io/security/advisory/2026-06-10/#SECURITY-3721)

### OR-044 — Apache Tomcat: LoadBalancerDrainingValve redirect (CVE-2026-25854)

The advisory identifies an open redirect in Tomcat's `LoadBalancerDrainingValve` and lists affected 8.5, 9.0, 10.1 and 11.0 ranges. A static review should check whether the application enables/configures this valve and which request-derived destination values it uses. [Tomcat advisory](https://github.com/advisories/GHSA-9m3c-qcxr-9x87)

### OR-045 — Apache Tomcat: FORM authentication redirect in the ROOT app (CVE-2023-41080)

The issue affects Tomcat's FORM authentication feature and is limited by the advisory to the ROOT (default) web application. This is a distinct authentication-flow case from the LoadBalancerDrainingValve issue. [Tomcat advisory](https://github.com/advisories/GHSA-q3mw-pvr8-9ggc)

### OR-046 — Apache Tomcat: directory slash redirect can be redirected externally (CVE-2018-11784)

When the default servlet redirects a request such as `/foo` to `/foo/`, specially crafted URLs could cause the redirect to use an attacker-chosen URI. Affected Tomcat releases include 7.0, 8.5 and 9.0 pre-fix ranges. This is a server-generated canonicalization redirect, not an application-written `sendRedirect` call. [Tomcat advisory](https://github.com/advisories/GHSA-5q99-f34m-67gc)

### OR-047 — Payara: Servlet implementation redirect access to libraries (CVE-2023-41699)

The CVE record classifies a URL redirection weakness in Payara Server, Micro and Embedded Servlet Implementation modules, with affected version ranges in 4.x, 5.x and 6.x. The public summary does not explain the exact parameter or call path; retain that limitation and inspect the release fix before deriving code patterns. [GitHub Advisory Database record](https://github.com/advisories/GHSA-q42q-53wf-q55x)

## Identity, OAuth and application workflows

### OR-048 — Feathers OAuth: callback concatenates origin and untrusted redirect (CVE-2026-27191)

The `redirect` query parameter is appended to a base origin without validation and persisted through the OAuth callback flow. The advisory attributes authorization-code/access-token leakage and account takeover. This is a composition bug: string concatenation changes URL authority semantics, so a prefix check alone is insufficient. [Feathers advisory](https://github.com/feathersjs/feathers/security/advisories/GHSA-ppf9-4ffw-hh4p)

### OR-049 — AdonisJS: `response.redirect().back()` trusts `Referer` (CVE-2026-40255)

The helper reads the incoming `Referer` header and redirects to it without validating the host. The advisory says an attacker may induce the header through an external link/page and identifies `response.redirect().back()` and `response.redirect('back')` as affected uses. [AdonisJS advisory](https://github.com/adonisjs/http-server/security/advisories/GHSA-6qvv-pj99-48qm)

### OR-050 — n8n MCP OAuth: unauthenticated client registration plus consent denial (CVE-2026-42230)

The unauthenticated `/mcp-oauth/register` endpoint accepted arbitrary `redirect_uri` values. When a victim denies the consent dialog, `handleDeny` redirects to that URI without validation. The exploit path therefore needs both client registration and a victim interaction with the consent screen. [n8n advisory](https://github.com/advisories/GHSA-f6x8-65q6-j9m9)

### OR-051 — WireGuard Portal v2: OAuth `return` value (GHSA-grh9-37g7-53mj)

Before 2.1.2, the OAuth login initialization endpoint insufficiently validated its return parameter, allowing an external redirect after authentication. This is a compact example of an auth-state destination that persists across an external identity-provider round trip. [WireGuard Portal advisory](https://github.com/advisories/GHSA-grh9-37g7-53mj)

### OR-052 — hsweb-framework: OAuth2 client component (CVE-2026-11477)

The reviewed advisory locates a remotely triggerable open redirect in `OAuth2Client` within `hsweb-authorization-oauth2` through version 5.0.1. The short public description does not provide a parameter or detailed preconditions, so the code path must be read before treating it as a pattern match. [hsweb advisory](https://github.com/advisories/GHSA-fxr3-gvm4-m8vc)

### OR-053 — Cloudflare Workers OAuth Provider: callback state exposes redirect URI and token (GHSA-2h78-5wx8-jccc)

Before v0.0.12, the callback handler lacked CSRF protection and used a plaintext `redirect_uri` embedded in base64-encoded state to redirect an authorization code or token. The advisory describes token leakage to an arbitrary endpoint. This is an OAuth callback composition issue; base64 is encoding, not integrity protection. [Google security research advisory](https://github.com/google/security-research/security/advisories/GHSA-2h78-5wx8-jccc)

### OR-054 — Traccar: OIDC authorize and callback redirect overrides (GHSA-ccc7-4r59-4pp7)

The advisory contains two OIDC redirect weaknesses: `/api/oidc/authorize` accepts a `redirect_uri` without a whitelist check, and a callback parameter can override the configured callback. It requires authenticated users and affects versions 6.7.0–6.14.x; the first fix addressed the authorize endpoint and 6.15.0 addressed both. Count this as one advisory with two explicitly documented sinks. [Traccar advisory](https://github.com/traccar/traccar/security/advisories/GHSA-ccc7-4r59-4pp7)

### OR-055 — Redash: post-login `next` survives slash stripping (GHSA-rfgc-hc86-pxrv)

`get_next_path()` strips scheme and network location from the `next` value but does not normalize repeated leading slashes; the result reaches Flask `redirect()` and is treated by browsers as protocol-relative. All listed authentication methods are affected. This is a strong source-transform-sink example and a warning against “remove scheme/host” as a complete validator. [Redash advisory](https://github.com/getredash/redash/security/advisories/GHSA-rfgc-hc86-pxrv)

### OR-056 — mod_auth_openidc: logout URL validator parses differently from browsers (GHSA-xm4c-5wm5-jqv7)

`oidc_validate_redirect_url()` did not parse URLs like browsers, enabling an attacker to bypass logout redirect validation with a backslash-containing URL. The fix normalizes backslashes to slashes, addressing a standards/parser differential. [mod_auth_openidc advisory](https://github.com/OpenIDC/mod_auth_openidc/security/advisories/GHSA-xm4c-5wm5-jqv7)

### OR-057 — Nextcloud user_oidc: protocol-relative URL bypass in login flow (GHSA-8wjr-5cg8-4w73)

The user_oidc application allowed a crafted login link to redirect a user to another site. The report identifies protocol-relative URL validation as the bypass and recommends upgrading to 8.2.2. User interaction with the OIDC login flow is required. [Nextcloud advisory](https://github.com/nextcloud/security-advisories/security/advisories/GHSA-8wjr-5cg8-4w73)

### OR-058 — Tornado `RedirectHandler`: protocol-relative destination (CVE-2026-116578)

The recent advisory describes an open redirect when Tornado's `RedirectHandler` is given a protocol-relative target. The trusted-domain endpoint is usable for phishing; check the actual handler's destination source and the affected version range from the advisory. [Tornado advisory](https://github.com/advisories/GHSA-pw9p-v7r6-gx4p)

### OR-059 — Mastodon: encoded path segments in `/web/*` (GHSA-xqw8-4j56-5hj6)

An unauthenticated open redirect was reported in the `/web/*` route due to improper handling of URL-encoded path segments. This is an application-route normalization case: trace decoded path segments into client navigation or redirect construction and inspect the route's patch. [Mastodon advisory](https://github.com/mastodon/mastodon/security/advisories/GHSA-xqw8-4j56-5hj6)

### OR-060 — Plone `Products.isurlinportal`: reusable portal-URL check (GHSA-q3m9-9fj2-mfwr)

The advisory covers a shared “is URL in portal” check used by several Plone components, often to decide whether a redirect target is safe. This is a validator-reuse case: enumerate all callers and their parsing/redirect behavior. The advisory must be consulted for its exact affected range and patch; the short description alone does not establish every caller as exploitable. [Plone advisory](https://github.com/plone/Products.isurlinportal/security/advisories/GHSA-q3m9-9fj2-mfwr)

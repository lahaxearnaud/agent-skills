# Open redirect static-review skill evaluation

Evaluation date: 2026-11-03. These are small, qualitative scenario checks of source-review behavior, not a benchmark of vulnerability detection performance. No application, browser, scanner, payload, or network target was executed.

## Scenarios

See [evaluation scenarios](evaluation-scenarios.md) for exact prompts, excerpts, and expected behaviors. The same excerpts are used without and with the skill where practical.

## Baseline without the skill

Fresh-context agents received the scenario prompts without access to the new skill.

### Scenario A — Login return paths under deadline pressure

The agent identified the server-side `next` flow and stated that `//attacker.example/path` passes the slash-prefix guard. It separated the `router.replace` flow and conditioned external-navigation behavior on router semantics. It also correctly said the given CSP does not generally block the navigation and did not claim token theft or account takeover.

The main failure was an unsupported severity assertion: **“Low severity (P3) is justified”** without a repository severity rubric, deployment exposure, or product impact context. The agent also did not ask for dependency/configuration context. The skill should therefore require evidence for severity and request relevant version and route configuration while keeping the code-level flaw visible.

Baseline output, verbatim:

> **Verdict: Unsafe.** The server-side check accepts any `next` value beginning with `/`, including `//attacker.example/path`. If the emitted `Location` header is honored by the deployed stack, that protocol-relative URL can send the user to an external site. The source shows the vulnerable condition; it does not prove the final response behavior of the framework and server.
>
> **Status and confidence:** Source-level open-redirect finding; high confidence in the validation flaw, medium confidence in its deployed effect. No runtime testing was performed.
>
> **Browser behavior:** The JavaScript has the same permissive prefix check, so it passes `//attacker.example/path` to `router.replace`. Whether that causes an external navigation depends on the router’s behavior, which the excerpt does not establish. The CSP does not make these redirect paths safe: it does not generally block server `Location` redirects or application-initiated navigation.
>
> **Impact and severity:** An attacker may craft a trusted-site link that redirects a user to an attacker-controlled site, enabling phishing. No token leakage or greater impact is established by the excerpt. **Low severity (P3) is justified;** the evidence does not support a higher rating.
>
> **Remediation:** Allow only known internal destinations, ideally by mapping route identifiers to server-defined paths. Apply equivalent validation before the client-side navigation. Use the framework’s response redirect mechanism consistently and avoid constructing a `Location` header directly from untrusted input.
>
> **Unknowns:** Whether the deployed stack honors the native `header()` call alongside the returned response, how `router.replace` resolves protocol-relative strings, and whether other controls or impacts exist outside this excerpt.

### Scenario B — False positive and safe route selection

The agent did not report the click-only external help link as an automatic redirect. It recognized the fixed route-name set and fallback as constraining the shown router flow, and left the unshown `helpCenterUrl` source unknown. This is a baseline success to preserve.

Baseline output, verbatim:

> **Decision: No, an open redirect is not established by the supplied evidence.**
>
> The shown `router.replace` accepts only the fixed route names `home` and `profile`; other `returnTo` values fall back to `home`. That does not show navigation to an arbitrary external URL. The `href` search hit is also inconclusive: the template binds `helpCenterUrl`, but its value and source are not provided.
>
> **Status / impact:** Unconfirmed; no severity can be justified from these snippets. The named-route allowlist weighs against the reported redirect path, but the `helpCenterUrl` binding remains unknown.
>
> **Remediation:** Trace where `helpCenterUrl` is set and whether untrusted input can control it. Keep external destinations on an explicit trusted-origin allowlist.
>
> **Unknowns:** The source and validation of `helpCenterUrl`, and whether other redirect paths exist.

### Scenario C — Incomplete OAuth evidence

The agent did not claim code theft. It noted that the grep result proves only that the request value reaches `authorizeClient`, then requested inspection of registration matching, normalization, code issuance and victim control. It recommended exact matching. This is a baseline success to preserve; the skill should make the RFC 9700 requirement and the scope of the missing evidence explicit.

Baseline output, verbatim:

> **Decision: No, the evidence does not establish that authorization codes can be stolen.** It does show that the request’s `redirect_uri` value is passed to `authorizeClient`; it does not show whether that method validates the URI or how authorization codes are returned.
>
> **Status / impact:** Suspected, unconfirmed. Code theft could be high impact if an attacker can make the authorization server send a victim’s code to an attacker-controlled URI, but that condition is not established here. Severity cannot be assigned from the title and grep fragment alone.
>
> **Evidence needed next:** Inspect `authorizeClient` and the surrounding flow to determine whether the URI is matched against the client’s registered redirect URIs, including any normalization, wildcard, or scheme rules; where and how the authorization code is issued and delivered; and whether an attacker can cause a victim’s authorization request to use an accepted attacker-controlled URI. Also determine whether code exchange protections such as PKCE apply.
>
> **Remediation:** Enforce exact matching against redirect URIs registered for the client before issuing or returning a code; reject unregistered values.

## Evaluation with the skill

Fresh-context agents read `SKILL.md` and the relevant bundled references before reviewing the same scenarios.

### Scenario A — Login return paths under deadline pressure

The agent separated the server and client paths, identified the server `Location` flow and the `//` condition, kept the Vue result as a candidate pending router semantics, rejected CSP as a general redirect control, and left severity unassigned without a rubric/exposure context. This addresses the baseline's unsupported **“Low severity (P3) is justified”** claim. The agent also stated phishing as the supported impact and did not infer token theft or account takeover.

Output, verbatim:

> Overall decision: **UNSAFE for release**. The server excerpt conditionally establishes an open redirect: query-controlled `next` passes the slash-prefix check for a value such as `//attacker.example`, then reaches the 302 `Location` header. The external redirect depends on the method being reachable and the response header reaching the browser; routing and middleware details were not supplied.
>
> The client excerpt is a **candidate**, not an established external redirect. Query-controlled `next` reaches `router.replace`, but the router package, version, configuration, and handling of `//...` are unknown.
>
> Supported impact is phishing through a trusted login domain. The snippets do not support token theft or account takeover. **Severity is unassigned** because no severity rubric or exposure details were provided. The CSP does not fix the server redirect or generally block ordinary top-level HTTP(S) navigation.
>
> Remediation: map fixed route identifiers to internal destinations and fall back to `/dashboard`. If arbitrary paths are required, validate against a fixed origin, canonicalize, and pass the same checked value to the sink. Apply an equivalent fixed-route policy to the client or remove its redirect. Review was limited to the supplied excerpts; no application, browser, scanner, or network requests were used.

### Scenarios B and C — False positive and incomplete OAuth evidence

The agent did not report the click-only help link or constant route-name allowlist as an open redirect, but preserved the unknown source/route-definition caveats. It kept the OAuth fragment at candidate status, required exact registered URI matching and asked for all authorization branches and code/token exchange evidence. This is consistent with the baseline successes; the skill makes the required distinctions and RFC rule explicit. No performance improvement can be inferred from two small examples.

Output, verbatim:

> **Ticket 1 — No open redirect established in the reviewed scope.** The `<a :href="helpCenterUrl">` requires a click, and the snippet does not show that its value is attacker-controlled. The query parameter selects only fixed route names in a constant allowlist, with a fixed `home` fallback. Route definitions and guards are not shown, so those still need review before drawing a broader conclusion.
>
> **Ticket 2 — Candidate only; code theft is not established.** The query-supplied `redirect_uri` reaches `authorizeClient(...)`, but the fragment does not show what that function validates or where the value goes. Next inspect its implementation, client registration and exact redirect-URI matching, all success and error branches, code delivery, state binding, and token-exchange protections such as PKCE and client authentication. Claim code theft only if the evidence shows an attacker-controlled URI can receive a victim’s code and that the code can be exchanged.
>
> No application, browser, scanner, payload, or network testing was performed.

## Criteria

1. Separates server `Location` responses from automatic client navigation.
2. Traces controllable source, transformations, policy, and final sink.
3. Treats URL parser/version/configuration uncertainty explicitly.
4. Does not report ordinary clickable links or fixed internal route mappings as open redirects without an automatic external-navigation flow.
5. Does not infer OAuth code/token theft, account takeover, CSP blocking, or severity beyond evidence.
6. Obeys static-only constraints and gives an actionable source-level remediation.

## Limits

Only three synthetic excerpts were assessed by separate fresh-context agents. The scenarios are not representative of all languages, frameworks, URL parsers, or repository layouts. No detection-rate, recall, precision, or false-positive rate is measured.

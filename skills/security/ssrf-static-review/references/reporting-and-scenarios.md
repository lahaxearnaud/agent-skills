# Evidence and scenarios

Report actor and privileges; input location and transformation; server-side sink; controllable destination/method/headers/body; validation and redirect/DNS/proxy semantics; response visibility; observed configuration and missing deployment facts; supported impact and focused remediation. Static evidence is not a runtime exploit.

- A controller passes a request URL to a server HTTP client with no visible destination policy: trace wrappers and deployment; if all paths are visible, establish the attacker-influenced request. Internal reachability remains conditional without evidence.
- An image loader validates an initial host then follows redirects: check actual client behavior and per-hop validation. A redirect-capable host under attacker influence may cross the intended boundary; do not assume an exploitable redirect exists.
- A URL appears only in a Vue browser fetch: not a server SSRF sink on that path. Trace separate SSR or API proxy code if present.
- A fixed URL is fetched and only a path parameter varies: determine whether URL joining permits origin changes; do not assume it does.
- A separate policy resolves a hostname but the client performs a fresh resolution: a gap is plausible; mark the effect uncertain until the connection binding and policy are known.
- A blind webhook invokes an attacker-controlled endpoint: do not claim response disclosure; identify what side effects and reachable destinations are supported.

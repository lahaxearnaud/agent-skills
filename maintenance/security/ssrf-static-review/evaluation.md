# Synthetic review scenarios

These are evaluation criteria, not observed runs or public incidents. No controlled precision/recall evaluation has been performed.

1. PHP controller passes user URL to an HTTP client; wrapper and egress configuration are missing: identify a candidate and the missing facts, without claiming metadata disclosure.
2. An image URL is checked against an allowlist but its fetch follows redirects: examine per-hop policy and actual client configuration; do not assume an attacker-controlled redirect exists.
3. Vue browser code fetches an input URL with no server proxy: do not report server SSRF on that path; examine SSR only if present.
4. Server worker fetches a stored tenant-supplied webhook URL and discards the response: trace stored actor to sink and distinguish blind request from response disclosure.
5. DNS is checked once but a later client resolves again: flag a potential validation/connection gap, dependent on resolver binding and actual configuration.
6. The destination is fixed and only a path changes: trace URL joining before claiming host control.

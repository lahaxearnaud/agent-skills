# Offline source notes

Summaries consulted 2026-11-05; these sources guide review but do not prove a vulnerability in the target. URLs provide attribution and optional follow-up. Never submit private reviewed code or secrets to external services.

## OWASP SSRF prevention

[OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) separates applications that can restrict calls to identified trusted applications from those that must fetch arbitrary external addresses. The former can combine strict destination allowlists with network controls; the latter need an explicitly defined address and protocol policy, careful URL parsing and DNS handling, and network-level defenses. Automatic redirect following can bypass validation of the initial address. Where DNS is involved, consider all returned addresses, rebinding and how the checked result is bound to the actual connection. A URL parser or denylist on its own is not a universal defense.

## Symfony HttpClient

[Symfony HttpClient documentation](https://symfony.com/doc/current/http_client.html) documents HTTP requests, client configuration, redirects and the `NoPrivateNetworkHttpClient` decorator for blocking requests to private networks. Determine the installed version and whether the decorator is actually applied to the exact client and path. An available feature or configured service name does not establish that every request is protected. Inspect redirection and proxy options and application-specific destination policy in the relevant version.

## PHP HTTP streams

[PHP HTTP context options](https://www.php.net/manual/en/context.http.php) describe options such as `follow_location`, `max_redirects`, `proxy`, headers, method and request content for the HTTP wrapper. Verify the context actually passed to `file_get_contents` or other stream operations and distinguish the HTTP and HTTPS wrappers from arbitrary protocol handling. Initial URL validation can be undermined if redirects are followed without equivalent destination checks.

## Limits

Runtime defaults differ by version, client and configuration. Use the target repository's installed code and effective configuration for specific claims. Network egress, DNS, proxy resolution and cloud service protections can be outside the repository; label them unknown when unavailable.

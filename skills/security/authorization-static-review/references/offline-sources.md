# Offline source notes

These attributed summaries support source review without Internet access. They are guidance, not evidence that the reviewed application is vulnerable. Consulted 2026-11-05; online lookup is optional and should only address a material unresolved detail without disclosing private code.

## OWASP authorization and object-level authorization

[OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) recommends deny by default, checking permissions on every request, and verifying the chosen authorization mechanism for the resource and action. Authentication alone does not authorize an operation; compare the principal, relationship to the resource, requested action, and context. An ID or UUID does not establish permission. Check list, search, mutation, export, and nested-resource paths independently. A framework's default or a single controller check is not evidence that every path is covered.

[OWASP API Security 2023: BOLA](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/) explains that APIs commonly accept object identifiers and that authorization needs to apply to the specific object in every function accessing it. Compare identifiers to actual object ownership and the authenticated principal; merely checking a user ID against one request field does not cover all policies. An API path without a demonstrated sensitive object or missing guard is a candidate, not a confirmed flaw.

## Symfony security configuration and voters

[Symfony access-control documentation](https://symfony.com/doc/current/security/access_control.html) describes ordered `access_control` rules: only the first matching entry applies. Matching may depend on path, method, host, IP or other configured criteria. Inspect the effective version, configuration, firewall, request method and routing; a later restrictive entry does not override an earlier match.

[Symfony voters documentation](https://symfony.com/doc/current/security/voters.html) describes voters as decisions about attributes and an optional subject. A controller or service can invoke `isGranted`/`denyAccessUnlessGranted` with an action and object; inspect the actual subject, voter support/decision logic, and configured decision strategy. A class named voter or an authorization call on a different object does not establish protection. Framework version and application configuration can change how these mechanisms apply.

## Boundaries and limitations

Vue guards and conditional rendering operate in the client; identify the server endpoint and its policy before concluding an authorization bypass. These notes summarize general guidance; the reviewed project's code, installed framework version, and deployment configuration determine the actual path. Missing configuration or external policy remains an explicit uncertainty.

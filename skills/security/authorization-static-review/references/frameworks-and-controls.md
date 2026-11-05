# Framework controls and false positives

## Symfony

- Identify the installed Symfony Security and FrameworkBundle versions and effective firewall/authenticator configuration.
- `security.yaml` `access_control` rules are order-sensitive: inspect the first matching rule, path, method, host, and firewall. A restrictive later rule may never apply.
- Trace route/controller `#[IsGranted]` or legacy annotations, `denyAccessUnlessGranted()`, `isGranted()`, and authorization checks in services. Confirm the metadata is active for the installed version and route.
- For voters, inspect `supports()` and the decision logic, the current user, attributes/action, and exact subject passed by the caller. A voter class or call name alone does not prove the decision is correct.
- Follow repository queries and domain relationships for ownership and tenant isolation. A broad role check can authorize an operation while leaving access to another user's object.
- Check inherited controller metadata, route aliases, alternate methods, exception/fallback branches, and APIs that call the same service directly.

## Vue and browser clients

- Vue Router guards, hidden or disabled controls, role checks in Pinia/Vuex, and client-side redirects govern interface behavior. They do not enforce authorization at the server.
- Do not report a backend authorization bypass solely because a UI control is visible. Find the corresponding protected endpoint and trace its server-side policy.
- Do not mark an endpoint protected because the Vue client refuses to call it. Conversely, data already delivered to the browser may be exposed even if the view is hidden; report that distinct data-exposure path with evidence.
- For SSR or server routes, identify the server boundary and review its authorization independently of client code.

## General controls

- Authentication establishes identity, not permission to every function or object.
- Unpredictable identifiers, UUIDs, hidden fields, CORS, CSRF defenses, and frontend checks do not replace authorization decisions.
- A list query constrained to a tenant does not automatically secure detail, export, mutation, count, or bulk queries.
- Field allowlists and DTOs can constrain mass assignment; verify the actual mapping and all writable fields rather than trusting a type or serializer label.
- A framework helper is neither automatically safe nor unsafe. Verify where its result comes from, what it checks, and whether execution reaches the protected operation only after a deny decision.

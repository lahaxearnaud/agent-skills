# Authorization sources and protected operations

Use this catalog to find candidates, then trace each flow in context.

## Actor and authority

- Authenticated principal, session/token claims, roles, groups, scopes, API keys, service identities, delegated users, and anonymous/public access.
- Tenant, organization, owner, membership, and relationship data. Establish whether values come from trusted server-side identity or request input.
- Framework attributes, middleware, access-control configuration, policy/voter calls, explicit ownership checks, and repository-level constraints.

## Operation and resource sources

- Route parameters and nested IDs; query, form, JSON, GraphQL, headers, cookies, and batch arrays.
- IDs received from queues, scheduled tasks, imports, webhooks, saved workflows, or database records. Persistence does not make a value authorized.
- Client-selected fields, sort/filter expressions, export columns, and polymorphic resource types.

## Protected sinks

- Reads and mutations: ORM/repository lookups, domain services, serializers, file/object storage, payment or account actions, and response construction.
- Bulk and indirect operations: list/search/count, export/download, batch mutation, relationship changes, invitations, impersonation, background jobs, and admin actions.
- Property-level boundaries: serialization groups/projections and entity/request mapping; writable or readable fields such as roles, owner, tenant, status, and billing data.

## Trace questions

1. Which actor controls the request, and what identity/permissions are established server-side?
2. Which operation and resource are reached? Can the caller select or substitute the resource identifier?
3. What policy applies to this action and object? Does it check the same actor, resource, tenant, and fields used by the sink?
4. Does every route, method, branch, and indirect path enforce that policy before data is read, changed, or returned?
5. What evidence is missing: route reachability, effective configuration, policy implementation, identity provenance, or deployment behavior?

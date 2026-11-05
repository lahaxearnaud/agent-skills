# Reporting and scenario decisions

## Evidence states

- **Statically established authorization bypass:** visible code connects an actor-controlled path to a protected operation/resource and shows that the required policy is absent, ineffective, or applied to the wrong subject. Runtime exploitation is not observed.
- **Candidate:** a plausible path exists, but a material route, configuration, identity, policy, resource, or call link is unavailable. Name the missing evidence.
- **Not established for this path:** visible code shows an effective policy or no protected operation on the traced path. Do not generalize beyond that scope.

## Finding template

1. Title and evidence status; state function, object, tenant, or property boundary.
2. Actor and required privileges, with source/configuration file and line.
3. Route/operation and resource identifier; trace transformations and lookups.
4. Exact policy and enforcement point, or evidence of its absence/mismatch; cite relevant lines.
5. Conditions and supported impact; keep unknown configuration and runtime facts explicit.
6. Minimal remediation at the server boundary and relevant alternative paths.
7. Files and surfaces reviewed, meaningful gaps, and statement that no runtime request was made.

## Mini decision grid

| Pattern | Decision |
|---|---|
| Controller loads `/orders/{id}` and returns it after authentication only | Candidate or established object-level bypass depending on complete route and policy evidence. |
| Symfony voter is invoked with the requested entity | Follow its implementation and decision inputs; invocation alone does not prove a correct ownership/tenant check. |
| Vue route guard blocks a non-admin page while API lacks visible policy | Client guard is not server authorization; trace the API and classify based on available backend evidence. |
| Vue hides an action button but endpoint checks actor and target resource | UI behavior is not a bypass of the shown endpoint. Check alternate endpoints only if in scope. |
| List endpoint filters by tenant, detail endpoint uses unscoped `find(id)` | Review independently; do not transfer list protection to detail. |
| Request DTO excludes `role`, but a separate mapper writes it | Trace the mapper and reachable fields; labels/types alone are not evidence of the final writable set. |

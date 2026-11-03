# Configurable Docker image allowlist

**Status:** Approved by the user on 2026-11-03.

## Intent

Prevent the isolated PoC runner from launching arbitrary Docker images while allowing users to select a private registry or follow new language-image tags without republishing the skill. The user chose an environment-provided list that replaces the built-in list and said tag-only wildcards are useful.

## Approaches

1. **Exact image tags only.** Each registry, repository, and tag is listed literally. This is easiest to audit, but every image-version change requires updating the local configuration.
2. **Exact registry and repository, wildcard only in the tag (recommended).** This permits patterns such as `registry.example.test/team/php:8.*`, while keeping the source and image name fixed. The user explicitly asked to use this flexibility for future language tags.
3. **Wildcards across the whole reference.** This is rejected because it can silently authorize different registries or repositories.

## Decision

- Keep a small built-in list of fully qualified patterns for the image repositories already used by the skill: `docker.io/library/node:*`, `docker.io/library/php:8.*`, `docker.io/library/python:*`, and `mcr.microsoft.com/playwright:*`. PHP 7 is intentionally excluded from the built-in policy.
- Add `ISOLATED_POC_ALLOWED_IMAGES`. When unset, use the built-in patterns. When set, parse its comma-separated entries as the entire effective allowlist; do not merge them with defaults. An empty or malformed value fails closed.
- Require a fully qualified, unambiguous registry and repository plus a non-empty tag pattern. Docker identifies a registry host by a dot, a port, or the exact host name `localhost`; reject bare single-label hosts that Docker can interpret as Docker Hub namespaces. Allow only `*` as a wildcard, and only after the final colon in the tag. Registry, namespace, and image name must match literally. Examples: `docker.io/library/php:8.*`, `registry.example.test/security/php:8.3-cli`, and `localhost/team/runtime:1.2`.
- Accept valid repeated Docker repository separators (such as `my__runtime` and `my--runtime`) rather than rejecting otherwise valid private image names.
- Continue to require a concrete tagged image plus `@sha256:<digest>` in the manifest. Match the full registry/repository/tag before the digest against one allowlist pattern. Reject the `latest` tag, remote Docker daemons, uncached images, and digest mismatches as today.
- User-selected private images are permitted only when explicitly named by the environment allowlist; the variable is read by the host runner and is not forwarded into the container.

## Acceptance checks

- Tests cover defaults (including rejection of PHP 7), environment override (including a private registry), exact and tag-wildcard matching, registry-host disambiguation, valid `localhost`/ported registry names and repeated repository separators, rejection of wildcards in registry/repository, malformed or empty configuration, missing tags/digests, `latest`, and digest inspection with a registry port.
- Update the skill, package README and workflow so the override semantics, supported pattern syntax, default entries, and digest requirement are clear offline.
- Add an ADR and index entry because this changes the durable image-trust boundary. Run the runner unit suite, harmless cached-image checks, Markdown-link/frontmatter checks, `npx skills add . --list`, and temporary local installation verification.

This approved design is the specification for the implementation plan in `docs/superpowers/plans/`.

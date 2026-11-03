# ADR-0007: Static open redirect review scope

- **Status:** Accepted
- **Date:** 2026-11-03
- **Decision owners:** Repository maintainers

## Context

The repository is adding an installable skill for reviewing server-generated redirects and browser-side navigation. Like the existing source-review skills, it should help agents find code paths without implying that a static review proves a live exploit. Open redirects also involve browser and framework URL parsing, deployment configuration, and OAuth flows that may not be visible in a source excerpt.

## Decision

The open redirect review skill analyzes available source code, templates, routes, framework configuration, dependencies, and supplied static-analysis results only. It does not launch the target application, browser, payloads, active scanners, or network requests. It distinguishes a source-to-navigation flow supported by visible code from a candidate with missing links or runtime-dependent URL semantics. It does not assign severity unless the repository's rubric and the relevant exposure and impact conditions are evidenced.

The skill covers server-side HTTP redirect responses and client-side automatic navigation in JavaScript and framework routers. It treats clickable external links, off-site URL generation without an automatic-navigation sink, SSRF, and XSS as separate behaviors unless a documented chain connects them.

## Consequences

The skill must trace inputs, transformations, validators, and the exact sink, and preserve unknown version, proxy, browser, and configuration conditions. It must include its own portable references so installation does not depend on this repository's research corpus. The existing [ADR-0003](0003-static-security-review-scope.md) continues to govern only XSS and SQL injection review; this ADR records the scope for open redirect review.

# ADR-0008: Static path traversal review scope

- **Status:** Accepted
- **Date:** 2026-11-03
- **Decision owners:** Repository maintainers

## Context

The repository is adding an installable skill for reviewing file path traversal in Web code. The weakness appears across ordinary file reads/writes/deletes, static resource handlers, framework/template loaders, archive import/restore, symlinks, and path parsing across request, framework, and operating-system layers. The final impact depends on reachable code, authentication, configuration, filesystem state, and process permissions. The skill will be used by code agents that may not be able to execute the target application.

## Decision

Add `path-traversal-static-review` under `skills/security/`. It performs source-based review of server-side Web and Web-adjacent code, including PHP/Symfony/Twig, JavaScript/Node, Java/Spring, Python, Go, and other stacks. It traces untrusted path inputs through decoding, normalization and validation to the actual filesystem or archive sink; records preconditions and unknowns; and distinguishes read, write, delete, template/resource, metadata-only, and recipient-side archive impacts.

The skill does not launch the reviewed application, browser, scanner, payload, or network request. It may inspect source, templates, routes, configuration, dependency declarations, and existing static evidence. It does not claim runtime exploitability, assign severity without evidence and a project rubric, or treat a similar CVE as proof about the current code.

Keep the research corpus under `corpus/security/path-traversal/` and include all operational references within the installable skill directory. The initial main register contains 50 published Web/application case records. Related local tooling, libraries, path-parser issues, aliases, and unreviewed leads remain separately labeled and are not silently counted as independent incidents.

## Consequences

The method is portable after installation and does not need the research corpus during code review. Static analysis cannot prove deployment-specific filesystem state, route exposure, symlink control, operating-system semantics, or runtime behavior; findings must state these limits. The corpus and skill will require maintenance as frameworks, advisories, and archive APIs change. This scope is distinct from XSS, SQL injection, and open-redirect reviews recorded in ADR-0003 and ADR-0007.

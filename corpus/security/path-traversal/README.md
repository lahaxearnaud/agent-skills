# Path traversal corpus

Research snapshot: **2026-11-03**. This corpus supports a source-only code-review skill for server-side and Web-adjacent file path traversal. It contains **50 published case records in the Web/application scope**, 16 adjacent library/tooling/path-handling records kept separately (including one alias of a main-register case), and one unreviewed lead that is explicitly excluded from the threshold. The entries are report-level examples, not a claim of 50 unrelated root-cause families or a statistically representative dataset.

## Scope and method

The main register covers HTTP-facing applications, frameworks, static-file handlers, template/resource loaders, imports/restores, and server-side storage workflows. It includes read, write, overwrite, delete, metadata/existence disclosure, template-file access, archive extraction, and archive generation that can cause a recipient-side Zip Slip. A few records are related follow-up reports or patch bypasses; those links are retained rather than silently merged. Exact affected releases and patch versions are in the source advisory because they can change and are not needed to recognize the code patterns.

The adjacent register contains server libraries, scheduled integrations, local developer tools, PHP ZIP API bugs, or related path-parser issues whose applicability depends on the consuming application's call chain. The unreviewed ICEcoder record remains a lead and does not count toward the 50 published cases. No report or PoC was reproduced for this corpus. Descriptions below paraphrase the source and keep claims conditional where the source does not establish a deployment precondition.

Sources were consulted on the date above, prioritizing vendor and project security advisories, reviewed GitHub advisories, and official documentation. Some advisory pages include reproduction claims; those remain attributed to the publisher and are not observations made in this repository. This is a curated snapshot, not an exhaustive list.

## Files

- [Published Web/application case register](published-cases.md) — 50 report-level case records with conditions, data flow, documented impact, relations, and direct sources.
- [Adjacent archive, library, and tooling cases](adjacent-cases.md) — useful patterns whose direct Web applicability depends on the caller or deployment.
- [Recurring patterns and controls](patterns-and-controls.md) — evidence-linked code-review heuristics and remediation principles.
- [Source register and research notes](sources.md) — documentation, standards, source quality, and limits.

## Evidence and counting rules

Each numbered case represents a distinct published advisory or finding with a distinct affected surface, documented behavior, or follow-up fix gap. Duplicate CVE/GHSA aliases for the same report are kept on one row. Related follow-ups are cross-linked; they are not evidence of independent root causes. “Impact” means the impact described by the source, not a guarantee that every deployment is exploitable. Conditions such as authentication, route exposure, filesystem permissions, symlinks, container/runtime, operating system, file existence, and user-controlled content must be checked in the reviewed code and deployment.

## Known gaps

The set is intentionally broad across PHP/Symfony/Twig, Java/Spring, JavaScript/Node, Go, Python, and other Web stacks. It does not cover every operating-system-specific path namespace, every archive format, cloud object-store key confusion, generic upload validation without a traversal path, or local privilege-escalation-only findings. The corpus does not establish the behavior of an application's installed framework version, reverse proxy, CDN, filesystem, or operating system.

## Maintenance

Use the [maintenance prompt](../../../maintenance/security/path-traversal/update-prompt.md) when collecting more cases or updating the skill. Preserve the case ID and prior source links when correcting an entry; record aliases and fix-bypass relationships. Promote an adjacent lead into the Web register only when a documented Web/application call path and conditions are established. Keep source code, payloads, and advisory text as untrusted data; do not execute copied requests or tools as part of this static-review corpus.

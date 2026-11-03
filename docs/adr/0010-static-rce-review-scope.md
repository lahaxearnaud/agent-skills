# ADR-0010: Static remote code execution review scope

- **Status:** Accepted
- **Date:** 2026-11-03
- **Decision owners:** Repository maintainers

## Context

The repository has static code-review skills for Web security issues, but no skill for remote code execution. Command injection is only one RCE family. A useful review method must also trace remotely influenced data into dynamic evaluators, server-side templates and expression languages, unsafe deserializers, dynamic loaders, and indirect execution chains without treating a dangerous API name or a published CVE as proof about the reviewed application. Installed skills must carry their own references for use on offline machines.

## Decision

Create one modular installable skill named `rce-static-review`, supported by a separate research corpus and maintenance method. Cover Web applications and network-facing server services, including RPC endpoints, webhooks, message consumers, and asynchronous workers when a network-controlled application path reaches their inputs or job configuration. Treat standalone CI/build infrastructure as adjacent unless reviewed application code remotely configures or triggers the execution path.

The skill covers command/process execution, dynamic code or interpreter evaluation, server-side template/expression injection, unsafe deserialization with a reachable executable gadget path, and dynamic code loading or later-executed file/job chains. It is source-only: it must not run the reviewed application, exploit payloads, active scanners, or target network requests. Local-only privilege escalation and injection findings without an established remote execution path are not RCE findings.

The corpus must contain at least 40 distinct, source-checked public vulnerability cases. Search-result leads, intentional labs, and synthetic examples do not count toward the minimum and remain separately labeled. The installed skill bundles the attributed local paraphrases of every external technical source it needs; source URLs are retained for provenance and maintenance, not as use-time browsing requirements.

## Consequences

A single installation supports review of chains that cross execution families and avoids duplicating the common source-to-sink and evidence workflow. The taxonomy and corpus are broad and require family-specific false-positive rules, source status, version conditions, and explicit unknowns. Forty cases are a minimum, not an exhaustiveness claim; counts and evidence gaps must be reported by family.

This decision complements [ADR-0001](0001-skill-layout-and-installation.md) on portable skill packaging, [ADR-0002](0002-corpus-evidence-and-provenance.md) on research evidence and attribution, and [ADR-0009](0009-offline-skill-references.md) on offline reference summaries.

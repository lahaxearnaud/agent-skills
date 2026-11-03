# Static Remote Code Execution Review Skill — Design

**Status:** Proposed for review  
**Date:** 2026-11-03

## Intent

Add an installable security skill that helps a coding agent find and assess remote code execution paths through static source review. The agent should connect remotely influenced input to an execution boundary, determine which controls and environmental conditions apply, and report only what the code and local evidence support. The repository will also hold the research corpus and maintenance method needed to update the skill.

## Goals

- Cover remote execution families rather than treating OS command injection as the only RCE mechanism.
- Include at least 40 distinct, source-checked public vulnerability cases in the corpus; search-result leads and synthetic/lab examples do not count toward this minimum.
- Give the reviewer one consistent source → transformations/guards → interpreter or execution sink → reachability/conditions workflow.
- Distinguish demonstrated unsafe flows, incomplete candidates, indirect execution chains, and non-RCE injection or code-loading paths.
- Package the skill with all operational references and paraphrased technical source notes so an installed copy does not require a corpus checkout or Internet access.
- Preserve a source-qualified corpus of public advisories, CVEs, bounty reports, tickets, intentionally vulnerable labs, and synthetic counterexamples, with their evidence classes kept separate.
- Evaluate positive, negative, and incomplete examples without executing the target application or payloads.

## Proposed scope and boundaries

The proposed review surface is Web applications and network-facing server services, consistent with the repository's existing static Web security skills. Include RPC endpoints, webhooks, message consumers, and asynchronous workers when a network-controlled application path reaches their inputs or job configuration. Treat standalone CI/build infrastructure as adjacent unless the reviewed application can remotely configure or trigger the relevant execution path. Prioritize PHP/Symfony, JavaScript/Node.js, Python, and JVM stacks, then include other technologies when a distinct execution pattern or well-sourced case warrants it.

The taxonomy should include:

1. OS command and process execution: shell command injection, unsafe argument construction, option/argument injection, environment and working-directory influence, and command wrappers.
2. Dynamic code and interpreter evaluation: `eval`/`exec`-like APIs, generated code, scripting engines, expression languages, and unsafe interpreter configuration.
3. Template and expression injection where attacker-controlled template/expression syntax can reach code execution; distinguish ordinary output injection from server-side template execution.
4. Unsafe deserialization and gadget-driven execution, only when the serialized input, deserializer, reachable gadget/callback path, and execution effect are supported by evidence.
5. Dynamic loading and execution chains: untrusted module/plugin/class loading, file writes or uploads later included or compiled, unsafe job/build hooks, and similar paths when remote control reaches execution.

Local-only privilege escalation, dependency presence without a reachable path, arbitrary file upload without execution, and injection findings that do not establish code or command execution are out of scope for RCE findings. SQLi or another vulnerability may be recorded as a chain only when the execution consequence is source-supported; do not recategorize the underlying issue automatically.

The installed skill is source-only. It must not launch the reviewed application, execute exploit payloads, invoke dynamic scanners against a target, or claim runtime reproduction. Static analyzer output is a lead to verify in source, not proof by itself. Impact such as operating-system command execution, filesystem access, credential exposure, or lateral movement remains conditional on the demonstrated process identity, privileges, isolation, network access, route reachability, role, and other visible conditions.

## Approaches considered

### A. One flat RCE skill and one large reference document

This is simplest to install, but command execution, template injection, deserialization, and code loading need different evidence and false-positive rules. One growing document would be hard to review and update.

### B. One modular `rce-static-review` skill — proposed choice

Install one skill with a short common workflow and separate family references under its `references/` directory. Organize the research corpus under `corpus/security/remote-code-execution/`, maintenance material under `maintenance/security/remote-code-execution/`, and use separate case files or data sections by family. This keeps a single installation and supports chains crossing multiple families while letting each family state its own sink, conditions, safe cases, and uncertainty rules. Keep external source summaries bundled by technical area.

### C. Separate installable skills for each RCE family plus a router

This reduces irrelevant material for a narrow audit, but creates multiple packages, duplicated workflow and maintenance, and a router that may miss cross-family chains. Reconsider it only if research and evaluation show that one package becomes unmanageably large or causes material retrieval failures.

The proposed choice is approach B because the request is to cover all RCE types and agents should be able to install one review skill. Separate packages can be reconsidered later if research and evaluation show meaningful retrieval or maintenance problems.

## Proposed repository deliverables

- `skills/security/rce-static-review/`: installable English skill, family-specific references, offline source notes, and README.
- `corpus/security/remote-code-execution/`: index, at least 40 distinct source-checked public vulnerability cases grouped by family, separate leads, standards/tool notes, patterns, and safe/incomplete/synthetic examples. Report case counts by family and source status; do not merge duplicates or fill the minimum with unverified titles.
- `maintenance/security/remote-code-execution/`: source collection and qualification prompt, update method, evaluation scenarios, and recorded outputs.
- Root README/catalog and `AGENTS.md` updates, `PROVENANCE.md` update, and an ADR describing the accepted RCE skill scope and packaging if implementation is approved.

Skill instructions, installed references, and README will be in English by repository convention. Corpus summaries will use the established security-corpus conventions and retain original identifiers and quotations as needed. The skill's user-facing findings will follow the audited project's requested language.

## Evaluation and acceptance

Define separate positive, negative, and incomplete static snippets for each execution family, plus at least one cross-family chain and a trust-boundary case. Fresh-context reviewers should be able to distinguish command execution from a harmless argument, a safely parameterized process call, a template rendered as data, benign deserialization without executable gadget path, and a file upload with no later execution. Record package-relative evidence and explicit unknowns. Compare with and without the skill if separate evaluators are available; do not present this small qualitative set as recall or precision.

Validate Markdown links and skill metadata, confirm `npx skills add . --list`, install the package from a temporary local checkout, and verify that every external technical source cited in the package has an attributed local synopsis. No target application, payload, exploit, or runtime scanner will be executed.

## Consequences and open points

The broad taxonomy improves coverage of RCE chains but increases corpus size and the chance of overclaiming from a dangerous-looking API. Family-specific evidence requirements, clear exclusions, source status, version conditions, and negative examples are required to control that risk. The corpus will be a curated snapshot, not an exhaustive catalogue of every RCE issue.

The web/server boundary and the modular single-skill structure are the proposed design decisions for approval. The user-approved minimum is 40 distinct, source-checked public vulnerability cases. Report case volume by family and evidence level, keep leads/labs/synthetic examples separate from that count, and leave coverage gaps visible rather than manufacturing records.

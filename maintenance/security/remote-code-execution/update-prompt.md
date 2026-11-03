# Research and regeneration prompt

Use this prompt to maintain `rce-static-review`. The repository instruction file, this maintenance directory, ADR-0010 and the corpus README define the project rules; this prompt does not override them.

> Research and update the static RCE review corpus and skill in English. Cover remotely reachable Web applications and network-facing services across command/process execution, dynamic evaluation, server-side template/expression injection, unsafe deserialization, dynamic loading, and delayed file/job execution chains.
>
> Read each primary vendor/maintainer advisory, official vulnerability record, or sufficiently detailed public issue directly. Search snippets and secondary summaries may discover leads but are not evidence. For every retained case, record a stable CVE/GHSA/vendor identifier, affected/fixed versions as stated, source status/type, publication date, consultation date, remote actor/input, source-to-execution path, required role/configuration/platform/reachability/trigger, impact claimed by the source, fix, evidence limits and direct source URL. Use original concise paraphrase; do not reproduce advisory text or operational exploit instructions.
>
> Deduplicate aliases for one upstream vulnerability. Keep distinct bypasses or regressions separate only when public evidence describes distinct issues/fixes. Preserve source metadata/prose conflicts explicitly. Maintain at least 40 distinct qualified records; leads, unreviewed claims, local-only tools, intentional labs and synthetic examples do not count. Keep those items in a clearly separate leads file.
>
> Include a finding only when the consulted source documents a remote/network-controlled path and an RCE consequence. A conditional file-write, upload, worker, model, job or configuration chain may qualify only when the source explicitly reports RCE; name every later-load/execute condition. Exclude ordinary argument handling, browser-only execution, local privilege escalation and unauthenticated/remote labels that do not establish the execution path. Do not use a dangerous API or severity label as proof.
>
> Synthesize source-backed patterns and controls. Consult official language/framework documentation, CWE/OWASP material and static-analysis query documentation. Record tool product/version, documented source/sink model, prerequisites, known limits, consultation date and whether it was merely researched or actually run. Do not run an analyzer against a target as part of this source-only skill project.
>
> Keep installed skill references offline-capable: every external technical source used operationally must have a dated, attributed local paraphrase, conditions and limitations in `skills/security/rce-static-review/references/offline-sources.md`. Use only package-relative links in the skill. Preserve attribution and use short paraphrases, not copied third-party text. Keep original URLs as provenance/update pointers.
>
> Update the skill's source-to-sink method, false-positive criteria, family guides, impact limits, report format, maintenance README, corpus README/counts, root README, provenance and ADR index only when required. If an architectural choice changes, record a new ADR under `docs/adr/` and index it in `AGENTS.md`.
>
> Maintain the inert evaluation scenarios. Compare a fresh-context baseline without the skill and a separate fresh-context run with only this skill package available when such evaluators are available. Preserve exact outputs and evidence citations; do not claim an improvement when baseline is already correct. If independent evaluators are unavailable, record that limitation plainly rather than inventing results. Evaluate only inert code snippets; do not execute the application, exploit payloads, scanners or target network requests.
>
> Run the repository's corpus threshold/metadata check, package-relative link/source checks, `git diff --check`, `npx skills add . --list`, and temporary local installation comparison when the CLI is available. Review changes for unrelated files, unsupported claims, copied text, duplicate cases and impact overstatement before committing.

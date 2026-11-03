# Remote code execution case corpus

This is a curated, source-checked snapshot of public vulnerabilities that demonstrate or explicitly describe remote paths to code or command execution in web applications and network-facing services. It is designed to train static source review: the useful unit is the path from remote input, through transformations and trust boundaries, to an execution sink, with deployment conditions attached.

## Qualified case count

The case files contain **55 distinct public vulnerability records** as of 2026-11-03.

| Execution family | Cases |
| --- | ---: |
| Execution family | Total | GitHub Reviewed | Maintainer GitHub | Vendor |
| --- | ---: | ---: | ---: | ---: |
| Command and process execution | 10 | 9 | 1 | 0 |
| Dynamic code and interpreter evaluation | 9 | 8 | 0 | 1 |
| Template and expression injection | 14 | 7 | 7 | 0 |
| Unsafe deserialization | 14 | 13 | 1 | 0 |
| Dynamic loading and execution chains | 8 | 6 | 0 | 2 |
| **Total** | **55** | **43** | **9** | **3** |

Source status within the case files: **43 GitHub Reviewed advisories, 9 maintainer-published GitHub advisories without an explicit GitHub Reviewed label in the consulted page, and 3 vendor advisories**. This is transcribed from the consulted source, not inferred from severity or CVE assignment. The family matrix shows the source-status breakdown so the total is auditable.

The count includes distinct identifiers whose source was opened and whose record documents a remote input path and an RCE consequence. Cases with conditional execution chains remain included when the source explicitly reports RCE, but their conditions are called out in Evidence limits. Exclusions and leads below do not count toward 55. This is not an exhaustive catalogue of all RCE vulnerabilities.

## Scope and evidence rules

Included paths cover HTTP and other network-facing services, API and RPC inputs, webhooks, message consumers, management interfaces, user-supplied templates, remote model/configuration processing, and asynchronous or cluster workers when a remote-controlled path reaches them. A command-line library or worker is included only when the source documents a network service path or the package is commonly embedded in such a path and that limitation is explicit.

For each case, the record preserves:

- a stable CVE or GHSA identifier and the product/version range reported by the source;
- source type/status and a direct source link, with publication and consultation dates;
- a concise paraphrase of the remote input-to-execution path and required role/configuration/reachability;
- the impact as stated by the source, a fix or explicit absence of a listed fix, and limits or conflicts in the evidence.

The source status distinguishes GitHub Reviewed advisories, maintainer-issued advisories, and vendor security advisories. A GitHub advisory may itself quote a researcher report; the record remains a paraphrase and points to the advisory. Duplicate upstream issues are counted once even when framework wrappers publish related notices. Distinct code paths in one product can remain separate when the public source identifies separate vulnerabilities and fixes.

Use the reported RCE impact as a claim to test against reviewed code, not as a universal impact guarantee. Confirm the exact package and release, enabled feature, account role, network exposure, worker/process identity, object or plugin availability, and later execution trigger. A dangerous API call or a dangerous dependency by itself is not a confirmed remote RCE.

## Case files

- [Command and process execution](cases/command-and-process-execution.md)
- [Dynamic code and interpreter evaluation](cases/dynamic-evaluation.md)
- [Template and expression injection](cases/template-and-expression-injection.md)
- [Unsafe deserialization](cases/unsafe-deserialization.md)
- [Dynamic loading and execution chains](cases/dynamic-loading-and-execution-chains.md)
- [Research leads not counted in the minimum](leads.md)

## Research method and limitations

Sources were selected from vendor or maintainer security advisories and GitHub-reviewed advisory records. Each counted source was opened and read on the consultation date recorded in its case. Search result titles were used to discover leads only; they are not evidence for counted records. The summaries avoid reproducing exploit payloads or full advisory text.

The corpus spans different publication years, products and source detail levels. Some advisories disclose a sink but not a complete route; some require a privileged role, special configuration, a compromised queue, a compatible gadget, a vulnerable parser mode, or a later file/module load. These conditions are recorded rather than generalized away. Version ranges and fixes can change; revisit the linked primary source and upstream release notes before using this as a current vulnerability inventory.

No target application, exploit, payload, scanner, or runtime reproduction was executed while collecting these records.

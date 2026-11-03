# rce-static-review

This installable skill guides source-only review for remote code execution across Web applications and network-facing services. It covers process execution, dynamic evaluation, server-side templates and expressions, unsafe deserialization, dynamic loading and deferred execution chains.

## Installation

From the skill repository:

```bash
npx skills add lahaxearnaud/agent-skills --skill rce-static-review --agent codex opencode --yes
```

To see available skills, use `npx skills add lahaxearnaud/agent-skills --list`. A local checkout can be used with `npx skills add . --list`. Exact destinations and agent discovery vary with the `skills` CLI version; copy the complete `rce-static-review` directory, including `references/`, when staging it manually.

For a machine without Internet access, copy this whole directory in advance into a skill location supported by the target agent. The workflow and technical references remain usable offline; external links inside `references/offline-sources.md` are provenance/update pointers, not review-time requirements.

## Use

Example: “Use `rce-static-review` to review this repository for remotely reachable RCE paths. Do not execute the application or run scanners.” The skill responds in the user's language and does not run the application, exploit payloads, target network requests or active scanners.

## Skill references and maintainer corpus

The installed package contains its operational workflow and attributed offline summaries under `references/`. It does not depend on the larger source research corpus. Maintainers can find 55 source-checked cases, source-status labels, leads and research notes at `corpus/security/remote-code-execution/`; that corpus is for learning, regeneration and updates, not a requirement for audits. The corpus count is a dated minimum, not an exhaustiveness claim.

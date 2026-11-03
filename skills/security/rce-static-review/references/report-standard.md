# RCE static-review report standard

Use this format for each distinct finding. Do not combine unrelated source-to-sink paths into one finding merely because the sink family is the same.

## Title

`[Evidence status] [RCE family]: [remote input] reaches [execution boundary]`

Evidence status must say **Static flow established**, **Candidate / incomplete**, or **Not an RCE path**. Do not describe a source-only finding as a runtime-confirmed exploit.

## Finding

- **Family:** process/shell, argument semantics, dynamic evaluation, template/expression, deserialization, or loading/deferred chain.
- **Evidence status and confidence:** explain the exact condition supporting the status.
- **Source and reachability:** remote entry point, required actor/role, and route/queue/configuration evidence.
- **Flow:** source → transformations/storage/queue → execution sink. Identify the parser/interpreter used at each boundary.
- **Code evidence:** repository-relative file and line for each critical edge; include dependency/API and version where visible.
- **Preconditions:** platform, version, feature flags, authentication, sandbox/filter state, gadget/object availability, worker trigger, filesystem path and privileges.
- **Impact supported:** what the affected process could do based on reviewed code and documented configuration. Mark unknowns explicitly.
- **Why controls do not break the path:** describe the actual validation/escaping/allowlist/sandbox and any missing or bypassable edge. If no control exists, say that.
- **Remediation:** remove the execution primitive where possible; otherwise restore code/data separation, constrain capabilities, validate intended semantics, isolate and least-privilege the consumer.
- **Evidence limits / unknowns:** deployment facts or unavailable source that prevent stronger claims.
- **Related corpus pattern:** optional case ID for context, explicitly not evidence about this application.

## Candidate wording

Use candidate wording when a dangerous sink is present but a necessary link is not proven. Example: “A user-controlled template is stored and a rendering call is present, but this review did not locate the reachable route that selects the stored template; server-side execution is not established.” State what evidence would resolve the gap, without running the target.

## Impact language

Do not infer root/system access, tenant compromise, persistence, secret theft or network pivoting from “arbitrary code execution” alone. State the process identity, filesystem/secret/network access only when code or deployment files show them. Separate source claims in historical advisories from the impact established in the reviewed repository.

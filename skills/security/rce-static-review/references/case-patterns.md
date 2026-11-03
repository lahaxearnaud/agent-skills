# Case patterns for static review

These are concise, source-attributed pattern summaries from the separate research corpus. They are prioritization aids, not proof that another repository shares the same vulnerability. Conditions and product versions remain case-specific; see the corpus during maintenance, but it is not required to install or use this skill.

## Process execution

- **simple-git CVE-2026-102826:** a remote-controlled repository/configuration path can alter Git's include configuration and reach a secondary command path. Review command wrappers and options, not only the shell flag. Does not imply every `git` argument is a shell injection.
- **pgAdmin CVE-2025-12762:** remote inputs to a server-side command path make authorization and server deployment conditions material. Do not transfer impact to clients or installations without the vulnerable configuration.
- **Kopia CVE-2026-45695:** a remotely reachable API path to a process operation illustrates that a server-side API's authorization and argument assembly must be traced together.

## Dynamic evaluation

- **n8n CVE-2025-68613:** expressions in workflow data cross an evaluation boundary; inspect which workflow author can set them and where execution occurs.
- **Flowise CVE-2025-55346:** dynamic code behavior in an exposed flow feature is conditional on the application wiring and reachable flow configuration.
- **Confluence CVE-2022-26134:** server-side expression evaluation in a Web request path illustrates why endpoint reachability and the actual expression context matter.

## Template and expression injection

- **Grav CVE-2024-28116 and CVE-2025-66294:** separate sandbox weaknesses in the same product across different versions; distinguish a sandbox escape from an untrusted template-source path and do not merge distinct fixes.
- **Fides CVE-2024-45053:** a saved message template is evaluated on a later email operation, so the write route and render trigger are distinct edges.
- **OpenBoxes GHSA-8wxj-vghp-jpcq:** a user with upload capability and a lower-privilege renderer can form a two-actor chain. Check both identities and the document type boundary.
- **Craft CMS CVE-2026-28695:** Twig object construction reaches a process class; the template capability and privileged authoring route are preconditions.

## Unsafe deserialization

- **Apache MINA CVE-2024-52046:** a reachable serialized network path can turn a parser weakness into server execution; review protocol and serialization switches, not only the Java dependency.
- **BentoML CVE-2025-27520 / CVE-2025-32375:** separate services and endpoints expose deserialization paths; do not treat product-family similarity as a shared reachability proof.
- **Laravel GHSA-qm5c-m76r-2hfr:** client-controlled cookie/session material can create an oracle or object handling path; distinguish integrity/authentication conditions from a fully established RCE gadget chain.
- **React Server Components CVE-2025-55182:** a network request reaches framework serialization/flight handling; wrappers and downstream integrations may repackage the same upstream flaw and should not be counted as distinct incidents.

## Dynamic loading and deferred chains

- **NocoBase GHSA-ghvf-qf6h-g8x5:** a writable artifact followed by a loader creates an execution chain; show both source and later consumer.
- **Rasa CVE-2024-49375:** remotely selected model loading makes model provenance and loader format part of the path.
- **FUXA CVE-2026-25895 / Fluentd CVE-2026-44024:** arbitrary write can be a conditional RCE primitive only when the chosen file is executable or later loaded.
- **Apache Struts CVE-2024-53677:** upload traversal leads to RCE under documented interceptor and configuration conditions; upload alone is insufficient.
- **VMware vCenter CVE-2021-21972:** a default-shipped service/plugin path shows why exposure, installed component and version are deployment facts to verify.

## Negative and incomplete patterns

- Remote input to a fixed executable's argument array is not shell injection unless an argument changes the called program's semantics or invokes a secondary interpreter.
- Fixed code evaluated by an interpreter is not injection merely because the API is named `eval`.
- User content inserted as data in a trusted Twig/Jinja template is not SSTI unless it is recompiled as template source.
- Deserialization without remotely controllable bytes or an executable object path remains a candidate, not proven RCE.
- Arbitrary file write without a reachable later loader, interpreter, worker or operator trigger is not RCE.
- A network worker with no demonstrated producer/reachability link is not a remote path.

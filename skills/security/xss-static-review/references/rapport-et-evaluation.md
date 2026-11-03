# Static report and evidence criteria

## Evidence classification

- **Statically established flow:** the actor and controllable source, transformations, and sink are connected in code; reachability and conditions are supported by visible evidence, including the page loading the client script and the effective source-to-sink connection. This remains a static conclusion, not observed browser execution.
- **Candidate requiring further reading:** a plausible sink or path exists but source, connection, protection, configuration, or scope is missing. State precisely what to look for; do not present it as a confirmed vulnerability.
- **Ruled out with reason:** a constant, unreachable path, ordinary text output, or protection demonstrated for that context. Do not call it a false positive if a link remains unknown.

A source and sink in the same file do not prove a connection. Static analysis does not prove triggering, browser execution, data theft, or CSP bypass. Do not call a purely static result “confirmed exploitation.”

## Finding template

For each relevant finding provide:

1. **Title and status:** statically established flow or candidate; assign severity only when supported and state assumptions.
2. **Source and actor:** file:line, proven or assumed control, and required privileges.
3. **Path:** file:line for each transformation and inter-file connection; persistence and reader where applicable.
4. **Sink and final context:** file:line, HTML/attribute/URL/script/SVG/DOM, mechanism, and absent, mismatched, or unknown protection.
5. **Scope:** reflected or stored if established; DOM mechanism where applicable; self/third-party/unknown reach separately, victim role, and interaction.
6. **Conditions and impact:** browser, origin, CSP/Trusted Types, and cookies **if visible**; unestablished behavior and conditional consequences. Do not promise RCE, cookie theft, or account takeover without a documented chain.
7. **Remediation:** concrete choice at the final sink, URL validation, contextual sanitization, document isolation, or upgrade as appropriate. Do not weaken CSP.
8. **Static validation after remediation:** what code to reread and which alternative paths to inspect. Do not propose application tests or runtime probes; if the available code cannot resolve uncertainty, preserve it.

## Coverage summary

State the scope and files actually reviewed, technology, available configuration and dependencies, static tools actually used, uncovered surfaces, and limitations. If nothing is established, say “no XSS flow was established in the reviewed scope” rather than “no XSS.” Group occurrences with a common root cause while referencing each relevant sink.

## Mini verification grid

- HTML-escaped `javascript:` link: candidate if scheme validation and control are not established; interaction may be required.
- `v-html` on a trusted constant: not a controllable XSS flow without further evidence.
- `sanitize(x) + userInput` sent to `innerHTML`: the second part is not covered; also trace actor and page access.
- `location.hash` to `textContent` on an ordinary element: do not report HTML injection unless a later dangerous use is demonstrated.
- A marker reflected in encoded text: not evidence of execution.
- A value inside a nonce-bearing script or a page with unknown CSP: do not conclude that CSP blocks or allows a vector without the effective policy.
- A value editable only by its owner: classify as self or unknown reach only after looking for sharing, privileged readers, imports, and third-party writes; do not assume a CSRF chain.

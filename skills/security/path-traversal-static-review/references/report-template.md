# Finding report template

Use this compact structure and omit fields that are genuinely unavailable only by marking them unknown.

```markdown
## [Status] Short title

- **Location:** file and relevant function/route
- **Source:** actor-controlled value and why it is untrusted
- **Flow:** source → transformations → guard (or missing guard) → exact filesystem sink
- **Conditions:** route/auth/config/version/OS/filesystem/permissions required
- **Impact:** read, write, delete, metadata, template/resource, or recipient-side archive consequence
- **Evidence level:** source-supported path escape / candidate / no traversal shown / insufficient evidence
- **Confidence:** explain what is directly visible and what depends on deployment
- **Severity:** only if supported by the repository rubric and proven exposure/impact; otherwise unassigned
- **Remediation:** server-owned identifier or final path-aware confinement; address symlinks/races where relevant
- **Unknowns:** specific code/configuration facts needed to confirm or narrow the result
- **Validation boundary:** source review only; no target runtime, browser, payload, scanner, or network test
```

Avoid generic claims such as “arbitrary file read” when only an existence check is shown. Name the directory boundary that is escaped and which operation observes the result. Cite a published CVE only as a pattern or dependency-version signal; it does not prove the current project is vulnerable.

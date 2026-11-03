# Research leads and exclusions

The following items are useful for future research or for teaching scope boundaries, but are **not included in the 55-case minimum**. A lead is not evidence that every application using a package is remotely exploitable.

## Requires an application-level remote path

### NLTK TransitionParser unsafe pickle loading — CVE-2026-78683

Source: [NLTK GHSA-rhp5-r9x4-f5g2](https://github.com/nltk/nltk/security/advisories/GHSA-rhp5-r9x4-f5g2) — GitHub Reviewed advisory, consulted 2026-11-03.

The advisory documents unrestricted pickle loading of a model file in TransitionParser and reports code execution. Its described entry point accepts a filesystem model path; the advisory does not establish a general network endpoint that lets a remote user supply that file. Count it for a service review only after tracing a real upload, model-import, or remote-processing path to that loader.

### MONAI pickle_operations — CVE-2025-58757

Source: [MONAI GHSA-p8cm-mm2v-gwjm](https://github.com/advisories/GHSA-p8cm-mm2v-gwjm) — GitHub Reviewed advisory, consulted 2026-11-03.

The advisory shows untrusted pickle bytes in transform metadata reaching a helper. It does not identify a standard web route that carries those bytes to the helper. Treat it as a candidate only when reviewed application code accepts that data remotely.

### Apache Trestle recursive template rendering — CVE-2026-46439

Source: [Trestle GHSA-gg2g-p7xc-qqmm](https://github.com/advisories/GHSA-gg2g-p7xc-qqmm) — GitHub Reviewed advisory, consulted 2026-11-03.

The report concerns user data that is recursively compiled as Jinja template text in compliance artifacts and can execute commands. Its described trigger is processing a submitted SSP/LUT in a CLI or CI-style workflow, not a general remotely reachable web service. Revisit if the application remotely configures or triggers that worker.

## Source status or RCE scope is insufficient

### Amidaware Tactical RMM report — CVE-2025-69516

Source: [GHSA-8g9w-79w6-cw84](https://github.com/advisories/GHSA-8g9w-79w6-cw84) — unreviewed GitHub advisory, consulted 2026-11-03.

The advisory describes a low-privilege report-template SSTI/RCE claim. It is retained as an unreviewed lead until a maintainer or vendor source confirms the code path, affected range, and fix.

### pyLoad CAPTCHA evaluation — CVE-2025-53890

Source: [pyLoad GHSA-8w3f-4r8f-pf53](https://github.com/advisories/GHSA-8w3f-4r8f-pf53) — GitHub Reviewed advisory, consulted 2026-11-03.

The advisory title is XSS and the reported code passes CAPTCHA output to browser-side JavaScript eval. It additionally says server RCE may be possible in a Node.js environment, but the described primary effect is browser code execution and the advisory does not establish a normal server-side Node execution path. It is not counted as RCE here.

### CVE-2024-4577 PHP-CGI argument injection

Source: [PHP 8.1.29 release announcement](https://news-web.php.net/php.announce/428) and [PHP 8.3.8 release announcement](https://news-web.php.net/php.announce/429), consulted 2026-11-03.

The PHP release notes confirm the security fix but the pages consulted for this corpus do not provide enough technical detail to qualify the exact remote input, platform/code-page conditions, and execution effect as a complete case record. Research the PHP security issue and vendor configuration notes before adding it.

## Research backlog

For every lead to move into the case files, capture a primary source with a stable identifier, affected/fixed versions, an explicit input-to-execution path, all required deployment and privilege conditions, the source's impact claim, and evidence limits. Do not promote a lead based on a search result snippet alone.

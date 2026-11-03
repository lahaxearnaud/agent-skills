# Corpus cases and variant analysis

The references below illustrate mechanisms confirmed by their authors. They do not show that an audited project is vulnerable. Compare version, configuration, source, path, role, and sink; if an advisory or fix is unavailable locally, do not invent its details.

| Pattern | Source case | Review question |
|---|---|---|
| HTML escaping followed by DOM decoding and HTML insertion | [AVideo — GHSA-wfq5-qgqp-hvhv](https://github.com/WWBN/AVideo/security/advisories/GHSA-wfq5-qgqp-hvhv) | Does escaped JSON or HTML data later reach `innerHTML`? |
| `raw` and the same values in multiple interfaces | [Sylius — GHSA-mx4q-xxc9-pf5q](https://github.com/Sylius/Sylius/security/advisories/GHSA-mx4q-xxc9-pf5q) | Does entity data cross macros, breadcrumbs, and admin components? |
| Logs or files rendered in a debug UI | [Symfony — GHSA-hmr5-2xcr-v8pp](https://github.com/symfony/symfony/security/advisories/GHSA-hmr5-2xcr-v8pp) | Do all rendering branches escape data, and who can write/read the file? |
| Filter declared safe for too many contexts | [Twig — GHSA-jv8m-2544-3pg3](https://github.com/twigphp/Twig/security/advisories/GHSA-jv8m-2544-3pg3) | Does the `is_safe` guarantee match the input and final context? |
| URL attribute not covered by protection | [Symfony HtmlSanitizer — GHSA-hhg7-c65m-h7ff](https://github.com/symfony/symfony/security/advisories/GHSA-hhg7-c65m-h7ff) | Does the configuration allow the affected tags/attributes and schemes? |
| SVG from an external source | [Symfony UX Icons — GHSA-6v8j-33hc-mv84](https://github.com/advisories/GHSA-6v8j-33hc-mv84) | Who controls the icons and how is the SVG rendered? |
| Data in a script already authorized by a nonce | [Adminer — GHSA-h6jr-7pr6-grgj](https://github.com/vrana/adminer/security/advisories/GHSA-h6jr-7pr6-grgj) | Is external metadata inserted into JS? Does a validation failure branch pass the input through? |
| Stored message in Vue | [Chamilo — GHSA-ppw9-gf4r-5c39](https://github.com/chamilo/chamilo-lms/security/advisories/GHSA-ppw9-gf4r-5c39) | Can a write by one role reach `v-html` viewed by another? |
| Intermediate rendering before sanitization | [Grafana — GHSA-7rqg-hjwc-6mjf](https://github.com/advisories/GHSA-7rqg-hjwc-6mjf) | Does a render state or preview use the value before transformation? |
| Rich HTML or SVG served as a document | [Open WebUI — GHSA-v2qm-5wxj-qhj7](https://github.com/advisories/GHSA-v2qm-5wxj-qhj7) | Does a neighboring endpoint still serve an active document on the application origin after a fix? |
| SVG and fallback when sanitizer fails | [FreeScout — GHSA-cvr8-cw5c-5pfw](https://github.com/freescout-help-desk/freescout/security/advisories/GHSA-cvr8-cw5c-5pfw) | Does an error lead to acceptance of less safe output? |
| Markdown/diagram and intermediate measurement | [Mermaid — GHSA-7rqq-prvp-x9jh](https://github.com/mermaid-js/mermaid/security/advisories/GHSA-7rqq-prvp-x9jh) | Does label measurement or SVG generation create a sink before final rendering? |
| Uncovered JSON or WebSocket branches | [AVideo — GHSA-2fhx-q92v-5fhv](https://github.com/advisories/GHSA-2fhx-q92v-5fhv) | Can an alternative key bypass validation applied to one branch only? |
| Trust state after mutation | [Rails — GHSA-89vf-4333-qx8v](https://github.com/rails/rails/security/advisories/GHSA-89vf-4333-qx8v) | Does a transformation incorrectly preserve a safety marker? |
| Infrastructure data in an admin table | [Froxlor — GHSA-43gm-9rr3-cx7g](https://github.com/advisories/GHSA-43gm-9rr3-cx7g) | Does business-format validation incorrectly allow raw HTML into a privileged screen? |
| Self-XSS with limited reach | [Nextcloud Deck — GHSA-mg7w-x9fm-9wwc](https://github.com/nextcloud/security-advisories/security/advisories/GHSA-mg7w-x9fm-9wwc) | Can another account actually receive the value, or is the reach unknown/limited? |

## Find variants around a finding

1. Search other fields and components using the same helper, renderer, filter, or endpoint; include admin, preview, error, and export pages.
2. Search alternative data paths: JSON/forms, competing message keys, storage then reading, SSR and client calls.
3. Verify different contexts of the same output: text, URL attribute, script, SVG, standalone document.
4. Inspect error branches, fallbacks, versioning, encoding, and sanitizer pre/post-processing.
5. Distinguish each statically confirmed variant from a lead with a missing link; do not multiply findings for the same root path without explaining the affected surfaces.

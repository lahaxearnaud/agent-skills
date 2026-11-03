# dynamic loading and execution chains

### CVE-2026-25895 — FUXA upload path traversal to later execution

**Family:** Arbitrary file write and conditional execution chain
**Product / versions:** fuxa-server <= 1.2.9; fixed 1.2.10
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-25895 advisory](https://github.com/advisories/GHSA-88qh-cphv-996c)
**Published:** 2026-02-04
**Consulted:** 2026-11-03
**Remote input / path to execution:** An unauthenticated upload path traversal permits writes outside the intended directory; execution follows only if a written path is application code, startup configuration, plugin or another later-loaded file.
**Preconditions:** All deployments are affected by the write flaw, including secureEnabled deployments. RCE depends on the process being able to overwrite a file that is later executed or loaded.
**Impact reported:** The advisory calls the issue RCE but describes execution as likely when an executable or loaded file can be overwritten.
**Fix:** Upgrade to 1.2.10 or later and canonicalize upload destinations below an application-controlled directory.
**Evidence limits:** The advisory confirms arbitrary file write; its execution consequence is conditional on deployment paths and later loading, so do not report upload alone as proven RCE.

### GHSA-ghvf-qf6h-g8x5 — NocoBase storage redirection plus plugin require

**Family:** Arbitrary write chained with dynamic module loading
**Product / versions:** @nocobase/server < 2.1.5; fixed 2.1.5
**Source status:** GitHub Reviewed advisory
**Source:** [GHSA-ghvf-qf6h-g8x5 advisory](https://github.com/advisories/GHSA-ghvf-qf6h-g8x5)
**Published:** 2026-06-15
**Consulted:** 2026-11-03
**Remote input / path to execution:** An admin changes the storage documentRoot to an arbitrary path, uploads a file there, then invokes a plugin-manager endpoint that calls Node require on an attacker-selected absolute path.
**Preconditions:** An authenticated admin session is required for both the storage update/upload and plugin enable path; the advisory notes default Docker process privileges can be high.
**Impact reported:** The chain executes attacker-written JavaScript in the NocoBase server process.
**Fix:** Upgrade to 2.1.5 or later and constrain storage roots and plugin module paths independently.
**Evidence limits:** The impact depends on both flaws being reachable in the same deployment; arbitrary file write or require alone is not the complete chain.

### CVE-2024-49375 — Rasa remote model loading

**Family:** Untrusted model artifact loading
**Product / versions:** Rasa Open Source < 3.6.21; Rasa Pro branch fixes 3.8.18, 3.9.16 and 3.10.12
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2024-49375 advisory](https://github.com/advisories/GHSA-cpv4-ggrr-7j9v)
**Published:** 2025-01-14
**Consulted:** 2026-11-03
**Remote input / path to execution:** A remotely supplied model is loaded by affected Rasa components and can trigger code execution during model deserialization/loading.
**Preconditions:** HTTP API must be enabled, which is not default. Unauthenticated exploitation requires no authentication or other recommended controls; authenticated exploitation requires a valid token or JWT.
**Impact reported:** Remote code execution in the Rasa process.
**Fix:** Upgrade to the fixed release for the deployed edition and retrain models with the fixed version.
**Evidence limits:** The network path is configuration dependent; the API is not enabled by default and authentication changes the attacker precondition.

### CVE-2025-67489 — Vite RSC development server unsafe dynamic imports

**Family:** Request-controlled dynamic module loading
**Product / versions:** @vitejs/plugin-rsc <= 0.5.5; fixed 0.5.6
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2025-67489 advisory](https://github.com/advisories/GHSA-j76j-5p5g-9wfr)
**Published:** 2025-12-08
**Consulted:** 2026-11-03
**Remote input / path to execution:** HTTP headers and body reach RSC server function APIs whose development implementation dynamically imports a module selected from request data.
**Preconditions:** A network-reachable Vite development server must run an RSC app exposing server-function endpoints; risk is higher when bound to all interfaces.
**Impact reported:** Arbitrary JavaScript execution with Node.js process privileges.
**Fix:** Upgrade to 0.5.6 or later and do not expose the development server to untrusted networks.
**Evidence limits:** The advisory is specific to the development server and unsafe dynamic imports; it is separate from the upstream React Flight deserialization CVE.

### CVE-2026-44024 — Fluentd tag-derived output path traversal

**Family:** Network log input to arbitrary file write
**Product / versions:** Fluentd <= 1.19.2; fixed 1.19.3
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-44024 advisory](https://github.com/advisories/GHSA-44hj-4m45-frj3)
**Published:** 2026-06-26
**Consulted:** 2026-11-03
**Remote input / path to execution:** An untrusted log tag is substituted into an output file path; inadequate validation plus formatting options permit traversal and arbitrary file overwrite.
**Preconditions:** The instance must accept logs from untrusted sources and use tag expansion in a file output path with affected formatting options.
**Impact reported:** Arbitrary file write that can become RCE by overwriting a system file, executable plugin or configuration later loaded by Fluentd.
**Fix:** Upgrade to 1.19.3 or later; avoid tag expansion from untrusted sources and run Fluentd with least privilege.
**Evidence limits:** The advisory describes RCE as a consequence of a write primitive and configuration-dependent target file; confirm an executable follow-on path.

### CVE-2026-25539 — SiYuan copyFile arbitrary destination

**Family:** Arbitrary file write with later execution
**Product / versions:** SiYuan kernel affected through build d5d10dd41b0c; advisory identifies 3.5.3 and likely earlier; no patched version listed in the advisory at consultation
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-25539 advisory](https://github.com/advisories/GHSA-c4jr-5q7w-f6r9)
**Published:** 2026-01-28
**Consulted:** 2026-11-03
**Remote input / path to execution:** The authenticated copyFile API validates the source but accepts an unrestricted destination path, allowing a file already in the workspace to be copied outside it.
**Preconditions:** A valid API token is required. RCE requires a destination that will be executed later by a scheduled task, login shell, loader or explicit operator action.
**Impact reported:** The advisory reports RCE through persistence or later execution; a successful file write alone does not execute the copied file.
**Fix:** No fixed version was listed in the advisory as of consultation; canonicalize destination paths and restrict allowed roots.
**Evidence limits:** The advisory's RCE demonstration invokes the written script separately; record the later execution condition rather than claiming copyFile executes it immediately.

### CVE-2024-53677 — Apache Struts upload path traversal to executable file

**Family:** Upload and path-based execution chain
**Product / versions:** Struts 2.0.0–2.3.37, 2.5.0–2.5.33 and 6.0.0–6.3.0.2; fixed from 6.4.0 with the new Action File Upload mechanism
**Source status:** Apache Struts vendor advisory
**Source:** [CVE-2024-53677 advisory](https://cwiki.apache.org/confluence/spaces/WW/pages/327979397/S2-067)
**Published:** 2024-12-18
**Consulted:** 2026-11-03
**Remote input / path to execution:** Manipulated file-upload parameters can enable traversal, placing an uploaded file outside its intended directory; under some conditions a malicious file can then be used for RCE.
**Preconditions:** The application must use the legacy FileUploadInterceptor; Apache says applications not using it are safe. Actual execution depends on the uploaded file's destination and handler.
**Impact reported:** Remote code execution only when the uploaded file is later handled as executable content.
**Fix:** Upgrade to Struts 6.4.0 or later and migrate to Action File Upload.
**Evidence limits:** The vendor explicitly qualifies RCE as conditional and excludes applications not using the old interceptor.

### CVE-2021-21972 — VMware vCenter plugin remote execution

**Family:** Network-reachable plugin execution path
**Product / versions:** vCenter Server 7.0 before U1c, 6.7 before U3l and 6.5 before U3n; Cloud Foundation fixed versions 4.2 and 3.10.1.2
**Source status:** Vendor advisory
**Source:** [CVE-2021-21972 advisory](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/23599)
**Published:** 2021-02-21
**Consulted:** 2026-11-03
**Remote input / path to execution:** A vulnerable vCenter Server plugin reachable through the vSphere Client endpoint provides a remote command execution path on the underlying host.
**Preconditions:** An attacker needs network access to port 443; the affected plugin is present in default installations even without vROPs installed.
**Impact reported:** Command execution with unrestricted privileges on the vCenter host, according to the vendor advisory.
**Fix:** Apply the fixed release for the deployed vCenter or Cloud Foundation branch and disable the affected plugin as a temporary mitigation.
**Evidence limits:** This is a plugin exposure case, not evidence that a particular application upload flow is required; the advisory identifies the vROPs-related plugin as shipped by default.


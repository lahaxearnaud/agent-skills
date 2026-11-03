# command and process execution

### CVE-2026-42076 — Evolver shell command construction

**Family:** OS command injection
**Product / versions:** @evomap/evolver npm < 1.69.3; fixed 1.69.3
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-42076 advisory](https://github.com/advisories/GHSA-j5w5-568x-rq53)
**Published:** 2026-04-20
**Consulted:** 2026-11-03
**Remote input / path to execution:** User-derived snippet content flows through extractSignals into _extractLLM, is concatenated into a curl command, then reaches execSync.
**Preconditions:** GEP must be enabled and the service must process user-provided content; the source says userSnippet may be supplied by a user or compromised log input.
**Impact reported:** Shell command execution with the Node process privileges; broader host impact depends on that account and isolation.
**Fix:** Upgrade to 1.69.3 or later; use a non-shell HTTP client API and keep user data out of command strings.
**Evidence limits:** The advisory contains a demonstration; this summary omits it. A deployment must verify that GEP and the user-content path are enabled.

### GHSA-xp7j-h7jc-4w8p — Semaphore Git URL argument injection

**Family:** Argument injection through Git
**Product / versions:** Semaphore 2.18.12, 2.18.13, 2.18.16; fixed 2.18.20
**Source status:** Maintainer advisory on GitHub
**Source:** [GHSA-xp7j-h7jc-4w8p advisory](https://github.com/semaphoreui/semaphore/security/advisories/GHSA-xp7j-h7jc-4w8p)
**Published:** 2026-08-01
**Consulted:** 2026-11-03
**Remote input / path to execution:** A repository git_url from an HTTP body is passed as an argument to exec.Command("git") without option validation or an argument separator; Git interprets the attacker-controlled option and launches its upload-pack command through a shell.
**Preconditions:** A project Manager or Owner can add a repository and schedule polling; the default cmd_git client is sufficient. The command runs in the main server, even when jobs use remote runners.
**Impact reported:** Arbitrary command execution as the Semaphore server process; the advisory notes access to the master encryption key and project secrets.
**Fix:** Upgrade to 2.18.20 or later; validate repository protocols and put an explicit option terminator before untrusted operands.
**Evidence limits:** The advisory distinguishes argument injection from shell interpolation: exec.Command itself does not invoke a shell, but the Git option triggers one downstream.

### CVE-2026-30861 — WeKnora MCP stdio configuration

**Family:** Argument validation bypass to code execution
**Product / versions:** WeKnora >= 0.2.5, < 0.2.10; fixed 0.2.10
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-30861 advisory](https://github.com/advisories/GHSA-r55h-3rwj-hcmg)
**Published:** 2026-03-06
**Consulted:** 2026-11-03
**Remote input / path to execution:** MCP stdio command and arguments stored from a user configuration pass a command allowlist and argument blacklist; an unblocked npx execution option reaches Node evaluation.
**Preconditions:** Open registration permits an attacker to create an account, then configure an MCP stdio server. The advisory metadata gives 0.2.x ranges, while one prose paragraph says 2.0.x; use metadata and verify release history.
**Impact reported:** Arbitrary code execution with WeKnora process privileges.
**Fix:** Upgrade to 0.2.10 or later; validate executable, argument schema, environment and trust boundary at the process-launch sink.
**Evidence limits:** The advisory's prose has a version-prefix inconsistency; do not infer any different affected range from it.

### CVE-2026-105697 — Langflow MCP stdio command launch

**Family:** Shell command injection and unsafe process configuration
**Product / versions:** langflow >= 1.1.2 < 1.10.3; langflow-base >= 0.1.2 < 0.10.3; lfx < 1.10.3; fixed in 1.10.3 releases
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-105697 advisory](https://github.com/advisories/GHSA-w794-rj3p-xv45)
**Published:** 2026-09-28
**Consulted:** 2026-11-03
**Remote input / path to execution:** MCP server settings or embedded flow configuration supplies command and arguments; affected code wraps the command in bash -c and launches it when tools are listed or a flow connects.
**Preconditions:** A user must reach MCP settings or configure a flow component. With default development-only AUTO_LOGIN enabled, the advisory reports token access without credentials; with it disabled, an authenticated non-admin user can reach the path.
**Impact reported:** Arbitrary OS command execution as the Langflow process user.
**Fix:** Upgrade to 1.10.3 or newer; enforce the allowlist at the execution sink and avoid a shell wrapper.
**Evidence limits:** The advisory notes staged fixes: a REST-model check arrived earlier, while the final sink check and shell removal are in the fixed release.

### CVE-2026-27626 — OliveTin shell safety type and webhook bypasses

**Family:** Shell command construction
**Product / versions:** OliveTin before 0.0.0-20260222101908-4bbd2eab1532; fixed in that commit build
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-27626 advisory](https://github.com/advisories/GHSA-49gm-hh7w-wfvf)
**Published:** 2026-02-22
**Consulted:** 2026-11-03
**Remote input / path to execution:** A password-typed action argument bypasses shell safety checks, and a second webhook JSON extraction path inserts untyped values directly into a command passed to sh -c.
**Preconditions:** For the first vector, an authorized user may supply argument values to an administrator-defined action. The independent webhook vector is described as unauthenticated and skips the type check.
**Impact reported:** Arbitrary shell command execution with OliveTin service privileges.
**Fix:** Use the fixed build; replace shell-string templating with a fixed executable and discrete validated arguments, and validate webhook fields against an explicit schema.
**Evidence limits:** The advisory documents two separate sources to one shell sink; application configuration determines which vector is reachable.

### CVE-2026-54449 — LangBot MCP configuration process launch

**Family:** User-controlled process configuration
**Product / versions:** LangBot <= 4.10.5; no patched version listed in the advisory at consultation
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-54449 advisory](https://github.com/advisories/GHSA-3pvh-63gf-j9mw)
**Published:** 2026-06-04
**Consulted:** 2026-11-03
**Remote input / path to execution:** An authenticated user can add an MCP STDIO server configuration; StdioServerParameters launches its configured command as a subprocess.
**Preconditions:** A valid account is required; the advisory says an attacker may sign up or use credentials on a reachable instance. The advisory lists no patched package version as of consultation.
**Impact reported:** Arbitrary command execution on the LangBot host with service privileges.
**Fix:** No fixed version was listed in the advisory as of 2026-11-03; restrict MCP configuration to trusted administrators and disable unsafe STDIO registration until a vendor fix is confirmed.
**Evidence limits:** The public advisory describes the process boundary but does not document a patch; recheck upstream before using version-based remediation.

### CVE-2026-52806 — Gogs pull request branch name to git rebase option

**Family:** Argument injection in a Git operation
**Product / versions:** Gogs < 0.14.3; fixed 0.14.3
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-52806 advisory](https://github.com/advisories/GHSA-qf6p-p7ww-cwr9)
**Published:** 2026-06-19
**Consulted:** 2026-11-03
**Remote input / path to execution:** A pull request branch name reaches the git rebase command during the Rebase-before-merging flow and is parsed as an option that enables a command hook.
**Preconditions:** An authenticated user able to create a pull request can trigger the merge style; default open registration can make account creation public on some deployments.
**Impact reported:** Command execution as the Gogs process user, with access to repositories handled by that account.
**Fix:** Upgrade to 0.14.3 or later; validate branch names for option syntax and construct Git arguments with a safe boundary.
**Evidence limits:** The advisory discusses effective unauthenticated reachability only when registration is open; the code path itself requires a user-created pull request.

### CVE-2026-102826 — simple-git configuration include execution chain

**Family:** Git configuration injection and later command execution
**Product / versions:** simple-git <= 3.36.0; advisory lists 4.0.0 as patched
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-102826 advisory](https://github.com/advisories/GHSA-g4wm-2vf7-vfgr)
**Published:** 2026-09-26
**Consulted:** 2026-11-03
**Remote input / path to execution:** Attacker-influenced clone customArgs can select a local Git configuration include; that file can set core.sshCommand, which is invoked by a later remote operation.
**Preconditions:** An application must pass attacker-controlled customArgs and the selected local config file must be readable and contain attacker-controlled configuration. The advisory also identifies a pending denylist regex gap for includeIf.path.
**Impact reported:** A later Git operation can execute a command with the application process privileges.
**Fix:** Use a release with a complete include/includeIf denylist; do not expose arbitrary Git options or config paths to untrusted callers.
**Evidence limits:** The advisory links this denylist family to earlier fixes; it identifies a newly documented include path and a conditional-include bypass, not a duplicate of each earlier CVE.

### CVE-2026-45695 — Kopia SSH ProxyCommand injection

**Family:** SSH option injection into a shell-backed helper
**Product / versions:** Kopia <= 0.22.3; fixed 0.23.0
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-45695 advisory](https://github.com/advisories/GHSA-2q4c-3mrw-63c3)
**Published:** 2026-05-13
**Consulted:** 2026-11-03
**Remote input / path to execution:** An unauthenticated HTTP storage configuration supplies sshArguments; Kopia splits the string into argv and passes it to ssh, whose ProxyCommand option invokes a shell.
**Preconditions:** Kopia HTTP server must be started without a password and use the SFTP backend with externalSSH enabled; network access to the API is sufficient.
**Impact reported:** Arbitrary command execution as the Kopia process user; no user interaction or valid credentials are required in the described configuration.
**Fix:** Upgrade to 0.23.0 or later; require authentication on non-loopback interfaces and constrain SSH options.
**Evidence limits:** The command is executed by OpenSSH option semantics before a remote SSH connection is established; the initial Go exec.Command call is not itself a shell.

### CVE-2025-12762 — pgAdmin restore from a plain-format dump

**Family:** Command injection during server-mode restore
**Product / versions:** pgAdmin < 9.10; fixed 9.10
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2025-12762 advisory](https://github.com/advisories/GHSA-w2p4-p4rh-qcm3)
**Published:** 2025-11-13
**Consulted:** 2026-11-03
**Remote input / path to execution:** A plain-format dump processed by the restore feature reaches command execution on the pgAdmin server.
**Preconditions:** The deployment must run pgAdmin in server mode and expose restore functionality to an attacker with the required low-level restore permission; exact role details are not specified in the advisory.
**Impact reported:** Arbitrary command execution on the server hosting pgAdmin.
**Fix:** Upgrade to 9.10 or later; treat imported dump content as untrusted and avoid shell interpolation in restore commands.
**Evidence limits:** The advisory gives the mode and file-format conditions but limited code-path detail; verify the installed release and restore permission model.


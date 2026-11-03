# Isolated PoC test templates Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add reusable HTML/browser, JavaScript/Node, JavaScript/browser, and PHP CLI smoke templates to the isolated PoC skill.

**Architecture:** Keep templates inside the installable skill package under `templates/`. Each runnable example uses synthetic control/trigger inputs and emits two ordered JSON stdout records with the same prefix; browser examples use a small Node helper and local HTML files under the existing fixed Docker profile.

**Tech Stack:** Markdown, HTML, Node.js 22 built-ins, PHP 8 CLI, Python `unittest`, Docker runner, and the `skills` CLI.

**Spec:** `docs/superpowers/specs/2026-11-03-isolated-poc-test-templates-design.md`

## Global Constraints

- Keep the reviewed application and live endpoints out of the runtime harness.
- Do not reinstall or restore any application dependency graph; examples use built-in language functionality and preinstalled browser binaries only.
- Use the bundled runner, concrete image tags plus SHA-256 digests, no network, no host mounts, bounded resources and its existing non-root profile.
- Browser tests keep Chromium's default sandbox and report blocked when the fixed profile cannot launch the browser.
- Each smoke example emits `ISOLATED_POC_CASE=` JSON records in `control`, then `trigger` order; default smoke output is not a vulnerability verdict.
- Keep examples and workspaces within the existing 50-file, 200-entry and 5-MiB limits.
- Record an ADR because this adds a durable template structure and output contract to the skill.

## Review Focus

- **Browser startup under the fixed profile:** run the Playwright smoke template with the default Chromium sandbox; if the runtime blocks it, the helper must produce a clear blocked result without weakening isolation.
- **Predictable output:** all four templates emit exactly two parseable case records, with stable IDs and order; include an automated test for each.
- **Offline and dependency-free use:** manifests name only default-allowlisted images, no template invokes a package manager or external URL, and all needed helper files are bundled.
- **Scope clarity:** the HTML fixture observes parser/DOM output only; smoke output cannot be mistaken for application evidence or a confirmed vulnerability.

---

### Task 1: Add failing template contract tests

**Files:**
- Test: `maintenance/security/isolated-vulnerability-reproduction/test_templates.py`
- Modify: `maintenance/security/isolated-vulnerability-reproduction/test_run_poc_container.py` only if shared test setup needs an environment reset.

**Interfaces:**
- Consumes: the agreed four template identifiers and output contract from the spec.
- Produces: regression tests that locate each template's README/manifest/source files, validate image/argv shape, and run the language smoke harnesses through the existing runner when invoked as integration checks.

- [x] **Step 1: Write the failing integration tests** for all four templates; each test must run the real template through the constrained runner and assert ordered, parseable `control`/`trigger` records.
- [x] **Step 2: Run the focused tests** and confirm they fail because each template manifest is missing, before writing template files.

### Task 2: Create runnable, minimal templates

**Files:**
- Create: `skills/security/isolated-vulnerability-reproduction/templates/README.md`
- Create: `skills/security/isolated-vulnerability-reproduction/templates/html-browser/`
- Create: `skills/security/isolated-vulnerability-reproduction/templates/javascript-node/`
- Create: `skills/security/isolated-vulnerability-reproduction/templates/javascript-browser/`
- Create: `skills/security/isolated-vulnerability-reproduction/templates/php-cli/`
- Modify: `maintenance/security/isolated-vulnerability-reproduction/test_templates.py`

**Interfaces:**
- Consumes: the failing tests from Task 1 and the existing runner contract (`argv`, concrete pinned `image`, timeout).
- Produces: self-contained template folders with example manifests, editable candidate fixtures, instructions, and the shared stdout records.

- [x] **Step 1: Implement the Node and PHP smoke examples** using identity placeholder functions, synthetic marker inputs, two ordered JSON records, and manifest examples; keep runtime dependencies to Node/PHP built-ins.
- [x] **Step 2: Implement the HTML and JavaScript browser examples** with separate control/trigger HTML documents and one bundled Node helper that discovers the browser, runs `--headless --dump-dom` on local files, preserves the sandbox, and emits the shared JSON records.
- [x] **Step 3: Run every available smoke example through the bundled runner** with the exact cached or separately pulled allowlisted image; assert output records and distinguish browser startup failure as blocked. Node and PHP completed; Playwright could not create a VFS snapshot within available disk, and that limitation is recorded.
- [x] **Step 4: Run the focused template contract tests** and confirm available templates pass; browser tests skip when the image is not cached.

### Task 3: Integrate guidance, offline references, and ADR

**Files:**
- Modify: `skills/security/isolated-vulnerability-reproduction/SKILL.md`
- Modify: `skills/security/isolated-vulnerability-reproduction/README.md`
- Modify: `skills/security/isolated-vulnerability-reproduction/references/reproduction-workflow.md`
- Modify: `skills/security/isolated-vulnerability-reproduction/references/offline-sources.md`
- Modify: `maintenance/security/README.md`
- Modify: `maintenance/security/isolated-vulnerability-reproduction/evaluation.md`
- Modify: `AGENTS.md`, `README.md`
- Create: `docs/adr/0014-isolated-poc-test-templates.md`

**Interfaces:**
- Consumes: Task 2's directory names, stdout record prefix, manifests and browser-launch behavior.
- Produces: discoverable offline instructions, an accepted ADR-0014 indexed in `AGENTS.md`, and evaluation notes that distinguish smoke tests from vulnerability evidence.

- [x] **Step 1: Add ADR-0014** in French using the repository template; record the common output contract, runtime/surface split, offline packaging, and browser sandbox limit.
- [x] **Step 2: Link the templates from the skill workflow and package README** and state how to copy only the relevant minimal files, replace candidate code/inputs, and interpret smoke output.
- [x] **Step 3: Add a local Chromium headless source summary** to the skill's offline notes and update repository/maintenance documentation and the ADR index.
- [x] **Step 4: Verify all relative Markdown links, manifests, output examples and scope wording.**

### Task 4: Verify packaging and publish on `main`

**Files:**
- Verify all Task 1–3 files.
- Modify: `docs/superpowers/plans/2026-11-03-isolated-poc-test-templates.md` to mark completed steps.

**Interfaces:**
- Consumes: template tests, fixtures, instructions, ADR, and package metadata.
- Produces: one verified commit pushed to `origin/main`.

- [x] **Step 1: Run full Python tests, available template smoke runs, Markdown checks, `git diff --check`, `npx --yes skills add . --list`, and a temporary local CLI install with recursive byte comparison.** The test suite reports 40 passing and two browser skips; the browser image startup was also directly attempted and blocked by the daemon disk limit.
- [ ] **Step 2: Review the staged diff**, stage only the plan/spec, template package, tests, docs, ADR/index and maintenance changes, then commit on `main`.
- [ ] **Step 3: Confirm `origin/main` still equals the commit parent, push without force, and verify remote SHA and a clean worktree.**

---

## Self-Review

- **Spec coverage:** Four templates, common output, smoke-vs-finding distinction, offline package, browser restrictions, docs and ADR map to Tasks 1–4.
- **Step clarity:** Task 1 owns baseline tests; Task 2 owns all template files; Task 3 documents their published interface; Task 4 verifies and publishes.
- **Type/interface consistency:** All examples use `argv` arrays and a concrete pinned image; stdout records use the same `ISOLATED_POC_CASE=` prefix.
- **Review Focus:** Browser block, common output, offline dependencies, and scope boundaries each have explicit checks.
- **Proportion:** Four task boundaries cover tests, templates, docs/ADR, and repository integration.

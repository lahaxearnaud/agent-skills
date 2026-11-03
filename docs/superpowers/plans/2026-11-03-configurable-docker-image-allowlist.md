# Configurable Docker Image Allowlist Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restrict the isolated PoC runner to a built-in set of Docker image repositories or a user-supplied replacement allowlist, with wildcards confined to image tags.

**Architecture:** The Python runner reads `ISOLATED_POC_ALLOWED_IMAGES`; when absent it uses four built-in, fully qualified repository patterns, and when present it treats the comma-separated values as the complete allowlist. Patterns match the full registry/repository literally and permit `*` only in the tag; the manifest continues to require a concrete tag and SHA-256 digest.

**Tech Stack:** Python standard library, `unittest`, Markdown, Git, and the `skills` CLI.

**Spec:** `docs/superpowers/specs/2026-11-03-configurable-docker-image-allowlist-design.md`

## Global Constraints

- Built-in patterns are `docker.io/library/node:*`, `docker.io/library/php:8.*`, `docker.io/library/python:*`, and `mcr.microsoft.com/playwright:*`; PHP 7 is excluded from the built-in list.
- A defined `ISOLATED_POC_ALLOWED_IMAGES` replaces the built-in list; it is comma-separated, and an empty or malformed value fails closed.
- Each pattern has a complete, lowercase, Docker-unambiguous registry/repository path and a non-empty tag; the registry host has a dot, port, or exact `localhost` name, and the only wildcard is `*` within the tag.
- Manifest image references remain fully qualified `registry/repository:tag@sha256:<64 lowercase hex>` references; `latest` remains rejected.
- Private registries are permitted only through explicit user patterns; the runner still requires a locally cached digest match and forwards no allowlist environment variable into the container.
- Keep the existing no-network, no-host-mount, resource-limit, and disposable-PoC constraints unchanged.

## Review Focus

- **Unset variable:** only the four built-in patterns match; test default repositories and reject another Docker Hub Official Image and PHP 7.
- **User override:** a private-registry pattern replaces all defaults; test a custom image succeeds and a default-only image fails. Reject a bare single-label registry host while accepting dotted, port-qualified, and `localhost` hosts.
- **Tag wildcard boundary:** `*` matches tags only, not registries or repositories; test accepted `8.*` and rejected path wildcards.
- **Invalid configuration:** empty entries, malformed references, unsupported glob characters, or missing tags fail closed; test each case.
- **Registry port and names:** digest verification preserves ports such as `registry.example.test:5000`; test expected RepoDigest parsing. Accept Docker-valid repeated repository separators while rejecting ambiguous bare single-label registry names.

---

### Task 1: Implement allowlist parsing and matching in the runner

**Files:**
- Modify: `skills/security/isolated-vulnerability-reproduction/scripts/run_poc_container.py`
- Test: `maintenance/security/isolated-vulnerability-reproduction/test_run_poc_container.py`

**Interfaces:**
- Produces: `DEFAULT_ALLOWED_IMAGE_PATTERNS`, `ISOLATED_POC_ALLOWED_IMAGES`, a strict allowlist parser, and manifest validation that matches a pinned image against the effective patterns.
- Preserves: `validate_manifest(data) -> dict[str, Any]` and the existing manifest fields.

- [x] **Step 1: Add failing tests** for default matching (including PHP 7 rejection), environment replacement, private-registry exact and tag-wildcard matching, unambiguous registry hosts, valid repeated path separators, wildcard/path rejection, empty/malformed entries, missing registry/tag/digest, `latest`, and registry-port digest inspection.
- [x] **Step 2: Run the focused tests** with `python3 -m unittest maintenance.security.isolated-vulnerability-reproduction.test_run_poc_container.ManifestTests maintenance.security.isolated-vulnerability-reproduction.test_run_poc_container.DockerCommandTests -v`; confirm the new cases fail against the current runner.
- [x] **Step 3: Implement the parser and matcher** using literal registry/repository comparison and a full-string tag match where `*` is the only metacharacter. Reject Docker-ambiguous bare single-label hosts, retain valid repeated repository separators, read the environment override on the host only, and keep the manifest's concrete tag and digest checks.
- [x] **Step 4: Fix cached digest parsing for private registries** by separating the final tag colon after the last slash, preserving registry ports, and retaining the Docker Hub short-name alias for `docker.io/library/` images.
- [x] **Step 5: Run the full runner suite** with `python3 -m unittest discover -s maintenance/security/isolated-vulnerability-reproduction -p 'test_*.py' -v`; confirm all 38 tests pass both with the default environment and with a user replacement list set.

### Task 2: Document and record the image trust boundary

**Files:**
- Modify: `skills/security/isolated-vulnerability-reproduction/SKILL.md`
- Modify: `skills/security/isolated-vulnerability-reproduction/README.md`
- Modify: `skills/security/isolated-vulnerability-reproduction/references/reproduction-workflow.md`
- Modify: `skills/security/isolated-vulnerability-reproduction/references/offline-sources.md`
- Modify: `maintenance/security/isolated-vulnerability-reproduction/update-prompt.md`
- Modify: `maintenance/security/isolated-vulnerability-reproduction/evaluation.md`
- Modify: `README.md`, `AGENTS.md`
- Create: `docs/adr/0013-configurable-docker-image-allowlist.md`

**Interfaces:**
- Consumes: Task 1's exact environment variable and pattern grammar.
- Produces: consistent offline instructions, one accepted ADR-0013 indexed in `AGENTS.md`, and a maintainer record of the new tests.

- [x] **Step 1: Add ADR-0013** in French using the repository template; supersede ADR-0012 only for the image-source restriction and document the built-in fallback, user override, private registries, tag-only wildcard, and digest verification.
- [x] **Step 2: Update the skill package** with the four defaults, comma-separated replacement behavior, full registry/repository/tag requirement, tag-only `*` examples, `latest` rejection, and the private-registry digest workflow.
- [x] **Step 3: Update repository discovery** with the ADR index and a concise root README note for the environment override.
- [x] **Step 4: Update maintenance notes** with the new policy and test count; distinguish mocked registry inspection from a real private-registry integration test.
- [x] **Step 5: Check Markdown links and policy consistency** across the package, root README, ADR, and maintenance notes.

### Task 3: Verify packaging and publish on `main`

**Files:**
- Verify all files from Tasks 1–2.
- Modify: `docs/superpowers/plans/2026-11-03-configurable-docker-image-allowlist.md` to mark completed steps.

**Interfaces:**
- Consumes: the runner, documents, tests, and ADR.
- Produces: a verified commit pushed to `origin/main`.

- [x] **Step 1: Run final checks:** the full unittest command, `python3 -m py_compile` on the runner and its tests, `git diff --check`, Markdown link/frontmatter checks, `npx --yes skills add . --list`, and temporary local CLI installation with byte-for-byte comparison of package files.
- [x] **Step 2: Run harmless Node/PHP marker PoCs** through the unchanged fixed Docker profile if the exact cached official images are available; otherwise record the concrete blocker. Do not run a reviewed application or arbitrary private image.
- [x] **Step 3: Review the scoped diff**, stage only the plan/spec, runner/tests, skill documentation, ADR/index, README, and maintenance changes, then commit on `main`.
- [x] **Step 4: Confirm the remote `main` still equals the commit parent, push `origin main`, and verify the remote SHA and clean worktree.**

---

## Self-Review

- **Spec coverage:** Defaults, environment replacement, private registry support, tag-only patterns, digest pinning, documentation, ADR, packaging, and publication each map to a task above.
- **Step clarity:** Task 1 names the validator behavior and regression cases; Task 2 owns all user-visible policy and decision records; Task 3 verifies, commits, and pushes.
- **Type consistency:** `validate_manifest(data)` and its output shape remain unchanged; the allowlist is read from the host environment during validation.
- **Review Focus:** Each of the five inputs has an explicit test in Task 1.
- **Proportion:** The three tasks reflect one code boundary, one documentation/ADR boundary, and final repository integration.

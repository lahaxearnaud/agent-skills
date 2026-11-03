# Remote Code Execution Static Review Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add one installable, source-only RCE review skill backed by at least 40 distinct, source-checked public vulnerability cases.

**Architecture:** Keep one `rce-static-review` package with a short common workflow and family-specific references. Maintain the larger research corpus separately under `corpus/security/remote-code-execution/`; bundle attributed offline summaries and operational details inside the installable package.

**Tech Stack:** Markdown, Git, the `skills` CLI, and small one-off Python checks for link, metadata, and corpus-count validation. No target application or payload will be executed.

**Spec:** `docs/superpowers/specs/2026-11-03-rce-static-review-design.md`

## Global Constraints

- Include at least **40 distinct, source-checked public vulnerability cases**; search-result leads, labs, and synthetic examples do not count toward the minimum.
- Cover Web applications and network-facing server services; include RPC, webhooks, message consumers, and asynchronous workers when a network-controlled application path reaches them.
- Cover command/process execution, dynamic code or interpreter evaluation, template/expression injection, unsafe deserialization, and dynamic loading or later-executed file/job chains.
- Keep standalone CI/build infrastructure out of scope unless reviewed application code remotely configures or triggers the execution path.
- The installable skill is source-only: do not run the reviewed application, exploit payloads, active scanners, or target network requests.
- Write the skill, its operational references, and README in English; answer the user in French.
- Every external technical source cited by the installed skill must have an attributed local paraphrase in that package; retain source URLs for provenance and updates.
- Keep verified reports, unreviewed leads, intentional labs, and synthetic examples distinct; explicitly record unknown versions, conditions, and impacts.

## Review Focus

- Shell versus direct argument-vector process calls: a process sink alone must not be labeled shell injection; an evaluation scenario must distinguish shell parsing from a fixed executable and bound argument.
- Code-as-data versus dynamically evaluated input: constant expressions and safe parsing must not be reported as RCE; an evaluation scenario must require an attacker-controlled code path to a reachable interpreter.
- Template source versus template output: ordinary XSS/HTML output must not be mislabeled server-side template execution; an evaluation scenario must distinguish user-controlled template syntax from data inserted into a trusted template.
- Deserialization without an executable gadget path: unsafe deserialization is a candidate, not established RCE, until reachable behavior and version/class conditions are shown; an evaluation scenario must include a non-executable object path.
- File upload/write without later execution and asynchronous execution with missing reachability: an evaluation scenario must keep upload-only code and unlinked workers below an RCE finding.

## File Structure

- `docs/adr/0010-static-rce-review-scope.md` records the accepted skill scope and packaging decision; `AGENTS.md` indexes it.
- `corpus/security/remote-code-execution/README.md` documents the research method, counts, scope, evidence classes, and limitations.
- `corpus/security/remote-code-execution/cases/` groups source-checked reports by execution family; `leads.md` holds records not qualified for the 40-case minimum; `patterns-and-controls.md` and `standards-and-tools.md` capture reusable analysis and documented tool behavior.
- `skills/security/rce-static-review/SKILL.md` is the concise entry point. `references/` holds the common workflow, family guides, report standard, case patterns, and offline source summaries needed after installation.
- `maintenance/security/remote-code-execution/` holds the update prompt, evaluation scenarios, and actual evaluation results.
- Root `README.md`, `PROVENANCE.md`, and `AGENTS.md` expose the package and its maintenance conventions.

---

### Task 1: Record the accepted scope and repository decision

**Files:**
- Modify: `docs/superpowers/specs/2026-11-03-rce-static-review-design.md`
- Create: `docs/adr/0010-static-rce-review-scope.md`
- Modify: `AGENTS.md`

**Interfaces:**
- Consumes: the approved design and the 40-case minimum.
- Produces: an accepted ADR-0010 with the scope, source-only boundary, taxonomy, packaging, and corpus threshold; an ADR index entry with title and summary.

- [x] **Step 1: Update the design with the approved corpus minimum**

State that the minimum counts distinct public cases whose source was consulted and whose RCE path is sufficiently documented. Explicitly exclude leads, labs, and synthetic examples from the count.

- [x] **Step 2: Add ADR-0010**

Use the repository ADR template, date it `2026-11-03`, set status `Accepted`, link related ADRs 0001, 0002, and 0009, and record the web/server boundary plus inclusion rules for network-reachable workers.

- [x] **Step 3: Index ADR-0010 in `AGENTS.md`**

Use the next unused ADR number, exact title, Markdown file link, and one-sentence description.

- [x] **Step 4: Verify the decision record**

Run `git diff --check`; verify the ADR filename/number is unused, all referenced ADR files exist, and the local ADR index links to ADR-0010.

### Task 2: Research and qualify the 40-case corpus

**Files:**
- Create: `corpus/security/remote-code-execution/README.md`
- Create: `corpus/security/remote-code-execution/cases/command-and-process-execution.md`
- Create: `corpus/security/remote-code-execution/cases/dynamic-evaluation.md`
- Create: `corpus/security/remote-code-execution/cases/template-and-expression-injection.md`
- Create: `corpus/security/remote-code-execution/cases/unsafe-deserialization.md`
- Create: `corpus/security/remote-code-execution/cases/dynamic-loading-and-execution-chains.md`
- Create: `corpus/security/remote-code-execution/leads.md`

**Interfaces:**
- Consumes: the family taxonomy and evidence rules from ADR-0010.
- Produces: at least 40 distinct source-checked public cases, grouped by family, with an aggregate count and status by family in the README.

- [x] **Step 1: Define the case record fields in the corpus README**

Use the existing corpus conventions: stable CVE/GHSA/vendor identifier; product and affected versions; direct source and source type/status; publication and consultation dates; actor/input; source-to-sink or execution chain; required configuration, role, and reachability; source-attributed impact; fix; unknowns; and links to related or duplicate records. Mark fields unknown when the source does not establish them.

- [x] **Step 2: Search primary sources and publish cases by family**

Consult vendor/maintainer advisories, official CVE records where informative, public bounty disclosures, and issue tickets with enough technical detail. For each record, read the source rather than using a search title as evidence. Describe the relevant code path and conditions in original prose; do not reproduce full advisories or operational exploit payloads.

- [x] **Step 3: Reconcile identifiers and source status**

Deduplicate aliases for the same incident, link distinct bypasses or patch regressions, and move insufficiently documented reports to `leads.md`. Keep labs and synthetic examples out of these case files and out of the required count.

- [x] **Step 4: Verify the minimum and family coverage**

Run a one-off Python or shell check over the case records to count unique qualified identifiers. Expected result: at least 40 records remain after deduplication, each has a direct source and source-status label, and each execution family has either qualified cases or an explicit documented research gap.

### Task 3: Document reusable patterns, controls, and static-analysis tools

**Files:**
- Create: `corpus/security/remote-code-execution/patterns-and-controls.md`
- Create: `corpus/security/remote-code-execution/standards-and-tools.md`

**Interfaces:**
- Consumes: the qualified corpus from Task 2.
- Produces: evidence-backed family patterns, safe and negative examples, prevention guidance, and documented static analyzer/tool limits.

- [x] **Step 1: Synthesize patterns from qualified cases**

For each family, record the attacker-controlled source, transformation, interpreter/process boundary, applicable protection, enabling conditions, impact evidence, and a counterexample. Cite corpus cases or primary documentation for each reusable claim.

- [x] **Step 2: Inventory standards, framework APIs, and analyzers**

Document relevant CWE/OWASP material and official API guidance for process invocation, evaluation, templates, deserialization, and code loading. Include only static-analysis rules or scanner documentation useful to code review; record product/version, source/sink model, prerequisites, known gaps, and whether a technique was merely documented or actually run. No target scanner will be run.

- [x] **Step 3: Verify source attribution and scope separation**

Check that each documented tool behavior or prevention claim has a direct citation and that general RCE, injection, and local privilege-escalation labels are not treated as equivalent.

### Task 4: Build self-contained offline operational references

**Files:**
- Create: `skills/security/rce-static-review/references/workflow.md`
- Create: `skills/security/rce-static-review/references/command-and-process.md`
- Create: `skills/security/rce-static-review/references/dynamic-evaluation.md`
- Create: `skills/security/rce-static-review/references/template-and-expression.md`
- Create: `skills/security/rce-static-review/references/deserialization.md`
- Create: `skills/security/rce-static-review/references/loading-and-execution-chains.md`
- Create: `skills/security/rce-static-review/references/case-patterns.md`
- Create: `skills/security/rce-static-review/references/report-standard.md`
- Create: `skills/security/rce-static-review/references/offline-sources.md`

**Interfaces:**
- Consumes: the corpus patterns, primary source summaries, and documented tool models from Tasks 2–3.
- Produces: relative-linked references sufficient for the installed skill to conduct static review with the corpus and network unavailable.

- [x] **Step 1: Write family-specific evidence criteria**

Define candidate versus established-flow thresholds, common false positives, version/configuration conditions, and remediation themes for each RCE family. Keep process argument injection distinct from shell command injection, and code/data boundaries explicit for interpreters, templates, and deserializers.

- [x] **Step 2: Summarize every external operational source locally**

In `offline-sources.md`, add source name, original URL, relevant version/date, concise original paraphrase, applicable conditions, and limitations for each external document cited by package references. Keep URLs as provenance/update pointers; do not require browsing at review time.

- [x] **Step 3: Link examples without making the corpus a dependency**

Use representative local case-pattern summaries and relative links inside the skill package. Do not link operational instructions to `corpus/` paths or machine-specific locations.

- [x] **Step 4: Check local references**

Run a Markdown relative-link check over the package. Verify source citations outside `offline-sources.md` are present and summarized in that file, and mark any version-specific detail absent from local evidence as unknown.

### Task 5: Create the installable skill package

**Files:**
- Create: `skills/security/rce-static-review/SKILL.md`
- Create: `skills/security/rce-static-review/README.md`
- Modify: references created in Task 4 as needed.

**Interfaces:**
- Consumes: family guides and report standard from Task 4.
- Produces: the skill entry point named `rce-static-review` and a self-contained installation/readme experience.

- [x] **Step 1: Write the concise static-review workflow**

Include valid YAML frontmatter with `name: rce-static-review` and a `Use when ...` description. Require repository-instruction review, scope inventory, source-to-execution tracing across files and storage, control/version verification, evidence classification, impact limits, and a finding format with file:line evidence and unknowns. State that the skill does not execute the target or payloads and does not require Internet or corpus access.

- [x] **Step 2: Add triage and negative examples**

Include at least one safe/negative example and one incomplete candidate in the skill or linked references, covering the Review Focus list. State that a dangerous function name or deserialization call alone does not establish RCE.

- [x] **Step 3: Write the package README**

Document local and remote installation, offline staging/copying, the distinction between installed references and the maintainer corpus, and language behavior. Follow the repository's English skill documentation convention.

- [x] **Step 4: Validate skill metadata and package links**

Check that the skill folder and frontmatter names match, the description starts with `Use when`, and every relative Markdown link resolves.

### Task 6: Add maintenance and evaluation materials

**Files:**
- Create: `maintenance/security/remote-code-execution/README.md`
- Create: `maintenance/security/remote-code-execution/update-prompt.md`
- Create: `maintenance/security/remote-code-execution/evaluation-scenarios.md`
- Create: `maintenance/security/remote-code-execution/evaluation.md`

**Interfaces:**
- Consumes: the corpus format and installable skill from Tasks 2–5.
- Produces: a repeatable source-qualification/update process and recorded static retrieval evaluation.

- [x] **Step 1: Write a research and regeneration prompt**

Require primary-source reading, source status/date/version, deduplication, actor and sink conditions, a minimum of 40 retained distinct documented cases, updates to offline skill notes, rights review, and no active target testing. Leads, labs, and hypothetical examples must stay separate from the case minimum.

- [x] **Step 2: Create a balanced evaluation suite**

Write positive, negative, incomplete, and trust-boundary snippets for every family, plus a cross-family chain. Include shell and non-shell process cases, safe code-as-data, untrusted template source versus rendered data, deserialization without gadgets, upload with no execute path, and a remotely triggered worker with missing reachability. Use inert code excerpts; do not include runnable exploit payloads.

- [x] **Step 3: Record baseline and with-skill outputs**

Use separate fresh-context evaluators when available and provide only the relevant skill package to the with-skill evaluator. Preserve outputs and exact citations; if the baseline already handles a scenario, report that rather than claiming improvement. No target application, scanner, or runtime is involved.

### Task 7: Integrate, verify, and commit the deliverable

**Files:**
- Modify: `README.md`
- Modify: `PROVENANCE.md`
- Modify: `AGENTS.md`
- Create: all ADR, corpus, skill, and maintenance files above.

**Interfaces:**
- Consumes: all verified deliverables from Tasks 1–6.
- Produces: catalogued, installable skill and a clean local commit.

- [x] **Step 1: Update repository catalog and provenance**

Add the skill installation command and catalog row to root README; document the new corpus's source/evidence conventions in `PROVENANCE.md`; ensure ADR-0010 is indexed in `AGENTS.md`.

- [x] **Step 2: Run final documentation and package checks**

Run `git diff --check`; check all repository Markdown relative links; confirm at least 40 distinct qualified cases and all package external sources summarized; run `npx skills add . --list`; install `rce-static-review` from a temporary local checkout and compare every installed file byte-for-byte with the package. Review the diff for unrelated files, unverified claims, sensitive data, or copied third-party text.

- [ ] **Step 3: Commit the scoped deliverable**

Stage only ADR-0010, corpus/security/RCE materials, the `rce-static-review` package, its maintenance materials, and the necessary README/provenance/index updates. Commit with `feat: add static RCE review skill and corpus`. Then fast-forward local `main` to the completed feature branch and push `origin main`, which the user explicitly requested; verify the remote ref equals the tested commit.

---

## Self-Review

- **Spec coverage:** The corpus quota and taxonomy are covered by Tasks 1–3; offline self-contained references by Task 4; source-only skill and report behavior by Task 5; regeneration/evaluation by Task 6; discovery, provenance, ADR indexing, and Git integration by Task 7.
- **Step clarity:** Each step produces an identifiable Markdown, research, validation, or integration result; no code API is introduced.
- **Review Focus:** All five failure modes map to negative/incomplete scenarios in Task 6, and Task 5 requires corresponding safe examples.
- **Proportion:** The deliverable is multi-part research and documentation; the task list follows its actual package boundaries without proposing new runtime tools or application changes.

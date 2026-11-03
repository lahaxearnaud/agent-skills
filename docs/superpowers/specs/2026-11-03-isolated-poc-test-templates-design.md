# Isolated PoC test templates

**Status:** Approved by the user on 2026-11-03.

## Intent

Add bundled, offline-ready test skeletons to `isolated-vulnerability-reproduction` so agents can start a small reproduction in a familiar shape and recognize its output consistently. The templates reduce setup variation without booting the reviewed application or restoring its dependency graph.

## Goals

- Provide four small starting points: static HTML observed in a browser, JavaScript under Node, JavaScript in a browser, and PHP CLI.
- Keep a shared stdout contract: one machine-readable `ISOLATED_POC_CASE=` JSON record for `control`, then one for `trigger`.
- Make the checked-in examples safe smoke scaffolds, not vulnerability demonstrations; they use synthetic marker values and clearly state that their output proves only that the harness ran.
- Keep browser checks local, network-disabled and inside the existing fixed Docker profile. Preserve Chromium's default sandbox; report a blocked run if it cannot start.
- Require agents to replace the sample function or fixture with the exact relevant code and synthetic inputs, and to record source origin, assumptions and interpretation.
- Package all templates and instructions inside the installable skill for offline use.

## Non-goals

- Do not add framework-specific scaffolds for Vue, Twig, Symfony, or other stacks yet. Add these only when a framework-specific runtime can be reproduced without reinstalling dependencies and materially changes the behavior under test.
- Do not add a template generator, dependency installer, active scanner, target application launcher, or runtime changes to the Docker runner.
- Do not treat the template smoke output, a browser parse, or a negative observation as a vulnerability verdict.

## Approaches

1. **One generic skeleton:** fewer files, but agents still have to adapt runtime assumptions and output collection for Node, browser DOM, HTML, and PHP.
2. **One skeleton per runtime/surface (selected):** four focused directories share a small case-output contract; browser scaffolds use the bundled Playwright image and a local HTML fixture. This follows the user's preference for repeatable, predictable runs while keeping each workspace small.
3. **One skeleton per vulnerability family or framework:** richer, but multiplies combinations and may require dependencies prohibited by the minimal-PoC rule. Defer until repeated cases demonstrate the need.

## Decision

Add `templates/` inside the skill. Include `html-browser`, `javascript-node`, `javascript-browser`, and `php-cli` examples. Each template documents its purpose, editable candidate/input slots, exact manifest image/argv fields, smoke output and limitations. The browser helper discovers Chromium within the official Playwright image, loads only local `file:` fixtures, prints the shared case records, and does not disable the browser sandbox. The static HTML template observes markup only; it does not execute PHP/Twig rendering or prove route reachability.

Every default sample prints exactly two `ISOLATED_POC_CASE=` JSON lines, one for each case. An agent must preserve the case order, change sample values to observations meaningful for its hypothesis, and explain which observation would count as reproduction. The PoC runner's own `status` and exit code remain separate from this hypothesis-level interpretation.

## Constraints and risks

- Use only images already in the allowlist, a concrete tag plus SHA-256 digest, and the fixed runner profile.
- Keep each workspace under the existing 50-file, 200-entry, 5-MiB limits; no package installation, network, host mounts, or reviewed project execution.
- A browser may be blocked by Chromium sandbox or runtime requirements under the fixed profile. The scaffold must report this as blocked; the agent must not add `--no-sandbox`, extra capabilities, or weaker container controls.
- A copied helper or fixture may omit integration behavior. Each result must identify those limits.

## Verification

Test that the four templates are complete and emit the shared records, then run the Node, PHP and browser smoke examples with digest-pinned allowlisted images through the bundled runner when those images are available. Verify the skill remains installable and all template files are included in a temporary local installation.

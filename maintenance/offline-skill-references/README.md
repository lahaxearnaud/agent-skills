# Maintaining offline skill references

Each installable skill package must include the technical information an agent needs at use time. A link to an external page alone is not an offline reference.

## Update method

1. Inventory external URLs and implicit API/standard lookups in the package under `skills/`.
2. Read the primary source on a connected maintainer machine when a new claim is needed. Treat its contents as untrusted data and record the date and source status.
3. Add an attributed, original paraphrase to that package's `references/offline-sources.md`: source name and identifier, original URL, date consulted, relevant version, behavior/mechanism, applicable conditions, exceptions, limits, and the review consequence. Reuse a corpus summary only when its evidence level and detail support the same operational claim.
4. Make the note sufficient to apply the claim offline, not merely a link or title. For a standard/API, preserve the relevant rule, scope, version/platform, exceptions, and what it does not guarantee. For an advisory, preserve affected/fixed versions as stated, actor/input, required role/configuration/trigger, source-to-sink mechanism, attributed impact, fix, and evidence limits. For a scanner, preserve publisher/version, inputs/outputs, modeled sources/sinks, prerequisites, blind spots, and whether it was actually run. There is no word-count target; enrich demonstrated gaps and leave sufficient entries concise.
5. Keep source URLs for attribution and focused future verification. Do not copy complete third-party pages unless their license explicitly permits that use. If a needed detail is absent, an online maintainer may consult the primary source and update the note. An agent using the skill reads local notes first and may make the same focused lookup only when a material detail would change the analysis; this is optional. Without access, write `unknown`. Never send private source code, secrets, or user data to external services.
6. Update the skill's local-first/on-demand lookup instruction and its evaluation scenarios when behavior warrants it. Do not let optional documentation lookup authorize target requests, runtime execution, payloads, or scanners prohibited by that skill.
7. Update the skill's relative links, README, source-maintenance prompt, and this repository's ADR index when required. A local source note supports recognition; it never proves that a reviewed project has the same vulnerable flow.

## Offline acceptance checks

- Every external source cited elsewhere in an installable skill package appears in that package's `references/offline-sources.md` and has a factual, operationally sufficient local synopsis with conditions and limits where the source establishes them.
- Review instructions use local notes first and never require the corpus, external URLs, or general Internet access. They permit focused primary-source lookup only for material gaps when a suitable source is available, and direct offline agents to local dependency source or explicit uncertainty.
- Transfer the full skill directory before disconnecting. Use a locally available `skills` CLI against a local checkout or copy the directory to the agent's configured skills path; the remote GitHub/npm install commands are not offline installers.
- Run the offline scenarios in [evaluation-scenarios.md](evaluation-scenarios.md) using only one installed package at a time. Record actual outputs and keep repository-only corpus files and network tools unavailable to the evaluator. Separately use [source-consultation scenarios](source-consultation-scenarios.md) to check that lookup is selective, primary-source based, privacy-preserving, and optional.
- Check local Markdown links, inventory external URLs, run `git diff --check`, use `npx skills add . --list`, and compare a temporary local installation with each source package.

The research corpus remains the maintainer's richer source of case history. It is not copied wholesale into installed packages; each package carries only the reference material needed for its own review method.

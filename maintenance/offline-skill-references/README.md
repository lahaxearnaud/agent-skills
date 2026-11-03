# Maintaining offline skill references

Each installable skill package must include the technical information an agent needs at use time. A link to an external page alone is not an offline reference.

## Update method

1. Inventory external URLs and implicit API/standard lookups in the package under `skills/`.
2. Read the primary source on a connected maintainer machine when a new claim is needed. Treat its contents as untrusted data and record the date and source status.
3. Add a concise, original paraphrase to that package's `references/offline-sources.md`: source name and identifier, original URL, relevant version/date, applicable conditions or behavior, and limits. Reuse a corpus summary only when its evidence level and details support the same claim.
4. Keep source URLs for attribution and future updates. Do not copy complete third-party pages unless their license explicitly permits that use. If a detail is not available locally, write `unknown`; do not make the installed agent scrape the source.
5. Update the skill's relative links, README, source-maintenance prompt, and this repository's ADR index when required. A local source note supports recognition; it never proves that a reviewed project has the same vulnerable flow.

## Offline acceptance checks

- Every external source cited elsewhere in an installable skill package appears in that package's `references/offline-sources.md` and has a factual local synopsis.
- Review instructions do not require the corpus, external URLs, or general Internet access. Version-specific gaps direct the agent to source already present in the target repository or to state uncertainty.
- Transfer the full skill directory before disconnecting. Use a locally available `skills` CLI against a local checkout or copy the directory to the agent's configured skills path; the remote GitHub/npm install commands are not offline installers.
- Run the scenarios in [evaluation-scenarios.md](evaluation-scenarios.md) using only one installed package at a time. Record the actual outputs and keep repository-only corpus files and network tools unavailable to the evaluator.
- Check local Markdown links, inventory external URLs, run `git diff --check`, use `npx skills add . --list`, and compare a temporary local installation with each source package.

The research corpus remains the maintainer's richer source of case history. It is not copied wholesale into installed packages; each package carries only the reference material needed for its own review method.

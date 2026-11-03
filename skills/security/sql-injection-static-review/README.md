# SQL injection static review

A portable coding-agent skill for reviewing SQL injection through source analysis. It covers PHP/Doctrine and other web stacks, direct and second-order flows, SQL structure versus values, ORM escape hatches, conditional impact and false-positive controls. It does not run an application, attack payloads or active scanners.

```bash
npx skills add lahaxearnaud/agent-skills --skill sql-injection-static-review --agent codex opencode --yes
```

The command installs the published repository version. In a local checkout use `npx skills add . --skill sql-injection-static-review`. The references included in this directory, including local summaries for each cited advisory and technical document, are sufficient offline; source URLs are retained for attribution and maintenance only. The repository corpus contains 61 published advisory summaries, 20 leads awaiting qualification, and 30 synthetic scenarios; see `corpus/security/sql-injection/` and the update process in `maintenance/security/sql-injection/`. Respond in the language requested by the user, independently of the English skill instructions.

For an offline machine, transfer this complete directory before disconnecting, then install from a local checkout with a preinstalled CLI or copy it into the agent's configured skills location. The GitHub installation command above requires network access.

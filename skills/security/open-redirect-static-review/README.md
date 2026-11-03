# Open redirect static review

This portable skill guides source-based review of server-side redirects and client-side automatic navigation. It emphasizes PHP/Symfony/Twig, JavaScript, Vue/Nuxt, login return paths, request headers, and OAuth. It does not run the target application, browser, payloads, scanner, or network requests.

Install from the repository with the [`skills`](https://github.com/vercel-labs/skills) CLI:

```bash
npx skills add lahaxearnaud/agent-skills --skill open-redirect-static-review --agent codex opencode --yes
```

Example request: “Use `open-redirect-static-review` to trace untrusted return destinations through the PHP controllers, Symfony routes, Twig templates, and Vue navigation code in this repository.”

`SKILL.md` and its relative references contain the guidance and local summaries needed for ordinary offline review. The larger research corpus is maintained separately at [`corpus/security/open-redirect/`](../../../corpus/security/open-redirect/README.md); the installed skill does not require it or Internet access. If online, an agent may consult a primary source when a missing material parser, version, or policy detail could change the conclusion. This is optional; private reviewed code must not be sent externally. Source URLs remain for attribution and maintenance. See the [corpus update prompt](../../../maintenance/security/open-redirect/update-prompt.md) to add evidence and improve the skill. Sources retain their own rights and attribution.

For an offline machine, transfer this complete directory before disconnecting, then install from a local checkout with a preinstalled CLI or copy the directory into the agent's configured skills location. The GitHub installation command above requires network access.

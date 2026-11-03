# Open redirect static review

This portable skill guides source-based review of server-side redirects and client-side automatic navigation. It emphasizes PHP/Symfony/Twig, JavaScript, Vue/Nuxt, login return paths, request headers, and OAuth. It does not run the target application, browser, payloads, scanner, or network requests.

Install from the repository with the [`skills`](https://github.com/vercel-labs/skills) CLI:

```bash
npx skills add lahaxearnaud/agent-skills --skill open-redirect-static-review --agent codex opencode --yes
```

Example request: “Use `open-redirect-static-review` to trace untrusted return destinations through the PHP controllers, Symfony routes, Twig templates, and Vue navigation code in this repository.”

`SKILL.md` and its relative references contain what an agent needs at review time. The larger research corpus is maintained separately at [`corpus/security/open-redirect/`](../../../corpus/security/open-redirect/README.md); the installed skill does not require it or Internet access during an audit. See the [corpus update prompt](../../../maintenance/security/open-redirect/update-prompt.md) to add evidence and improve the skill. Sources retain their own rights and attribution.

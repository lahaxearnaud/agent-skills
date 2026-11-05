# Static authorization review

A portable coding-agent skill for source-based review of broken access control, including function, object, tenant, and property-level authorization. It emphasizes Symfony server policies and distinguishes Vue UI checks from backend enforcement. It does not run an application, send requests, or use active scanners.

```bash
npx skills add lahaxearnaud/agent-skills --skill authorization-static-review --agent codex opencode --yes
```

For a local checkout, use `npx skills add . --skill authorization-static-review`. The skill includes the references needed for offline review. Respond in the language requested by the user, independently of the English skill instructions.

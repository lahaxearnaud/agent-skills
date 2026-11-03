# path-traversal-static-review

An installable, source-only code-review skill for server-side Web path traversal: file reads/writes/deletes, static and download handlers, PHP/Symfony/Twig template/resource loaders, Node.js/Java/Python/Go code, archive import/restore (Zip Slip), symlinks, and path normalization mismatches.

The skill does not execute the reviewed Web application or send requests to it. Its references, including local summaries of filesystem APIs and standards, are bundled and work after installation; it does not require the repository corpus or Internet access. Read local notes first. If online, consult an exact primary source only when a material version, platform, or filesystem detail is missing. This is optional; never send private code externally. External URLs remain for attribution and future updates.

Install from this repository with:

```bash
npx skills add lahaxearnaud/agent-skills --skill path-traversal-static-review --agent codex opencode --yes
```

The maintained case corpus and regeneration process live under `corpus/security/path-traversal/` and `maintenance/security/path-traversal/`.

For an offline machine, transfer this complete directory before disconnecting, then install from a local checkout with a preinstalled CLI or copy it into the agent's configured skills location. The GitHub installation command above requires network access.

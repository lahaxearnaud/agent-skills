# path-traversal-static-review

An installable, source-only code-review skill for server-side Web path traversal: file reads/writes/deletes, static and download handlers, PHP/Symfony/Twig template/resource loaders, Node.js/Java/Python/Go code, archive import/restore (Zip Slip), symlinks, and path normalization mismatches.

The skill does not execute the reviewed Web application or send requests. Its references are bundled and work after installation; it does not require the repository research corpus at review time.

Install from this repository with:

```bash
npx skills add lahaxearnaud/agent-skills --skill path-traversal-static-review --agent codex opencode --yes
```

The maintained case corpus and regeneration process live under `corpus/security/path-traversal/` and `maintenance/security/path-traversal/`.

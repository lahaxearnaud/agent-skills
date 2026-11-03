# Research-backed skill builder

A skill for creating or improving a coding-agent skill from documentation, real-world cases, tools, and a traceable corpus, for security and other technical domains.

Once this skill is published on the branch read by GitHub, use it from a repository or project where the `skills` CLI is available:

```bash
npx skills add lahaxearnaud/agent-skills --skill research-backed-skill-builder
```

Example request: “Use research-backed-skill-builder to create a static SQL review skill with a sourced corpus, then create a local commit.” Specify the subject, technologies, research and runtime constraints, destination, and any authorized publication.

By default the builder writes generated skill instructions, operational references, and skill READMEs in English; an explicit user preference overrides this. It responds to users in their requested language, or otherwise the language of their request.

The [SKILL.md](SKILL.md) and its references are self-contained after installation. The method does not assume that a corpus or Internet access will be available when the generated skill is used; it reports research and evaluation limitations. Remote publication requires applicable authorization.

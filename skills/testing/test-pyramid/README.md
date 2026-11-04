# Test Pyramid Skill

An installable, self-contained skill for choosing test layers and writing application tests with the test pyramid.

Install from the repository:

```sh
npx skills add lahaxearnaud/agent-skills --skill test-pyramid --agent codex opencode --yes
```

The package contains the skill instructions and offline source summaries. It has no separate case corpus, runtime tool, or additional package dependency. It asks an agent to follow the test framework and commands already present in the application repository.

See [the skill](SKILL.md), [layer guide](references/layer-selection.md), [offline sources](references/offline-sources.md), and the repository's [evaluation notes](../../../maintenance/testing/evaluation.md).

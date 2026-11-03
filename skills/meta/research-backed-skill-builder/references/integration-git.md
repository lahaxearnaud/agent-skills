# Repository integration and maintenance

## Portable placement

Inspect repository instructions and layout. In a catalog using the `skills` CLI, a location such as `skills/<domain>/<name>/SKILL.md` groups topics; confirm discovery with the version actually available. Do not create a parent `SKILL.md` that hides nested skills. Each installable skill contains the references it needs and does not depend on the repository corpus after installation.

Add the skill to the existing catalog, provide a suitable installation command, and explain where the corpus and maintenance instructions reside. Check existing paths, names, conflicts, and local changes; do not overwrite other work or regenerate files without cause.

## Git and publication

- Before starting, inspect `git status`, branch, and applicable instructions; choose a branch or isolated workspace if needed. Preserve pre-existing changes, including untracked files.
- Prepare only assignment files, inspect their diff and provenance, and check for sensitive data and third-party rights. Do not use a blanket add that would include unrelated changes.
- When the assignment requests a repository deliverable, create a targeted local commit after verification. A local commit is the default unless an instruction or higher-priority rule says otherwise. If no repository or Git identity is available, explain the blocker and preserve deliverables.
- Do not push, publish, create a remote repository, open a PR, or send messages to third parties without applicable authorization; if the request explicitly authorizes an action, follow repository rules and verify its result. Never treat elapsed time as approval.

## Maintenance

Provide a regeneration prompt or method: reread the skill and corpus, qualify new sources, preserve prior evidence, update useful references, verify installation, and reevaluate scenarios. Explain that a corpus can evolve and cited cases do not prove the quality of a future analysis. Do not overwrite an existing skill and its corpus by default. Generated skill instructions and references use English by default unless the user explicitly requests another language; preserve the user's desired response language separately.

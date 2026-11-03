# Maintaining the RCE corpus and skill

The qualified corpus, installable skill and local source notes have different jobs:

- `corpus/security/remote-code-execution/` contains dated case research, source status, exclusions and reusable pattern notes. The acceptance minimum is 40 distinct source-checked public cases; the current snapshot records 55.
- `skills/security/rce-static-review/` is the offline installable workflow. Keep its operational guidance concise and self-contained, with external technical sources paraphrased in `references/offline-sources.md`.
- This directory stores the update prompt and static evaluation scenarios/results.

To update, use [the research prompt](update-prompt.md), qualify primary sources and reconcile aliases before updating the count, refresh local notes where the skill depends on a new external source, then run the corpus/package checks. Keep leads, labs, synthetic examples and duplicate notices separate from the 40-case minimum.

No target application, payload, active scanner or runtime is required for maintenance or skill evaluation.

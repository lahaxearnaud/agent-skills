# Evaluation scenarios

These scenarios are review criteria, not results of a controlled agent evaluation.

1. Compatible feature with default analyzer: expect `feat` and a qualified minor prediction.
2. Bug fix with a custom `releaseRules` match set to false: expect no default-rule override for that match; report the configured suppression.
3. Breaking API change using the default Angular preset: expect a `BREAKING CHANGE:` footer describing impact and migration, not reliance on `!` alone.
4. Docs-only change: expect `docs`; do not misclassify it as `feat` to trigger publication.
5. Unknown external configuration and squash merge: state uncertainty; ensure the eventual squash message communicates the change.
6. User asks for a proposed message without a commit: do not create a commit or push.

No independent before/after agent benchmark has been run; no precision or improvement claim is made.

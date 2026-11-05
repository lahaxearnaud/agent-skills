# Offline source notes

Consulted 2026-11-05. These summaries support offline use; links are attribution and optional verification pointers.

## Conventional Commits 1.0.0

[Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/) defines a type, optional scope, optional breaking marker, colon and description, followed by optional body and footers. `feat` denotes a feature and `fix` a bug fix. A breaking change can be expressed by `!` before the colon or a `BREAKING CHANGE:` footer. Other types are allowed and are not inherently associated with a version bump by the specification. The specification's syntax does not prove a particular release tool uses a compatible parser.

## semantic-release commit analyzer

[@semantic-release/commit-analyzer documentation](https://github.com/semantic-release/commit-analyzer) documents Angular as its default preset, customizable `preset`, `parserOpts`, and `releaseRules`, and selection of the highest matching release type. Its [default rules](https://github.com/semantic-release/commit-analyzer/blob/master/lib/default-release-rules.js) map parsed breaking changes to major, `feat` to minor, `fix` and `perf` to patch, and recognized reverts to patch. Types such as `docs` have no default release mapping. Unmatched custom rules fall back to defaults; a matching custom rule may suppress a release. Rule behavior depends on parsed commit properties and installed version.

The analyzer documentation says Angular-style breaking notes require `BREAKING CHANGE:` in the footer. Conventional Commits `!` support depends on the chosen parser/preset; include the footer and inspect the actual configuration. Other semantic-release plugins and branches influence whether a release is published. When configuration is unavailable, state the uncertainty instead of inventing a release prediction.

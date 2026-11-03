# Installation and use

This portable skill follows the Agent Skills format: `SKILL.md` and relative references. Copy the directory into the skills location recognized by your Codex or OpenCode installation; discovery locations depend on the tool's configuration and version. This directory is a repository deliverable and is not automatically installed or globally enabled.

Example request: “Use the xss-static-review skill to statically audit the routes, Twig templates, and Vue components in this repository.” The agent reads `SKILL.md`, then the relevant references. The skill does not run the application or dynamic tests; its code searches remain local and read-only. It responds in the user's requested language, or otherwise in the language of their request.

The references are included in this directory so they work after copying. They summarize this repository's corpus under `corpus/security/xss/` and link to public advisories and documentation; they do not require access to that corpus or to the Internet during an audit. Security versions and links can change.

For a project-local installation, copy the entire directory to `.agents/skills/xss-static-review/` in the target project if supported by the tool version. OpenCode also documents `.opencode/skills/xss-static-review/`: [official documentation](https://opencode.ai/docs/skills). Verify discovery in the tool after copying; no global location is changed by these instructions.

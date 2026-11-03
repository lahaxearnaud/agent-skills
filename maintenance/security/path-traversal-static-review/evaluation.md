# Path traversal static-review skill evaluation

Evaluation date: 2026-11-03. This is a qualitative comparison on two synthetic static-code scenarios, not a benchmark or a measurement of precision, recall, or vulnerability-detection performance. The cases are in [evaluation scenarios](evaluation-scenarios.md). No Web application, browser, scanner, payload, or target network request was run.

## Baseline without the skill

Fresh-context agents received the scenarios without the new skill.

### Scenario A — Prefix-based static download check

The agent identified that the string-prefix check did not prove containment and described the sibling-prefix condition. It limited disclosure to an existing readable target and correctly rejected the ticket's RCE claim. It also noted route reachability, process permissions, deployment layout, and symlink follow-through. The baseline handled this simple positive case correctly; this does not demonstrate a failure to be fixed or establish a skill performance gain.

Baseline result, verbatim:

> **Finding: path traversal can escape the download directory.** The check uses a string prefix, so a resolved path under a sibling whose name begins with `/srv/app/public/downloads` can pass even though it is outside `DOWNLOAD_ROOT`. This means the validation does not prove confinement.
>
> **Preconditions and impact:** The route must be reachable with attacker-controlled `name`, and a matching-prefix target file must exist and be readable by the process. The likely impact is disclosure of that file; the excerpt does not support a claim of RCE or access to every system file. Confirm whether other middleware restricts the name, and inspect deployment directory layout, symlinks, and process permissions. `readFile` follows symlinks, so a symlink inside the root could also point outside it.
>
> **Severity:** Cannot be set from this excerpt alone; it depends on reachable targets and their sensitivity.
>
> **Remediation:** Resolve the path, then use `path.relative` to reject paths that escape the root. If symlinks may be present or attacker-controlled, check canonical paths as well, with a race-safe file access strategy where needed.

### Scenario B — Fixed lookup and archive extraction

The agent correctly rejected a traversal finding for the fixed key-to-file map. For the archive function, it identified a `realpath()` failure fallback, a symlink at the final candidate, the prefix check, and check-to-write races. It conditioned exploitability on destination state, permissions, platform, and process privileges. This baseline also handled the designed edge case correctly.

Baseline result, verbatim:

> **Snippet A — no path traversal shown.** The request controls only `$key`, which must exactly match one of two fixed array keys. The selected `readfile()` path comes from the fixed map; the request value is never joined to a filesystem path. This does not establish that the mapped files are safe from filesystem changes: whether either target or a parent directory is a symlink is unknown. Keep the map targets under trusted control and protect them from untrusted modification; filename validation adds no traversal protection here.
>
> **Snippet B — unsafe extraction path handling; outside-root writes are possible under specific filesystem conditions.** The archive entry name reaches the `copy()` source as an entry in the `zip://` stream, while the destination is built from `basename($name)`. That strips ordinary path components for the destination, but does not establish filesystem containment. The code also fails to check whether `realpath($destination)` succeeded. If it returns `false`, `$root` becomes an empty string in path concatenation, and the candidate becomes a rooted filename; the fallback in the check can then make `str_starts_with(..., $root)` pass. Even with a valid root, the check resolves only `dirname($candidate)`, so an existing symlink at the candidate filename can point outside the root and be followed when `copy()` opens the destination. A check followed by a write can also race if an attacker can alter the destination directory. The string-prefix check itself lacks a path-component boundary, though ordinary `basename()` output makes that less central here.
>
> Static evidence does not prove an exploitable write in a particular deployment. Missing facts include whether the destination exists, its permissions and contents, whether an outside-pointing symlink can be present or changed, the PHP/platform path semantics, and the process’s write privileges. Reject a failed `realpath()` and require a real destination directory. Extract into a fresh, private directory and create each output file exclusively so an existing symlink cannot be followed; validate entry names for the intended flat-file policy as additional input validation. For any design that permits nested paths, verify canonical filesystem containment with path-component boundaries and protect the check-to-write operation from races.

## Evaluation with the skill

Fresh-context agents read `skills/security/path-traversal-static-review/SKILL.md` and relevant bundled references, then reviewed the exact same excerpts.

### Scenario A — Prefix-based static download check

The agent reported a source-supported path escape and traced request input through `path.resolve`, a raw prefix check, and `fs.readFile`. It stated conditional disclosure, left severity unassigned, and rejected RCE or unrestricted file access. The baseline already identified the same weakness and limits; the skill confirmed the finding and produced a more explicit evidence chain. This is not evidence of measured improvement.

With-skill result, verbatim:

> **Source-supported path escape:** `GET /download` converts request-controlled `req.query.name` to a string, resolves it against `/srv/app/public/downloads`, checks only `resolved.startsWith(DOWNLOAD_ROOT)`, then passes `resolved` to `fs.readFile`. A path resolving to an adjacent sibling whose name shares the root’s character prefix can pass this guard while remaining outside the downloads directory.
>
> The impact is conditional file disclosure: the route must be reachable, the request must select a matching-prefix target that exists, and the process must be able to read it. `path.resolve` performs lexical path resolution; the excerpt does not show symlink checks, so a link under the root could also affect the target. Authentication, deployment exposure, filesystem layout, permissions, and link control are unknown. This supports a path escape in the shown source, but not RCE, access to every host file, or an observed exploit. Severity is unassigned because no repository rubric or deployment evidence is provided.
>
> Remediation: compare path components with a path-aware containment check at the file-access boundary, and review symlink handling and check-to-open races. **Validation:** source review only; no runtime, browser, payload, scanner, or network activity. **Skill effect:** the skill confirmed the suspected prefix-check weakness and sharpened the distinction between the visible source finding and conditional deployment impact.

### Scenario B — Fixed lookup and archive extraction

The agent kept the server-owned map at “no traversal shown,” while reporting the ZIP flow as a candidate for an outside-root write. It traced `basename`, `realpath(dirname(...))`, the prefix check, and `copy`; it distinguished canonicalization failure, final-target symlinks, prefix boundaries, and TOCTOU. It left reachability, strict typing, platform, target, and permissions as unknowns. The baseline already reached the same overall conclusion; the skill reinforced the separation of lexical checks and filesystem conditions.

With-skill result, verbatim:

> **Snippet 1 — fixed lookup:** **No traversal shown.** The request controls `$key`, but `array_key_exists` restricts it to `manual` or `terms`; only the corresponding server-defined path reaches `readfile`. An unknown key exits with 404. The map’s paths or their filesystem targets could raise separate issues if they were attacker-controlled or linked elsewhere, but the snippet provides no such evidence. Keep the mapping server-owned; no traversal remediation is indicated here.
>
> **Snippet 2 — backup extraction:** **Candidate for an out-of-root write; reachability and filesystem conditions are unknown.** The archive supplies `$name`; `basename($name)` is joined to the canonical `$root`, then the code checks `realpath(dirname($candidate))` with `str_starts_with` before `copy()` writes the archive member to `$candidate`.
>
> Several conditions could defeat that check:
>
> - If `realpath($destination)` fails, `$root` is `false`. In a weak-typing PHP context, concatenation can produce a candidate rooted at the platform filesystem root, and the empty-string prefix check can accept it. Whether the call proceeds and the write succeeds depends on PHP typing behavior, OS path rules, and process permissions.
> - With a valid root, the check examines the parent, not the final target. A pre-existing symlink at `$candidate` can therefore point outside the root if `copy()` follows it and the process can write to its target. Replacing a path component between the check and write can create a similar race.
> - `str_starts_with` does not enforce a path-component boundary. For example, if the checked directory resolves to a similarly prefixed sibling after a path change, its string can still start with `$root`. The shown `basename` usually limits ordinary names to one component, so this specific case depends on filesystem changes and path semantics; the snippet does not establish that those conditions exist.
> - `basename()` limits path components on the platform, but does not prove final filesystem confinement. Special names such as `.` or `..`, and platform-specific behavior, also require review.
>
> The snippet does not show who can call this function, who controls the ZIP, whether the destination exists, or the OS, PHP version, strict typing context, filesystem permissions, and ability to create or change symlinks. It therefore does not prove a successful outside-root write in every deployment. Execution is not supported by the evidence.
>
> Fail closed when `realpath($destination)` fails; use a private extraction directory and safely create files without following attacker-controlled links. Validate final targets by path components at the write boundary, and account for concurrent filesystem changes. Treat archive names as untrusted even when reduced with `basename()`.
>
> The skill confirmed and sharpened the analysis: it reinforced tracing the archive member through the exact write sink and separating lexical checks, canonicalization failure, symlinks, and races. This was a source-only review; no code or application was run.

## Limits

Two synthetic scenarios and a small number of model responses do not test other languages, frameworks, archive APIs, path namespaces, or repository layouts. No statistical performance claim is made. Both baseline agents already handled the selected cases; with-skill results show consistency and a more explicit status/evidence structure, not a demonstrated detection-rate or false-positive improvement. The skill packages a repeatable method grounded in the larger research corpus.

# Command and process execution

## What to trace

Find direct process and shell APIs, framework process helpers, wrappers and commands invoked by dependencies. Trace remote input through concatenation, formatting, option construction, executable selection, current-directory selection, environment, scripts, configuration and stored/queued values to process creation.

Determine the actual process semantics:

1. Is a system shell invoked? Identify the option, helper or string API that selects it.
2. If no shell is used, can input alter the executable, argument boundary, option, response file, input script, plugin name, URL, config or secondary command understood by the called program?
3. Does a wrapper script reinterpret the arguments as shell, Python, PowerShell, SQL, a template or another language?
4. Which platform and library version are used, and what do their exact APIs do?

An argument vector usually avoids shell metacharacter parsing, but does not stop option injection or unsafe semantics in the child program. A user-controlled executable path is a distinct direct execution risk. A fixed executable with a remote filename argument may still be unsafe if the program accepts special options or loads code from that file. See [OS-01–OS-07](offline-sources.md#os-01) and [process patterns](case-patterns.md#process-execution).

## Candidate threshold

At least one value with a plausible remote or network-controlled origin reaches process construction. Then establish whether it changes executable behavior. If the source is a trusted constant, a validated enum mapped to fixed values, or a data argument whose target semantics are safe, do not label shell injection. If only a dangerous process API is visible, report an incomplete candidate until the source and interpretation are known.

## Controls to verify

- Prefer a non-process library where practical.
- Use a fixed executable and fixed option structure; pass distinct arguments without shell mode.
- Validate values against the invoked program's accepted domain, including whether leading option markers or special file/URL schemes carry meaning.
- Use a trusted working directory and controlled environment; consider inherited variables that change runtime/module loading.
- Avoid string shell helpers. If a shell feature is essential, verify context-specific escaping for the exact shell/platform and separately validate the target program's argument semantics.
- Run with least privilege and avoid secrets in command-line arguments. These controls reduce consequences but do not prove the flow safe.

## Common false positives and incomplete reports

- `ProcessBuilder`/`Symfony Process`/`subprocess.run([...])` with no shell does not alone establish shell injection.
- `execFile` differs from shell-based APIs only if the actual option configuration leaves shell mode disabled and the executable semantics are safe.
- A library may spawn internally, so inspect its documented API/version and wrapper path.
- A command used only in a local developer tool is not a remote RCE path without application-controlled reachability.
- A sanitized argument can still select a dangerous option. Conversely, a raw argument that the child treats strictly as data is not automatically command execution.
- An error or return-code difference alone is not proof of arbitrary execution.

Use the [report standard](report-standard.md) to name the exact parser boundary, not just the API call.

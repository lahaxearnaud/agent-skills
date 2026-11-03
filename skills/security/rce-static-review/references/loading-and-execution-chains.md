# Dynamic loading, writable artifacts, and deferred execution

## Trace the entire chain

Search for dynamic include/require/import/load, plugin registries, class loaders, script compilation, model or archive loading, task schedulers, workflow definitions, and configuration that is evaluated at startup. For file writes and uploads, trace the output path to every later consumer. A write primitive is not RCE unless a loader, interpreter, worker or privileged operation later executes or evaluates the artifact.

Model a cross-component flow explicitly:

1. remote actor or source;
2. validation and transformations;
3. storage, path or job identifier;
4. later consumer/loader and trigger;
5. execution-capable operation;
6. identity and privileges of the executing service.

Asynchronous paths need an explicit queue producer and consumer relationship. A worker that processes remote data is in scope only when application code connects the external source to its queue/job or configuration. Keep standalone build/CI concerns separate unless the Web application can remotely control or trigger that environment.

## Candidate threshold

The remote value controls code/module selection, executable file content or an artifact that a later loader will consume. If the report claims arbitrary write, determine whether the affected paths can actually be loaded, whether the application has write access, and whether execution requires a restart, deployment, operator action or separate vulnerability. Mark a conditional chain as conditional.

## Controls

- Resolve user selections through a fixed identifier-to-module registry.
- Keep uploads and generated files outside executable, template, plugin and configuration search paths.
- Use immutable trusted code paths, strict path/extension/type checks, no symlink traversal and least-privilege write permissions.
- Separate upload, render, worker and process identities; require explicit approval for code-bearing artifacts.
- Protect queues and administrative triggers; validate jobs again at the consumer because producer-side checks may not cover alternate producers.
- Record later triggers and delay assumptions in the finding.

## Common false positives

- A file write to isolated data storage with no later code-capable consumer is not RCE.
- A fixed import selected from application code is not an attacker-controlled module load.
- A worker's existence does not establish reachability from a public request.
- A local build script triggered only by a developer is not a remote service path. CI findings belong in scope only when an application remotely configures or triggers that CI execution.

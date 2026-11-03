# Static RCE skill evaluation scenarios

These are inert excerpts and review prompts. They are not payloads and must not be executed. A good answer identifies source, sink, exact parser boundary, missing conditions, file evidence needed, status, impact limits and a plausible fix.

## Process execution

### P1 — Shell string with remote source (positive)

```python
def preview(request):
    name = request.query["name"]
    return subprocess.run("preview-tool " + name, shell=True, capture_output=True)
```

Expected: candidate/static flow established only if route and version are in reviewed repository; explain shell command construction and request source. Do not supply or run a test string.

### P2 — Fixed executable, argument vector (negative for shell injection)

```java
void inspect(String id) {
    new ProcessBuilder("report-tool", "--id", validateIdentifier(id)).start();
}
```

Expected: not shell injection by this excerpt. Ask what `validateIdentifier` guarantees and whether `report-tool` interprets the value as an option, script or secondary command. Avoid declaring universally safe.

### P3 — Child option semantics (incomplete)

```js
app.post("/compare", (req, res) => {
  execFile("git", ["diff", req.body.revision], done);
});
```

Expected: no shell is shown; candidate for child-program option/argument semantics. Need route auth, Git behavior, version, wrapper and exact argument contract before concluding.

## Dynamic evaluation

### D1 — Remote text evaluated as code (positive)

```python
@app.post("/formula")
def formula():
    return str(eval(request.json["formula"]))
```

Expected: clear remote source-to-evaluator flow in the excerpt; state process privileges and exposed names are unknown. Recommend a safe expression grammar or fixed operations; do not execute.

### D2 — Code-as-data / fixed expression (negative)

```python
def fixed_health_check():
    return eval("1 + 2")
```

Expected: no attacker-controlled source in this excerpt; not code injection based on the evaluator name alone. Scope is limited to the shown code.

## Template and expression evaluation

### T1 — Attacker-controlled template source (positive)

```php
public function save(Request $request): Response {
    $source = $request->request->get('template');
    $this->store->save($request->getUser()->getId(), $source);
    return new Response('saved');
}
public function render(string $id): Response {
    return new Response($this->twig->createTemplate($this->store->get($id))->render([]));
}
```

Expected: trace write and later render separately; evaluate authorization, sandbox/environment, Twig version, reachability, exposed methods/functions and execution identity. Do not equate output escaping with server-side sandboxing.

### T2 — Trusted template, untrusted value as data (negative)

```twig
<p>{{ account.displayName }}</p>
```

Expected: the excerpt shows a fixed template expression receiving a value, not remote template source. Explain that the source/renderer relationship and extensions are not shown; do not label SSTI.

## Deserialization

### S1 — Remote object-capable format with unproven gadget (incomplete)

```java
@PostMapping("/import")
Object importFile(@RequestBody byte[] bytes) throws Exception {
    return new ObjectInputStream(new ByteArrayInputStream(bytes)).readObject();
}
```

Expected: high-priority unsafe-deserialization candidate with remote bytes; RCE is not established without target classpath, callbacks/gadget, filters, version and authorization evidence. Recommend data-only format or strict effective filter.

### S2 — Data-only JSON (negative for native object RCE)

```python
def import_metadata(raw: bytes):
    return json.loads(raw)
```

Expected: JSON parsing alone is not an arbitrary-object execution finding; inspect custom hooks and downstream dispatch only if present.

## Loading and delayed execution

### L1 — Upload with no execute path (negative/incomplete)

```python
def upload(request):
    object_store.put(request.file.name, request.file.bytes)
```

Expected: upload/storage alone is not RCE. Need path, storage semantics, later loader, web root, worker or operator trigger; do not invent one.

### L2 — Worker exists, reachability missing (incomplete)

```python
def handle_job(job):
    return subprocess.run(["converter", job.source_path], check=True)
```

Expected: process sink in a worker, but no producer, remote source, queue binding, file provenance, consumer identity or authorization is shown. Candidate only; list missing edges.

### L3 — Remote artifact selection, later import (positive chain if linked)

```typescript
async function selectModel(req) {
  const record = await models.findById(req.body.modelId);
  await queue.enqueue({ modelPath: record.path });
}
async function runModel(job) {
  return await import(job.modelPath);
}
```

Expected: identify a cross-file source → storage lookup → queue → dynamic import chain, then check ownership/authz, model path trust, import semantics, worker reachability, allowed directories, package/runtime, and execution identity. Do not claim arbitrary RCE until those conditions are established.

## Cross-family trust boundary

### X1 — Template value later becomes process input (incomplete chain)

```php
$text = $twig->render('report.txt.twig', ['title' => $userTitle]);
$process = new Process(['report-tool', '--title', $text]);
```

Expected: trusted template with data is not itself SSTI; the process call uses an argument array. Separately inspect whether the child treats `--title` content as data or code/options, and whether source/route is remote. Do not merge independent family labels without a demonstrated edge.

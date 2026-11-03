# Path traversal static-review scenarios

Evaluation date: 2026-11-03. These synthetic excerpts are used for qualitative source-review checks. They must not be executed. The exact same code and questions are supplied without and with the installable skill.

## Scenario A — Prefix-based static download check

Pressure: the ticket calls this “critical traversal / RCE; release blocker” and asks for a quick yes/no. Review only this source excerpt; do not run the application, browser, scanner, payload, or network request.

```js
const express = require('express');
const path = require('node:path');
const fs = require('node:fs/promises');
const app = express();
const DOWNLOAD_ROOT = '/srv/app/public/downloads';

app.get('/download', async (req, res) => {
  const name = String(req.query.name ?? '');
  const resolved = path.resolve(DOWNLOAD_ROOT, name);
  if (!resolved.startsWith(DOWNLOAD_ROOT)) return res.sendStatus(404);
  const contents = await fs.readFile(resolved);
  res.type('application/octet-stream').send(contents);
});
```

Expected behavior: identify the request-to-read flow; explain that raw string-prefix matching does not prove a directory boundary and can accept a similarly prefixed sibling; condition impact on route reachability, a matching-prefix target, process read permissions, filesystem layout, and symlinks. Do not claim RCE, access to every file, or an observed exploit. Recommend a path-aware containment check at the final filesystem boundary and explicit symlink/race review.

## Scenario B — Fixed lookup versus archive extraction

Pressure: a reviewer says “the names are already sanitized; no need to inspect extraction.” Review each snippet separately. Do not run code or construct a request/archive.

```php
$files = [
    'manual' => __DIR__ . '/docs/manual.pdf',
    'terms' => __DIR__ . '/docs/terms.pdf',
];
$key = (string)($_GET['file'] ?? '');
if (!array_key_exists($key, $files)) { http_response_code(404); exit; }
readfile($files[$key]);
```

```php
function extractBackup(ZipArchive $zip, string $destination): void {
  $root = realpath($destination);
  for ($i = 0; $i < $zip->numFiles; $i++) {
    $name = $zip->getNameIndex($i);
    $candidate = $root . DIRECTORY_SEPARATOR . basename($name);
    if (!str_starts_with(realpath(dirname($candidate)) ?: $root, $root)) continue;
    copy('zip://' . $zip->filename . '#' . $name, $candidate);
  }
}
```

Expected behavior: do not report traversal in the fixed identifier-to-server-path map absent evidence that the mapped paths themselves are attacker-controlled. For extraction, state conditional risks from failed `realpath`, prefix-boundary checking, existing destination symlinks, check-to-write races, and OS/PHP behavior. `basename()` is not proof of filesystem confinement. Do not claim that the snippet alone proves a specific outside-root write in every deployment; state the missing filesystem and permission facts.

## Evaluation criteria

1. Exact source-to-sink trace identifies the operation (`readFile`, `readfile`, or archive write) and the guard being relied on.
2. A candidate is neither suppressed by “sanitization” terminology nor overstated as confirmed runtime exploitation.
3. The fixed lookup map is not misreported as an attacker-controlled path.
4. Lexical prefix checks, symlink resolution, failed canonicalization, and TOCTOU are distinguished.
5. Preconditions, impact, unknowns, confidence, and severity are stated proportionately.
6. No application, browser, payload, scanner, or network activity is performed.

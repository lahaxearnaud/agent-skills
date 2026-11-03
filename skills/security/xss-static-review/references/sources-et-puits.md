# Sources, transformations, and sinks for XSS review

These lists guide discovery. For each occurrence, determine the data type, who controls it, the path, and the context: no keyword alone is sufficient.

## Sources to inventory

- HTTP: query, path, body, forms, JSON, cookies, headers, duplicate parameters, and redirect URLs; data from SAML/OIDC authentication and associated exception messages.
- Persisted data: profiles, comments, product names, editable translations and settings, CMS content, titles, files, search results, tickets, and posts. Distinguish write control from readers.
- External providers: APIs, webhooks, WebSocket messages, imports, files, filenames, database metadata, certificates, logs, DNS, and metrics. An internal API or database does not automatically confer trust.
- Browser: `location.search`, `location.hash`, `location.href`, `document.referrer`, `document.cookie`, `localStorage`, IndexedDB, `fetch`/XHR responses, `postMessage`, `data-*` attributes, and DOM state. For messages, examine `event.origin`, `event.source`, and message structure checks.
- Vue: props and slots, router query/params/hash, API data, stores, computed values/watchers, translations, bindings, object keys, SSR state, and hydration. A prop is not automatically attacker-controlled: trace its parents and sources.
- Twig/PHP: `render` parameters, entities and getters, macros, includes, inheritance, globals, translations, functions/filters, and `Twig\Markup`. Trace values across files.

## Propagation and grammar changes

Trace assignments, interpolation, callbacks, calls, arrays/objects and their **keys**, closures, events, promises, APIs, databases, storage, serialization, and field names. Explicitly mark unknown steps.

Look for `decodeURIComponent`, `html_entity_decode`, `htmlspecialchars_decode`, HTML/DOM parsing and serialization, Markdown, XML, SVG, URL, JSON, charset handling, and Unicode normalization. Decoding does not automatically imply a vulnerability: determine the input, order, and final sink. Reading an HTML attribute through `dataset` may return decoded characters after initial encoding.

Never treat `JSON.parse`, `json_encode`, format validation, database storage, or an API response as universal HTML sanitization. Transformations after sanitization can change or invalidate its guarantee.

## Sinks by context

| Context | Candidates |
|---|---|
| Server HTML | Twig `raw`, `autoescape false`, `Markup`, functions/filters marked `is_safe`, concatenation in a PHP response, error or debug views, HTML generation in libraries. |
| DOM HTML | `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, jQuery `.html`/`.append` with HTML, `Range.createContextualFragment`, HTML parsers followed by insertion; `v-html`, `h(...,{innerHTML})`, JSX `innerHTML`, and other raw HTML mechanisms. |
| URL/navigation | `href`, `src`, `action`, `formaction`, redirects and return parameters, JS navigation, script or iframe URLs. Check scheme and destination; an escaped attribute does not validate its protocol. |
| JS code | Data in a `<script>` element, inline handler, `eval`, `Function`, string-based timers, script creation, and client template compilation. Account for the enclosing HTML parser. |
| Active document | Upload, preview, or conversion of HTML/SVG/XML, `iframe.srcdoc`, webhook response, and files served inline. Examine media type, origin, sandbox, and direct navigation. |
| CSS and UI | Style values or free HTML that can alter the interface; qualify UI deception separately and do not claim XSS without an execution chain. |

`textContent` on an ordinary display element creates text, not HTML. On a `script` element, the value can be code: verify the element type and lifecycle. Fixed non-executable attributes, constant values, and structured DOM construction can be safe; do not confuse a symbol with evidence.

## Directed search

Start with source, template, and configuration directories actually present. Search indirect calls and libraries that generate HTML; adjust `vendor`, `node_modules`, and bundle exclusions when a dependency or artifact matters. Use existing SAST tools only if they can analyze local files statically; document limits in language, file, and interprocedural coverage. Do not install or run a tool that executes the application.

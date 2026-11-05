# Reporting and scenarios

Report actor and privileges; upload entry and controlled bytes/metadata; validation and transformations; destination and filename; processing or delivery sink; server/browser configuration; supported effect and unknowns. Separate direct code facts from assumptions and avoid claiming exploitation.

- A Symfony controller moves a client-named upload into a public directory, but web server handlers are unavailable: trace validation and path; classify execution as conditional, not established.
- A Vue component only accepts images but the server accepts arbitrary uploads: inspect the server path and resulting use; UI validation is not a server guard.
- A server inspects MIME but retains an unchecked client extension: compare accepted bytes, saved name and execution handler. An extension mismatch is a meaningful lead, not proof of RCE.
- SVG is accepted and served inline on the application origin: establish content sanitization, access and response headers before reporting stored XSS.
- File bytes are stored privately with generated keys, download requires authorization and the server does not execute or render them: do not infer execution from arbitrary bytes; inspect actual processing and other paths.
- A rejected type is still saved in a draft or extracted from an archive: follow storage and subsequent consumers rather than treating the rejection message as a full barrier.

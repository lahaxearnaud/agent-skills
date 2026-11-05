# Sources, transformations and sinks

Sources include multipart body, filename and content-type headers, base64 fields, chunks, upload session metadata, archive entries and persisted filenames. Client filename, extension, `Content-Type`, browser checks and `accept` attributes are attacker-controlled unless independently established otherwise. Follow bytes separately from declared metadata.

In PHP/Symfony find `UploadedFile`, request file bags, validators, `move()`, filesystem/storage adapters, original names, extension guessing, temporary paths and upload handlers. Inspect custom validators and framework version rather than trusting a method name. Search JavaScript server paths for multipart middleware, `multer`, busboy, form parsers, object storage SDKs and filesystem writes; distinguish Node server handlers from Vue UI components. Search generic copy/write, archive extraction, image conversion, document processing and imports. A scanner hit or dangerous extension is only a candidate.

Trace final object keys and filesystem paths, overwrites and public serving. Compare normalized and case-folded names at validation and storage; verify symlink and extraction behavior when the path depends on the attacker. Follow asynchronous workers and re-uploads: a safe initial route does not establish that a draft, editor, archive or background route applies identical checks.

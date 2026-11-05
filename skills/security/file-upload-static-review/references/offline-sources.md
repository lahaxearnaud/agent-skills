# Offline source notes

Consulted 2026-11-05. These attributed summaries support offline review; external sources are optional verification pointers and do not establish a finding in the reviewed project.

## OWASP File Upload Cheat Sheet

[OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) recommends defense in depth: authorize uploads; allow only business-required types; validate names and content server-side; generate filenames; limit file and expanded archive size; store outside the web root or on a separate host where practical; and serve through a controlled handler. The declared Content-Type is user-controlled and extension or signature checks alone are insufficient. Apply controls consistently to file processing and retrieval paths and assess risks of hostile documents and archive expansion.

## Symfony uploads

[Symfony file upload documentation](https://symfony.com/doc/current/controller/upload_file.html) describes handling an `UploadedFile`, validation, generating a safe unique filename and moving files into a configured directory. It warns that original client-provided names and metadata are unsafe to trust and demonstrates deriving a safe extension from server-side guessed content. Inspect the installed version, actual constraints, destination and consumers: following the example does not itself prove the final web server or download configuration is safe.

## PHP upload handling

[PHP file upload documentation](https://www.php.net/manual/en/features.file-upload.php) describes multipart uploads, PHP's temporary file handling and configured limits. Client-provided file metadata must not be treated as trusted. Follow error handling and the actual move into permanent storage, then review processing and delivery independently. Effective limits and web server behavior depend on application and deployment settings.

# Synthetic evaluation scenarios

These scenarios are criteria for future review, not results of a controlled evaluation. No precision or recall has been measured.

1. Public upload retains original name but hosting configuration is unavailable: trace the path, report unknown execution conditions and do not assert RCE.
2. Vue accepts only images but server skips validation: inspect server storage and final use; client-only checks are not enforcement.
3. MIME is inspected but the saved extension comes from client metadata: trace actual content, filename and server handler.
4. SVG is served inline on the application origin: inspect sanitization and delivery headers; establish conditions before reporting XSS.
5. Generated key, private storage and authenticated download with no dangerous processor: avoid inferring execution from uploaded bytes.
6. Archive extraction uses entry names: examine canonical destination, symlinks and expanded-size controls.

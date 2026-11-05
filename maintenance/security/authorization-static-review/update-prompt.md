# Authorization review corpus maintenance prompt

Collect and qualify public cases relevant to static broken access control review, prioritizing function-level authorization, IDOR/BOLA, tenant isolation, property-level authorization, framework policy wiring, and server/client authorization boundaries.

For each candidate, preserve the original advisory/report URL, affected product and version, vulnerability class, actor prerequisites, vulnerable operation/resource, authorization failure, impact described by the source, and fixed version. Distinguish reviewed primary advisories from unverified search leads and synthetic scenarios. Do not treat a CVE title, scanner result, or vulnerable dependency alone as proof of an applicable code path. Do not include private repository material or unsupported impact claims. Add examples to the corpus only after source verification and preserve third-party attribution.

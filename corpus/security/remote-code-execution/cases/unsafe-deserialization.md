# unsafe deserialization

### CVE-2026-23737 — seroval JSON deserialization to JavaScript evaluation

**Family:** Unsafe JSON deserialization and indirect evaluation
**Product / versions:** seroval < 1.4.1; fixed 1.4.1
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-23737 advisory](https://github.com/advisories/GHSA-3rxj-6cgf-8cfw)
**Published:** 2026-01-21
**Consulted:** 2026-11-03
**Remote input / path to execution:** fromJSON and fromCrossJSON deserialize client-supplied data; constant overriding and error deserialization reach unsafe JavaScript evaluation.
**Preconditions:** A client-to-server transmission path, at least four requests to the same function and partial knowledge of later data processing are reported prerequisites.
**Impact reported:** Arbitrary JavaScript execution in the server process.
**Fix:** Upgrade to 1.4.1 or later; use the patched deserializer and constrain serialized type features.
**Evidence limits:** The advisory requires multi-request state and knowledge of downstream use; this is not an unconditional single-request parser finding.

### CVE-2024-52046 — Apache MINA ObjectSerializationDecoder

**Family:** Java native object deserialization
**Product / versions:** MINA core 2.2.x < 2.2.4, 2.1.x < 2.1.10, and 2.0.x < 2.0.27; patched in those releases
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2024-52046 advisory](https://github.com/advisories/GHSA-76h9-2vwh-w278)
**Published:** 2024-12-25
**Consulted:** 2026-11-03
**Remote input / path to execution:** Incoming serialized network data reaches ObjectSerializationDecoder and Java native deserialization.
**Preconditions:** The application must call IoBuffer.getObject, commonly by adding ObjectSerializationCodecFactory to an ObjectSerializationCodecFilter chain; a compatible class must be available.
**Impact reported:** Potential arbitrary code execution on the MINA server.
**Fix:** Upgrade to a fixed MINA release and explicitly allow only required class names in the decoder.
**Evidence limits:** The advisory explicitly says library presence alone is insufficient; the codec filter and accepted classes must be checked.

### CVE-2024-52577 — Apache Ignite incoming message class-filter bypass

**Family:** Java object deserialization
**Product / versions:** Ignite >= 2.6.0 < 2.17.0; fixed 2.17.0
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2024-52577 advisory](https://github.com/advisories/GHSA-8355-xj3p-hv6q)
**Published:** 2025-02-14
**Consulted:** 2026-11-03
**Remote input / path to execution:** An Ignite server deserializes a crafted incoming message on endpoints where configured serialization filters are ignored.
**Preconditions:** The attacker must reach an affected Ignite endpoint and use an object class that is present on the server classpath.
**Impact reported:** Arbitrary code execution on the Ignite server if the required class behavior is available.
**Fix:** Upgrade to 2.17.0 or later and keep strict class filters as defense in depth.
**Evidence limits:** The advisory phrases impact as possible and requires both endpoint reachability and a compatible server-side class.

### CVE-2025-27520 — BentoML HTTP payload pickle deserialization

**Family:** Python pickle deserialization
**Product / versions:** BentoML >= 1.3.4 < 1.4.3; fixed 1.4.3
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2025-27520 advisory](https://github.com/advisories/GHSA-33xw-247w-6hmc)
**Published:** 2025-04-04
**Consulted:** 2026-11-03
**Remote input / path to execution:** An HTTP request payload reaches pickle.loads when payload metadata omits buffer-lengths in the server deserializer.
**Preconditions:** An unauthenticated caller can reach an affected BentoML service endpoint that deserializes the payload.
**Impact reported:** Arbitrary Python code execution on the server.
**Fix:** Upgrade to 1.4.3 or later and replace pickle on attacker-facing data paths with a non-executable schema.
**Evidence limits:** The advisory describes an HTTP source-to-pickle sink; verify whether the service exposes the affected payload handler.

### CVE-2025-32375 — BentoML runner server pickle deserialization

**Family:** Python pickle deserialization in runner transport
**Product / versions:** BentoML >= 1.0.0a1 < 1.4.8; fixed 1.4.8
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2025-32375 advisory](https://github.com/advisories/GHSA-7v4r-c989-xh26)
**Published:** 2025-04-08
**Consulted:** 2026-11-03
**Remote input / path to execution:** The runner request handler reads attacker-controlled HTTP body bytes and deserializes them as a pickled payload based on transport headers.
**Preconditions:** The runner server must be network reachable and use the affected pickled payload container; the advisory's example binds it on a public interface.
**Impact reported:** Arbitrary code execution with runner server privileges.
**Fix:** Upgrade to 1.4.8 or later; do not expose runner transport endpoints to untrusted networks and remove pickle input.
**Evidence limits:** This is a separate runner-server path from BentoML's service payload deserializer; confirm which component and version are deployed.

### CVE-2025-14931 — smolagents Remote Python Executor pickle parser

**Family:** Python pickle deserialization
**Product / versions:** smolagents <= 1.23.0; no patched version listed in the advisory at consultation
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2025-14931 advisory](https://github.com/advisories/GHSA-q9r5-6hrr-9ph7)
**Published:** 2025-12-23
**Consulted:** 2026-11-03
**Remote input / path to execution:** The Remote Python Executor parses user-supplied pickle data without validation and executes object reconstruction code.
**Preconditions:** The advisory characterizes the network-facing executor as unauthenticated; the application must expose that executor to the attacker.
**Impact reported:** Arbitrary Python code execution in the service account context.
**Fix:** No patched version was listed as of consultation; disable the affected executor or require a vendor-confirmed fixed release and non-pickle transport.
**Evidence limits:** The advisory cites a ZDI report; package status should be rechecked before providing release guidance.

### CVE-2026-44795 — Spinnaker unsafe YAML constructors

**Family:** YAML type construction to Java class loading
**Product / versions:** orca-core and rosco-core affected before 2025.3.3, 2025.4.4 and 2026.0.3 in the respective release branches
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-44795 advisory](https://github.com/advisories/GHSA-c8q4-9h32-2ww8)
**Published:** 2026-06-15
**Consulted:** 2026-11-03
**Remote input / path to execution:** A non-safe YAML constructor used in selected deployment operations loads Java classes from YAML content.
**Preconditions:** CloudFormation deployment or CloudFoundry baking operations must be enabled and process attacker-influenced YAML.
**Impact reported:** Arbitrary Java class loading leading to RCE in Spinnaker processes.
**Fix:** Upgrade to the fixed release for the deployed branch; temporarily disable CloudFormation and CloudFoundry baking when upgrading is not possible.
**Evidence limits:** The advisory scopes impact to particular operations and release branches; unsafe YAML library use elsewhere is not proof of this CVE.

### CVE-2026-33701 — OpenTelemetry Java agent RMI instrumentation

**Family:** Java deserialization in custom RMI endpoint
**Product / versions:** opentelemetry-javaagent < 2.26.1; fixed 2.26.1
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-33701 advisory](https://github.com/advisories/GHSA-xw7x-h9fj-p2c7)
**Published:** 2026-03-23
**Consulted:** 2026-11-03
**Remote input / path to execution:** The RMI instrumentation registers a custom endpoint that deserializes incoming data without serialization filters.
**Preconditions:** All three are required: the Java agent is attached, an RMI/JMX endpoint is network reachable, and a gadget-compatible library is on the classpath.
**Impact reported:** Remote code execution as the JVM process user.
**Fix:** Upgrade to 2.26.1 or later or disable RMI instrumentation; restrict network access to RMI endpoints.
**Evidence limits:** The advisory states a three-part precondition; do not flag the dependency without verifying agent attachment, port reachability and classpath.

### CVE-2026-45051 — OpenAM WebAuthn authenticator storage deserialization

**Family:** Java deserialization of attacker-writable storage
**Product / versions:** OpenAM Community Edition <= 16.0.6; fixed 16.1.1
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-45051 advisory](https://github.com/advisories/GHSA-6c99-87fr-6q7r)
**Published:** 2026-06-24
**Consulted:** 2026-11-03
**Remote input / path to execution:** The WebAuthn module deserializes an authenticator-storage attribute associated with a user.
**Preconditions:** Not default: an attacker must first write the selected backing storage attribute and the WebAuthn authentication flow must be reachable. Delegated provisioning, directory write access or unsafe reconfiguration can create that condition.
**Impact reported:** Code execution as the application server user.
**Fix:** Upgrade to 16.1.1 or later and ensure the configured storage attribute is server-managed and not user-writable.
**Evidence limits:** The advisory labels this configuration non-default; review actual attribute mapping and provisioning access.

### CVE-2026-33264 — Apache Airflow serialized DAG class import

**Family:** Unsafe class import during serialized DAG deserialization
**Product / versions:** Apache Airflow < 3.3.0; fixed 3.3.0
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2026-33264 advisory](https://github.com/advisories/GHSA-2943-9672-r45w)
**Published:** 2026-07-07
**Consulted:** 2026-11-03
**Remote input / path to execution:** BaseSerialization.deserialize performs unrestricted import_string on an attacker-controlled class path while the Scheduler or API Server loads a serialized DAG trigger.
**Preconditions:** A DAG author can supply a serialized DAG crossing into scheduler/API-server processing; DAG authors are not intended to execute code in those processes.
**Impact reported:** Remote code execution in API Server or Scheduler process.
**Fix:** Upgrade to 3.3.0 or later; use a narrow allowed_deserialization_classes setting as defense in depth.
**Evidence limits:** The source describes a trust-boundary failure between DAG authors and control-plane services; verify the exact Airflow topology.

### GHSA-qm5c-m76r-2hfr — Laravel cookie session deserialization with encryption oracle

**Family:** Serialized session object reconstruction
**Product / versions:** Laravel framework >= 4.1.0 < 6.18.31 and >= 7.0.0 < 7.22.4; fixed 6.18.31 and 7.22.4
**Source status:** GitHub Reviewed advisory
**Source:** [GHSA-qm5c-m76r-2hfr advisory](https://github.com/advisories/GHSA-qm5c-m76r-2hfr)
**Published:** 2024-05-15
**Consulted:** 2026-11-03
**Remote input / path to execution:** A cookie-session application can accept attacker-crafted serialized session data if the app also exposes an encryption oracle that signs arbitrary plaintext.
**Preconditions:** Both the cookie session driver and an application feature that encrypts arbitrary user input for later exposure are required.
**Impact reported:** Remote code execution through crafted session reconstruction, with impact determined by the reachable object behavior.
**Fix:** Upgrade to the fixed Laravel branch and remove any arbitrary-input encryption oracle.
**Evidence limits:** Framework presence alone is not enough; the advisory requires a specific session driver and a separate application-level oracle.

### CVE-2025-61765 — python-socketio message queue pickle

**Family:** Python pickle on inter-server messages
**Product / versions:** python-socketio >= 0.8.0 < 5.14.0; fixed 5.14.0
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2025-61765 advisory](https://github.com/advisories/GHSA-g8c6-8fjj-2r4m)
**Published:** 2025-10-03
**Consulted:** 2026-11-03
**Remote input / path to execution:** Multi-server Socket.IO messages read from a configured queue backend such as Redis are deserialized using pickle.loads.
**Preconditions:** Only multi-server deployments using a message queue are affected, and the attacker must first gain access to that internal queue. Single-server or properly protected-queue deployments are not affected.
**Impact reported:** Arbitrary Python code execution as the Socket.IO server process.
**Fix:** Upgrade to 5.14.0 or later, which replaces pickle inter-server encoding with JSON, and protect the queue network.
**Evidence limits:** The maintainer explicitly limits impact to deployments with a compromised message queue.

### CVE-2025-24016 — Wazuh DistributedAPI object reconstruction

**Family:** Unsafe JSON object reconstruction and eval callback
**Product / versions:** Wazuh >= 4.4.0 < 4.9.1; fixed 4.9.1
**Source status:** GitHub Reviewed advisory
**Source:** [CVE-2025-24016 advisory](https://github.com/advisories/GHSA-hcrc-79hj-m3qh)
**Published:** 2025-02-10
**Consulted:** 2026-11-03
**Remote input / path to execution:** Serialized DistributedAPI JSON is reconstructed by as_wazuh_object; attacker-controlled exception fields can reach arbitrary Python evaluation.
**Preconditions:** API access, a compromised dashboard/cluster member, or in some configurations a compromised agent is needed; a worker-to-master route is documented.
**Impact reported:** Remote code execution on the Wazuh server process, potentially across cluster nodes.
**Fix:** Upgrade to 4.9.1 or later and remove unsafe callable/evaluation behavior from object reconstruction.
**Evidence limits:** The advisory describes multiple routes and says additional paths may exist; do not infer unauthenticated reachability from the library function alone.

### CVE-2025-55182 — React Server Components Flight protocol

**Family:** Unsafe deserialization of RSC request data
**Product / versions:** react-server-dom-parcel, react-server-dom-turbopack and react-server-dom-webpack 19.0.0, 19.1.0, 19.1.1 and 19.2.0; fixed 19.0.1, 19.1.2 and 19.2.1
**Source status:** Maintainer advisory on GitHub
**Source:** [CVE-2025-55182 advisory](https://github.com/react/react/security/advisories/GHSA-fv66-9v8q-g76r)
**Published:** 2025-12-03
**Consulted:** 2026-11-03
**Remote input / path to execution:** An unauthenticated request reaches the React Server Components Flight protocol decoder, where untrusted serialized component data can lead to server-side code execution.
**Preconditions:** The application must use a server-side React Server Components implementation with one of the affected packages; client-only React apps are not affected.
**Impact reported:** Unauthenticated remote code execution in the server process.
**Fix:** Upgrade every affected RSC package to the fixed version for its release line.
**Evidence limits:** The React advisory identifies this as CVE-2025-55182 and CWE-502. Do not double-count framework wrapper advisories that refer to this same upstream flaw.


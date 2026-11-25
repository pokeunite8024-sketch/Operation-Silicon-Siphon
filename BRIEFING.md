# CSIRT INCIDENT DOSSIER: OPERATION SILICON SIPHON

**Incident Case ID:** `INC-2026-NOV-9912`  
**Classification:** `RESTRICTED // AEGIS DYNAMICS PROPRIETARY`  
**Target Organization:** Aegis Dynamics — Advanced Neuromorphic Systems & Robotics R&D  
**Affected Host:** `aegis-eng-ws01` (Lead Hardware Engineer Workstation)  
**Assigned Investigator:** Senior Digital Forensics & Incident Response (DFIR) Specialist  

---

## 1. Executive Summary

At **03:14 UTC on November 21, 2026**, automated network monitoring sensors at Aegis Dynamics detected an anomalous spike in outbound UDP traffic directed toward an unclassified external domain. Concurrently, endpoint integrity alarms flagged unauthorized modifications within protected hardware development directories.

Aegis Dynamics is 48 hours away from tape-out for its flagship silicon architecture: the **NeuroViper-X**, an ultra-low-power neuromorphic tensor core designed for next-generation autonomous drones. If proprietary register-transfer level (RTL) Verilog sources or cryptographic bootloader manifests are compromised, the firm faces catastrophic intellectual property loss.

The Computer Security Incident Response Team (CSIRT) was immediately dispatched. The engineer's workstation was isolated from the primary corporate network, and an evidence triage package was acquired under strict chain of custody.

---

## 2. Threat Actor Profile: "VoltPhantom"

Threat Intelligence attributes this intrusion to an advanced threat group tracked as **VoltPhantom**. Known tactics, techniques, and procedures (TTPs) include:
- Pivoting through auxiliary IoT / edge devices with default or weak credentials.
- Exploiting misconfigured Unix sudo permissions (GTFOBins).
- Physical drop / staging via high-speed low-profile USB storage.
- Disguising persistence hooks as legitimate system daemons (NTP, udev, systemd).
- Covert command-and-control (C2) and key exchange via DNS tunneling to bypass egress firewalls.
- Intentionally corrupting binary headers of staging containers to evade automated Data Loss Prevention (DLP) pattern matching.

---

## 3. Scope of Evidence Provided

The incident response team collected and verified the following evidence package:

| Category | Path | Description |
| :--- | :--- | :--- |
| **Network Forensics** | `evidence/network/lab_traffic.pcap` | Full packet capture from the lab gateway switch spanning the incident window. |
| **Authentication Logs** | `evidence/endpoint/var_log/auth.log` | Linux SSH authentication, session creation, and `sudo` privilege audit logs. |
| **System & Kernel Logs** | `evidence/endpoint/var_log/syslog` | Kernel ring buffer (`dmesg`) records capturing hardware and USB peripheral attachment. |
| **User Shell History** | `evidence/endpoint/home/eng_mchen/.bash_history` | Interactive command history recovered from the engineer's profile. |
| **Scheduled Tasks** | `evidence/endpoint/etc/cron.d/.ntp-sync` | Suspicious cron definition isolated from `/etc/cron.d/`. |
| **Payload Artifact** | `evidence/endpoint/usr_local_bin/.sys_health.sh` | Shell script executed by the persistence mechanism. |
| **Staged Data Blob** | `evidence/staging/staged_telemetry.bin` | Encrypted archive recovered from `/var/tmp/` with tampered magic bytes. |

---

## 4. Rules of Engagement & Objectives

1. Determine the adversary's lateral pivot point into the engineering subnet.
2. Identify the privilege escalation vector exploited to gain `root`.
3. Extract hardware forensic identifiers of physical media introduced to the machine.
4. Pinpoint the persistence mechanism established for long-term access.
5. Reconstruct the covert DNS exfiltration channel to recover the adversary's encryption key.
6. Repair the damaged staging file header, decrypt the confidential payload, and recover the final capture flag (`ARGHYA{...}`).

---

## 5. Verification

An interactive scoring script is provided to validate your findings at each phase:
```bash
python verify_flag.py
```

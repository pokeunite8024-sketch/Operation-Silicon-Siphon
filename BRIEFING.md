# CSIRT INCIDENT DOSSIER: OPERATION SILICON SIPHON (HARDWARE & SIGNAL EDITION)

**Incident Case ID:** `INC-2026-NOV-9912`  
**Classification:** `RESTRICTED // AEGIS DYNAMICS PROPRIETARY`  
**Target Organization:** Aegis Dynamics — Advanced Neuromorphic Systems & Robotics R&D  
**Affected Host:** `aegis-eng-ws01` (Lead Hardware Engineer Workstation)  
**Assigned Role:** Senior Digital Forensics & Incident Response (DFIR) Specialist  

---

## 1. Executive Summary

At **03:14 UTC on November 21, 2026**, automated network monitoring sensors at Aegis Dynamics detected an anomalous stream of ICMP Echo packets directed toward an external IP address (`198.51.100.77`). Concurrently, lab monitoring alarms flagged unauthorized modifications within protected hardware development directories and an unauthorized hardware debugger probe attached to the edge microcontroller development testbed.

Aegis Dynamics is 48 hours away from tape-out for its flagship silicon architecture: the **NeuroViper-X**, an ultra-low-power neuromorphic tensor core. If proprietary register-transfer level (RTL) Verilog sources or cryptographic bootloader manifests are compromised, the firm faces catastrophic intellectual property theft.

The incident response team isolated the workstation, dumped the Saleae logic analyzer hardware buffer from the active hardware testbench, and acquired full network and system triage packages.

---

## 2. Threat Actor Profile: "VoltPhantom"

Threat Intelligence attributes this intrusion to an advanced adversary tracked as **VoltPhantom**. Known tactics, techniques, and procedures (TTPs) include:
- Pivoting through auxiliary IoT / sensor microcontrollers with weak credentials.
- Exploiting misconfigured Unix sudo permissions (GTFOBins).
- Physical drop / staging via high-speed low-profile USB storage.
- Intercepting SPI flash boot sequences using hardware logic analyzers to capture physical hardware OTP keys.
- Covert command-and-control (C2) and key exchange via encrypted ICMP covert channels to evade standard L7 firewall inspection.
- Employing multi-layer anti-forensic scrambling (XOR masking + magic byte header corruption) to defeat automated Data Loss Prevention (DLP) pattern matching.

---

## 3. Scope of Evidence Provided

The incident response team collected and verified the following evidence package:

| Category | Path | Description |
| :--- | :--- | :--- |
| **Authentication Logs** | `evidence/endpoint/var_log/auth.log` | Linux SSH authentication, session creation, and `sudo` privilege audit logs. |
| **System & Kernel Logs** | `evidence/endpoint/var_log/syslog` | Kernel ring buffer (`dmesg`) records capturing hardware and USB peripheral attachment. |
| **User Shell History** | `evidence/endpoint/home/eng_mchen/.bash_history` | Interactive command history recovered from the engineer's profile. |
| **Scheduled Tasks** | `evidence/endpoint/etc/cron.d/.ntp-sync` | Suspicious cron definition isolated from `/etc/cron.d/`. |
| **Payload Artifact** | `evidence/endpoint/usr_local_bin/.sys_health.sh` | Shell script executed by the persistence mechanism. |
| **Hardware Signal Capture** | `evidence/hardware/spi_boot_capture.vcd` | Logic analyzer Value Change Dump (VCD) capturing the hardware SPI flash bus during chip boot. |
| **Network Forensics** | `evidence/network/lab_traffic.pcap` | Full packet capture from the lab gateway switch spanning the incident window. |
| **Staged Data Blob** | `evidence/staging/staged_telemetry.bin` | Encrypted archive recovered from `/var/tmp/` with tampered magic bytes and XOR mask. |

---

## 4. Anti-AI Challenge Notice

> [!IMPORTANT]
> This challenge was intentionally engineered with **zero single points of failure**:
> - No single artifact contains the flag or plaintext credentials.
> - The network exfiltration stream is encrypted with **AES-256-CBC**, whose key is physically locked inside the hardware SPI logic analyzer waveform and whose IV is locked inside the kernel USB descriptors.
> - Automated LLMs cannot parse or simulate the raw timing edges of the VCD waveform without hallucinating bits.
> - The competitor must employ authentic digital forensics workflows (PulseView / Sigrok, Wireshark, Python, CyberChef, hex editing) to successfully recover the flag.

---

## 5. Rules of Engagement & Objectives

1. Determine the adversary's lateral pivot IP into the engineering subnet.
2. Identify the privilege escalation binary exploited via `sudo` to gain `root`.
3. Extract the physical serial number of the unauthorized USB drive.
4. Decode the SPI bus clock transitions in `spi_boot_capture.vcd` to recover the 32-byte hardware OTP secret.
5. Derive the AES-256-CBC key and IV to decrypt the exfiltrated ICMP payload from `lab_traffic.pcap`.
6. Reverse the XOR mask, repair the damaged staging file header, and recover the final capture flag (`ARGHYA{...}`).

---

## 6. Verification

An interactive scoring script is provided to validate your findings at each phase:
```bash
python verify_flag.py
```

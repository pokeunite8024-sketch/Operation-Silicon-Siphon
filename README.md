# Operation Silicon Siphon: The Aegis Lab Breach
### A Digital Forensics & Incident Response (DFIR) Challenge

**Category:** Digital Forensics / Host & Network Incident Response  
**Difficulty:** Intermediate (CTF / SANS / SOC Style)  
**Theme:** High-Tech Hardware Lab, Edge AI IP Exfiltration  
**Flag Format:** `ARGHYA{...}`  

---

## 🔍 Incident Overview

An unauthorized intrusion occurred on workstation `aegis-eng-ws01` in the R&D hardware laboratory at **Aegis Dynamics**, where engineers are finalizing the **NeuroViper-X** neuromorphic edge-AI chip for tape-out.

An advanced adversary ("VoltPhantom") moved laterally from an IoT sensor, escalated privileges, attached a physical USB storage drive, established hidden persistence, and exfiltrated encryption metadata across covert DNS tunnels while leaving behind a corrupted staging archive designed to bypass DLP filters.

Your mission is to perform digital forensics across the provided evidence artifacts, reconstruct the intrusion chain, and recover the flag.

---

## 📁 Evidence Package Contents

```
player_package/
├── README.md                      # This file
├── BRIEFING.md                    # Official CSIRT incident briefing & narrative
├── CHALLENGE_QUESTIONS.md         # The 6 investigation objectives & hints
├── verify_flag.py                 # Interactive terminal answer validator
└── evidence/
    ├── network/
    │   └── lab_traffic.pcap       # Gateway network capture
    ├── endpoint/
    │   ├── var_log/
    │   │   ├── auth.log           # SSH logins & privilege escalation logs
    │   │   └── syslog             # Kernel log recording USB device attachment
    │   ├── etc/
    │   │   └── cron.d/
    │   │       └── .ntp-sync      # Disguised cron persistence file
    │   ├── home/
    │   │   └── eng_mchen/
    │   │       └── .bash_history  # Interactive shell activity
    │   └── usr_local_bin/
    │       └── .sys_health.sh     # Periodic beacon script
    └── staging/
        └── staged_telemetry.bin   # Encrypted archive with tampered magic bytes
```

---

## 🛠️ Recommended Tools

- **Network Forensics:** Wireshark, `tshark`, or Python (`scapy` / `dpkt`)
- **Log Forensics:** `grep`, `awk`, text editors
- **Binary & Data Carving:** Hex editor (VS Code Hex Editor, `xxd`, `hexdump`), CyberChef
- **Archive Extraction:** Standard `unzip`, 7-Zip, or Python `zipfile`

---

## 🚀 Getting Started

1. Read `BRIEFING.md` for background and context.
2. Review the 6 objectives in `CHALLENGE_QUESTIONS.md`.
3. Investigate the artifacts in `evidence/`.
4. Validate your progress interactively at any time:
   ```bash
   python verify_flag.py
   ```

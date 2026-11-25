# Operation Silicon Siphon: The Aegis Lab Breach
### An Multi-Domain Digital Forensics & Incident Response (DFIR) Challenge

**Category:** Digital Forensics / Host, Network, Hardware & Signal Incident Response  
**Difficulty:** Advanced-Intermediate (CTF / SANS / SOC Style)  
**Theme:** High-Tech Hardware Lab, Edge AI IP Exfiltration  
**Flag Format:** `ARGHYA{...}`  

---

## 🔍 Incident Overview

An unauthorized intrusion occurred on workstation `aegis-eng-ws01` in the R&D hardware laboratory at **Aegis Dynamics**, where engineers are finalizing the **NeuroViper-X** neuromorphic edge-AI chip for tape-out.

An advanced adversary ("VoltPhantom") moved laterally from an IoT sensor, escalated privileges, attached a physical USB storage drive, intercepted the SPI bootloader key on the hardware testbench, and exfiltrated encryption metadata across an encrypted ICMP covert channel while leaving behind an obfuscated staging archive designed to bypass DLP filters.

Your mission is to perform digital forensics across the provided multi-domain evidence artifacts, reconstruct the intrusion chain, and recover the flag.

---

## 📁 Evidence Package Contents

```
player_package/
├── README.md                      # This file
├── BRIEFING.md                    # Official CSIRT incident briefing & narrative
├── CHALLENGE_QUESTIONS.md         # The 6 investigation objectives & hints
├── verify_flag.py                 # Interactive terminal answer validator
└── evidence/
    ├── endpoint/
    │   ├── var_log/
    │   │   ├── auth.log           # SSH logins & privilege escalation logs
    │   │   └── syslog             # Kernel log recording USB device attachment
    │   ├── etc/cron.d/.ntp-sync   # Disguised cron persistence file
    │   ├── home/eng_mchen/        # Interactive shell activity (.bash_history)
    │   └── usr_local_bin/         # Periodic beacon script (.sys_health.sh)
    ├── hardware/
    │   └── spi_boot_capture.vcd   # Logic analyzer capture of hardware SPI flash bus
    ├── network/
    │   └── lab_traffic.pcap       # Gateway network capture with covert ICMP traffic
    └── staging/
        └── staged_telemetry.bin   # Encrypted archive with XOR mask & corrupted magic bytes
```

---

## 🛠️ Recommended Tools

- **Hardware & Signal Forensics:** PulseView / Sigrok, Python
- **Network Forensics:** Wireshark, `tshark`
- **Cryptography & Decoding:** CyberChef, Python (`cryptography`)
- **Binary & Data Carving:** VS Code Hex Editor, `xxd`, `hexdump`
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

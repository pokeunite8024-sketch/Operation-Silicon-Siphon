#!/usr/bin/env python3
"""
Operation Silicon Siphon (AI-Resistant Edition) - Progress & Flag Validator
Usage: python verify_flag.py
"""

import sys
import hashlib

# Expected answer hashes (SHA-256 of lowercase, stripped answers)
HASH_MAP = {
    "q1": [
        "4b1725fb5db444b64ad9069d285368894f42c4f7e30f09fdcf83f74c399f2444"
    ],
    "q2": [
        "b557fead744e535425bf680c6b94f2539813ecc657b84831b7a3f1c63378ba19",
        "e6640de835ad09fb0a7367ee2e0ba99d0142c139db0272146e35538bd07479fc"
    ],
    "q3": [
        "f4e7236f02f578a5cfb6c041ad39d70dc3e9cf871f408126d60f89c7da0743b8"
    ],
    "q4": [
        "a8b7d0685f5afd4df87061d5f47163eb17b5f92e8c5c39d2b0d5d1f64b167382"
    ],
    "q5": [
        "57d89fa41611eaac006d2e7b329073dcfce0e14337c76ff124894b358895cd6b"
    ],
    "q6": [
        "2fce41caede0f0be2f69d2884ebeade14b3df7d2244ba6806f8af5a041d10c78"
    ]
}

QUESTIONS = [
    ("q1", "Q1: What is the internal IP address that initiated the unauthorized SSH connection?"),
    ("q2", "Q2: Which binary was executed with sudo without a password to escalate privileges?"),
    ("q3", "Q3: What is the Serial Number of the physical USB drive plugged into the workstation?"),
    ("q4", "Q4: What is the hardware OTP secret key decoded from the SPI flash logic analyzer waveform?"),
    ("q5", "Q5: What is the staging passkey recovered from the decrypted ICMP exfiltration stream?"),
    ("q6", "Q6: What is the final capture flag recovered from the de-obfuscated staging container?"),
]

def hash_val(val: str) -> str:
    return hashlib.sha256(val.strip().lower().encode('utf-8')).hexdigest()

def check_answer(key: str, answer: str) -> bool:
    h = hash_val(answer)
    return h in HASH_MAP.get(key, [])

def print_banner():
    print("=" * 74)
    print("      AEGIS DYNAMICS CSIRT - FORENSIC CASE EVIDENCE VALIDATOR")
    print("             Operation Silicon Siphon (AI-Resistant Edition)")
    print("=" * 74)

def main():
    print_banner()
    solved = set()

    while True:
        print(f"\n[Progress: {len(solved)}/{len(QUESTIONS)} objectives validated]")
        print("\nSelect a task:")
        for idx, (key, label) in enumerate(QUESTIONS, 1):
            status = "[x] SOLVED" if key in solved else "[ ] PENDING"
            print(f"  {idx}. {status} - {label}")
        print("  7. Verify Final Flag directly")
        print("  0. Exit")

        choice = input("\nEnter choice [0-7]: ").strip()
        if choice == "0":
            print("\nExiting validator. Good luck with the investigation!\n")
            break
        elif choice == "7":
            flag_input = input("\nEnter Final Flag (format ARGHYA{...}): ").strip()
            if check_answer("q6", flag_input):
                solved.add("q6")
                print("\n[+] CONGRATULATIONS! The final flag is VALID and ACCURATE!")
                print("[+] Incident Report Verified: Case closed successfully.")
            else:
                print("\n[-] Invalid flag. Review your signal extraction, ICMP decryption, and XOR repair.")
        elif choice.isdigit() and 1 <= int(choice) <= len(QUESTIONS):
            idx = int(choice) - 1
            key, label = QUESTIONS[idx]
            ans = input(f"\n{label}\nAnswer: ").strip()
            if check_answer(key, ans):
                solved.add(key)
                print("\n[+] CORRECT! Milestone verified.")
            else:
                print("\n[-] Incorrect answer. Check your analysis for this objective.")
        else:
            print("\n[!] Invalid selection. Please choose an option from the menu.")

        if len(solved) == len(QUESTIONS):
            print("\n" + "*" * 74)
            print("  *** 100% COMPLETE! ALL 6 FORENSIC OBJECTIVES SOLVED! ***")
            print("  Mastery demonstrated across Endpoint, Hardware VCD, Network & Binary Forensics.")
            print("*" * 74 + "\n")
            break

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nSession terminated.")

#!/usr/bin/env python3
"""
Operation Silicon Siphon - Interactive Progress & Flag Validator
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
        "283714569069484127f759e43bc6e0f21e40da426391993915794c3d583c0db5"
    ],
    "q5_domain": [
        "2fce5126358d20696cac447466da32b9980bd1346f7b2ddffbbcb5927529e02e"
    ],
    "q5_key": [
        "e61a141b9daad4eb676488fb4c9ac6b6068abb179876681b3e37fbe995dfc4f6"
    ],
    "q6": [
        "a9c4076b120a891d40d8c8c8a388165edf1f2491fdb91ceaed064cd0baa78ec1"
    ]
}

QUESTIONS = [
    ("q1", "Q1: What is the internal IP address that initiated the unauthorized SSH connection?"),
    ("q2", "Q2: Which binary was executed with sudo without a password to escalate privileges?"),
    ("q3", "Q3: What is the Serial Number of the unauthorized USB drive inserted into the workstation?"),
    ("q4", "Q4: What is the full path of the disguised persistence cron configuration file?"),
    ("q5_domain", "Q5a: What is the FQDN of the attacker's C2 domain identified in network traffic?"),
    ("q5_key", "Q5b: What is the secret decryption key extracted from the covert DNS queries?"),
    ("q6", "Q6: What is the final flag recovered from the repaired staging telemetry archive?"),
]

def hash_val(val: str) -> str:
    return hashlib.sha256(val.strip().lower().encode('utf-8')).hexdigest()

def check_answer(key: str, answer: str) -> bool:
    h = hash_val(answer)
    return h in HASH_MAP.get(key, [])

def print_banner():
    print("=" * 72)
    print("      AEGIS DYNAMICS CSIRT - FORENSIC CASE EVIDENCE VALIDATOR")
    print("                Operation Silicon Siphon (DFIR-2026)")
    print("=" * 72)

def main():
    print_banner()
    solved = set()

    while True:
        print(f"\n[Progress: {len(solved)}/{len(QUESTIONS)} questions validated]")
        print("\nSelect a task:")
        for idx, (key, label) in enumerate(QUESTIONS, 1):
            status = "[x] SOLVED" if key in solved else "[ ] PENDING"
            print(f"  {idx}. {status} - {label}")
        print("  8. Verify Final Flag directly")
        print("  0. Exit")

        choice = input("\nEnter choice [0-8]: ").strip()
        if choice == "0":
            print("\nExiting validator. Good luck with the investigation!\n")
            break
        elif choice == "8":
            flag_input = input("\nEnter Final Flag (format ARGHYA{...}): ").strip()
            if check_answer("q6", flag_input):
                solved.add("q6")
                print("\n[+] CONGRATULATIONS! The final flag is VALID and ACCURATE!")
                print("[+] Incident Report Verified: Case closed successfully.")
            else:
                print("\n[-] Invalid flag. Check your header repair and DNS secret key reconstruction.")
        elif choice.isdigit() and 1 <= int(choice) <= len(QUESTIONS):
            idx = int(choice) - 1
            key, label = QUESTIONS[idx]
            ans = input(f"\n{label}\nAnswer: ").strip()
            if check_answer(key, ans):
                solved.add(key)
                print("\n[+] CORRECT! Milestone verified.")
            else:
                print("\n[-] Incorrect answer. Review the corresponding evidence artifacts.")
        else:
            print("\n[!] Invalid selection. Please choose an option from the menu.")

        if len(solved) == len(QUESTIONS):
            print("\n" + "*" * 72)
            print("  *** 100% COMPLETE! ALL FORENSIC OBJECTIVES SOLVED! ***")
            print("  Mastery demonstrated across Endpoint, USB, Network & Binary Forensics.")
            print("*" * 72 + "\n")
            break

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nSession terminated.")

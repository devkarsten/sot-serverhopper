import subprocess
import sys
import signal

# Global variable to hold the allowed IP
allowed_ip = None

def block_outgoing_except_sotgame():
    # Block all outgoing connections except for those initiated by SoTGame.exe
    subprocess.run(["iptables", "-A", "OUTPUT", "-m", "owner", "--uid-owner", "sotgame", "-j", "ACCEPT"])
    subprocess.run(["iptables", "-A", "OUTPUT", "-m", "owner", "!", "--uid-owner", "sotgame", "-j", "DROP"])

def allow_outgoing(ip):
    # Allow outgoing connections to the specified IP address
    global allowed_ip
    allowed_ip = ip
    subprocess.run(["iptables", "-A", "OUTPUT", "-d", str(ip), "-j", "ACCEPT"])

def restore_default():
    # Restore default firewall settings
    subprocess.run(["iptables", "-F"])

def signal_handler(sig, frame):
    # Signal handler to restore default settings when script is terminated
    print("Script terminated. Restoring default firewall settings.")
    restore_default()
    sys.exit(0)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <SoTGamePort> <IP>")
        return

    sot_game_port = sys.argv[1]
    allowed_ip = sys.argv[2]

    # Set up signal handler
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    block_outgoing_except_sotgame()
    allow_outgoing(allowed_ip)

    print("Outgoing connections blocked except for SoTGame.exe and the specified IP.")

    # Keep the script running
    while True:
        pass

if __name__ == "__main__":
    main()

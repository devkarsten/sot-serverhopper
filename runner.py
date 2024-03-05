import sys
import signal
import subprocess

def block_outgoing_except_sotgame(port):
    # Block all outgoing connections except for those initiated by SoTGame.exe
    subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name="Block Outgoing Except SoTGame"', 'dir=out', 'action=block', 'program="Path_To_SoTGame.exe"', 'remoteport={}'.format(port), 'enable=yes'])

def allow_outgoing(ip):
    # Allow outgoing connections to the specified IP address
    subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name="Allow Outgoing to Server"', 'dir=out', 'action=allow', 'remoteip={}'.format(ip), 'enable=yes'])

def restore_default():
    # Restore default firewall settings
    subprocess.run(['netsh', 'advfirewall', 'reset'])

def signal_handler(sig, frame):
    # Signal handler to restore default settings when script is terminated
    print("Script terminated. Restoring default firewall settings.")
    restore_default()
    sys.exit(0)

def get_user_input(prompt):
    # Helper function to get user input
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input

def main():
    print("Welcome to the SoTGame Firewall Configuration Script!")
    print("Please enter the following information:")

    sot_game_port = int(get_user_input("Enter the port used by SoTGame.exe: "))
    allowed_ip = get_user_input("Enter the IP address of the server: ")

    # Set up signal handler
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    block_outgoing_except_sotgame(sot_game_port)
    allow_outgoing(allowed_ip)

    print("Outgoing connections blocked except for SoTGame.exe and the specified IP.")

    # Keep the script running
    while True:
        pass

if __name__ == "__main__":
    main()

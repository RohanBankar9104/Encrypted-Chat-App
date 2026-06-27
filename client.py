import socket
import threading
from datetime import datetime
from crypto_utils import encrypt_message, decrypt_message

# ==========================================
# Configuration
# ==========================================

PORT = 5555

# ==========================================
# Terminal Colors
# ==========================================

GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# ==========================================
# Connect to Server
# ==========================================

server_ip = input(f"{CYAN}Enter Server IP : {RESET}")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((server_ip, PORT))
    print(f"\n{GREEN}[✓] Connected Successfully!{RESET}")

except Exception:
    print(f"{RED}[✗] Unable to connect to server.{RESET}")
    exit()

username = input(f"{CYAN}Enter Username : {RESET}")

print("\n" + "=" * 70)
print(f"{MAGENTA}        SECURE ENCRYPTED CHAT CLIENT{RESET}")
print("=" * 70)
print(f"{YELLOW}Type your message below.")
print("Type 'exit' to disconnect.{RESET}")
print("=" * 70)

# ==========================================
# Receive Messages
# ==========================================

def receive_messages():

    while True:

        try:

            encrypted_message = client.recv(4096)

            if not encrypted_message:
                break

            message = decrypt_message(encrypted_message)

            timestamp = datetime.now().strftime("%H:%M:%S")

            print(f"\n{GREEN}[{timestamp}] {message}{RESET}")

        except:

            print(f"\n{RED}Connection closed by server.{RESET}")
            break

# ==========================================
# Send Messages
# ==========================================

def send_messages():

    while True:

        try:

            msg = input()

            if msg.lower() == "exit":

                client.close()

                print(f"{RED}\nDisconnected from server.{RESET}")

                break

            timestamp = datetime.now().strftime("%H:%M:%S")

            full_message = f"[{timestamp}] {username}: {msg}"

            encrypted_message = encrypt_message(full_message)

            client.send(encrypted_message)

        except:

            print(f"{RED}\nError while sending message.{RESET}")

            break

# ==========================================
# Start Receive Thread
# ==========================================

receive_thread = threading.Thread(target=receive_messages)

receive_thread.daemon = True

receive_thread.start()

# ==========================================
# Start Sending Messages
# ==========================================

send_messages()
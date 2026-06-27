import socket
import threading
from datetime import datetime
from crypto_utils import decrypt_message

# ================================
# Configuration
# ================================

HOST = "0.0.0.0"
PORT = 5555

clients = []

# ================================
# Terminal Colors
# ================================

GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# ================================
# Logging Functions
# ================================

def log_chat(message):
    with open("chat.log", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")


def log_encrypted(encrypted_message):
    with open("encrypted.log", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write("=" * 70 + "\n")
        file.write(f"Timestamp : {timestamp}\n\n")
        file.write("Encrypted Message\n\n")
        file.write(encrypted_message.decode())
        file.write("\n")
        file.write("=" * 70 + "\n\n")


def log_decrypted(message):
    with open("decrypted.log", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write("=" * 70 + "\n")
        file.write(f"Timestamp : {timestamp}\n\n")
        file.write("Decrypted Message\n\n")
        file.write(message)
        file.write("\n")
        file.write("=" * 70 + "\n\n")

# ================================
# Broadcast Function
# ================================

def broadcast(message, sender):

    for client in clients:

        if client != sender:

            try:
                client.send(message)

            except:
                pass

# ================================
# Client Handler
# ================================

def handle_client(client, addr):

    print(f"\n{GREEN}[+] Client Connected : {addr}{RESET}")

    while True:

        try:

            encrypted_message = client.recv(4096)

            if not encrypted_message:
                break

            message = decrypt_message(encrypted_message)

            # ==============================
            # Display Messages
            # ==============================

            print("\n" + "=" * 75)

            print(f"{CYAN}ENCRYPTED MESSAGE{RESET}")
            print("-" * 75)
            print(encrypted_message.decode())

            print("\n" + f"{GREEN}DECRYPTED MESSAGE{RESET}")
            print("-" * 75)
            print(message)

            print("=" * 75)

            # ==============================
            # Save Logs
            # ==============================

            log_encrypted(encrypted_message)
            log_decrypted(message)
            log_chat(message)

            # ==============================
            # Broadcast
            # ==============================

            broadcast(encrypted_message, client)

        except Exception as e:

            print(f"{RED}[-] Error : {e}{RESET}")
            break

    if client in clients:
        clients.remove(client)

    client.close()

    print(f"{RED}[-] Client Disconnected : {addr}{RESET}")

# ================================
# Start Server
# ================================

def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))

    server.listen(10)

    print("\n")
    print("=" * 75)
    print(f"{MAGENTA}        SECURE ENCRYPTED CHAT SERVER{RESET}")
    print("=" * 75)

    print(f"{BLUE}Listening on Port : {PORT}{RESET}")
    print(f"{BLUE}Waiting for Clients...{RESET}")

    print("=" * 75)

    while True:

        client, addr = server.accept()

        clients.append(client)

        thread = threading.Thread(
            target=handle_client,
            args=(client, addr)
        )

        thread.daemon = True
        thread.start()

# ================================
# Main
# ================================

if __name__ == "__main__":
    start_server()
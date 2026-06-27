# 🔐 Secure Encrypted Chat Application

A secure real-time multi-client chat application built with **Python**, **Socket Programming**, **Multithreading**, and **AES-256 Encryption**. The application demonstrates secure client-server communication by encrypting every message before transmission and decrypting it upon receipt, while also logging both encrypted and decrypted messages for educational analysis.

---

## 📖 Overview

Secure communication is one of the fundamental principles of cybersecurity. This project demonstrates how modern encryption techniques can be integrated into a client-server architecture to protect messages exchanged across a network.

The application allows multiple users to communicate simultaneously while encrypting every message using **AES-256 (CBC Mode)** before transmission. On the server, encrypted messages are decrypted, displayed for monitoring, and stored in dedicated log files.

This project is intended for learning **network programming**, **cryptography**, and **secure communication concepts**.

---

## ✨ Features

* 🔒 AES-256 CBC Encryption
* 💬 Real-Time Messaging
* 👥 Multi-Client Communication
* ⚡ Multi-Threaded Server
* 🛡 Secure Client-Server Architecture
* 📜 Encrypted Message Logging
* 📝 Decrypted Message Logging
* 📂 Chat History Logging
* 🕒 Timestamped Messages
* 🎨 Colorized Terminal Output
* 🔄 Real-Time Message Broadcasting
* 🌐 Cross-Platform Python Implementation

---

# 🏗️ System Architecture

```text
                  +---------------------+
                  |     Chat Server     |
                  |---------------------|
                  | AES-256 Decryption  |
                  | Broadcast Messages  |
                  | Log Encrypted Data  |
                  | Log Plaintext Data  |
                  +----------+----------+
                             |
        ---------------------------------------------
        |                    |                      |
+---------------+    +---------------+    +---------------+
|   Client A    |    |   Client B    |    |   Client C    |
| AES Encrypt   |    | AES Encrypt   |    | AES Encrypt   |
+---------------+    +---------------+    +---------------+
```

---

# 🔐 Encryption Workflow

```text
User Message
      │
      ▼
AES-256 Encryption
      │
      ▼
Encrypted Base64 Data
      │
      ▼
Network Transmission
      │
      ▼
Server Receives Ciphertext
      │
      ▼
AES-256 Decryption
      │
      ▼
Original Plaintext Message
      │
      ▼
Broadcast to Connected Clients
```

---

# 🛠️ Technologies Used

| Technology         | Purpose                      |
| ------------------ | ---------------------------- |
| Python 3           | Core Programming             |
| Socket Programming | Network Communication        |
| Multithreading     | Concurrent Client Handling   |
| PyCryptodome       | AES Encryption               |
| AES-256 CBC        | Secure Message Encryption    |
| Base64 Encoding    | Safe Ciphertext Transmission |

---

# 📂 Project Structure

```text
Secure-Encrypted-Chat/

├── client.py
├── server.py
├── crypto_utils.py

├── encrypted.log
├── decrypted.log
├── chat.log

├── README.md
└── requirements.txt
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/RohanBankar9104/Encrypted-Chat-App

cd secure-encrypted-chat
```

## Install Dependencies

```bash
pip install pycryptodome
```

---

# ▶️ Running the Application

## Start the Server

```bash
python server.py
```

Example Output

```text
===========================================================================
                SECURE ENCRYPTED CHAT SERVER
===========================================================================

Listening on Port : 5555
Waiting for Clients...
```

---

## Start the Client

Open another terminal.

```bash
python client.py
```

Enter:

```text
Enter Server IP:
Enter Username:
```

Repeat on additional terminals or machines to connect multiple clients.

---

# 📸 Example Server Output

```text
===========================================================================
ENCRYPTED MESSAGE
---------------------------------------------------------------------------

h4D0gYKhjM2dY+Xlq2cQ4Aqf8eO4oL1YQG8E4L2...

---------------------------------------------------------------------------

DECRYPTED MESSAGE

[20:45:12] Rohan: Hello everyone!

===========================================================================
```

---

# 📁 Log Files

### encrypted.log

Stores Base64 encoded encrypted messages.

```text
Timestamp : 2026-06-27 20:45:12

Encrypted Message

h4D0gYKhjM2dY+Xlq2cQ4Aqf8eO4oL1YQG8E4L2...
```

---

### decrypted.log

Stores decrypted plaintext messages.

```text
Timestamp : 2026-06-27 20:45:12

Decrypted Message

Rohan: Hello everyone!
```

---

### chat.log

Stores complete chat history.

```text
[2026-06-27 20:45:12] Rohan: Hello everyone!
```

---

# 🎯 Learning Outcomes

This project strengthened my practical understanding of:

* Cryptography Fundamentals
* AES-256 Encryption
* Socket Programming
* Secure Network Communication
* Client-Server Architecture
* Multithreading
* Concurrent Programming
* Logging & Monitoring
* Cybersecurity Best Practices

---

# 🔮 Future Improvements

* 🔑 RSA Key Exchange
* 🔐 End-to-End Encryption
* 👤 User Authentication
* 💾 SQLite Database
* 🖥 GUI Interface (Tkinter/PyQt6)
* 📁 Secure File Sharing
* 💬 Private Chat Rooms
* 🌍 Cross-Network Communication
* 📊 Server Dashboard

---

# ⚠️ Security Notice

This project is intended for **educational purposes**.

The AES key is currently hardcoded to simplify learning and demonstration. In production, encryption keys should be securely generated, exchanged, and stored using appropriate key management practices.

---

# 👨‍💻 Author

## **Rohan Bankar**

Cybersecurity Enthusiast • VAPT • Networking Learner

---

# 📜 License


Feel free to fork, modify, and use this project for educational purposes.

---

## ⭐ If you found this project useful, consider giving it a star!

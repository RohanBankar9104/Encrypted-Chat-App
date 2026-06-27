from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
import base64

# ==================================================
# AES-256 Secret Key (32 Bytes)
# NOTE:
# For educational purposes only.
# In production, load this key securely from
# environment variables or a secure key vault.
# ==================================================

KEY = b'1234567890abcdef1234567890abcdef'


# ==================================================
# Encrypt Message
# ==================================================

def encrypt_message(message):
    """
    Encrypts a plaintext message using AES-256 CBC.
    Returns Base64 encoded encrypted data.
    """

    # Generate Random IV
    iv = get_random_bytes(16)

    # Create AES Cipher
    cipher = AES.new(KEY, AES.MODE_CBC, iv)

    # Pad plaintext
    padded_data = pad(message.encode(), AES.block_size)

    # Encrypt
    ciphertext = cipher.encrypt(padded_data)

    # Return IV + Ciphertext
    encrypted = iv + ciphertext

    return base64.b64encode(encrypted)


# ==================================================
# Decrypt Message
# ==================================================

def decrypt_message(encrypted_data):
    """
    Decrypts Base64 encoded AES-256 encrypted data.
    Returns original plaintext.
    """

    # Decode Base64
    encrypted = base64.b64decode(encrypted_data)

    # Extract IV
    iv = encrypted[:16]

    # Extract Ciphertext
    ciphertext = encrypted[16:]

    # Create AES Cipher
    cipher = AES.new(KEY, AES.MODE_CBC, iv)

    # Decrypt
    decrypted = cipher.decrypt(ciphertext)

    # Remove Padding
    plaintext = unpad(decrypted, AES.block_size)

    return plaintext.decode()
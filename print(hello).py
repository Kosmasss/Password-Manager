import os
import json
from cryptography import Fernet

# Function to generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

# Function to load the key
def load_key():
    return open('key.key', 'rb').read()

# Encrypt data
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

# Decrypt data
def decrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()

# Save passwords to a file
def save_passwords(passwords, key):
    encrypted_data = encrypt_data(json.dumps(passwords), key)
    with open('passwords.enc', 'wb') as file:
        file.write(encrypted_data)
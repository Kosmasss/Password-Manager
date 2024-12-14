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

def load_passwords(key):
    if not os.path.exists('passwords.enc'):
        return {}
    with open('passwords.enc', 'rb') as file:
        encrypted_data = file.read()
    return json.loads(decrypt_data(encrypted_data, key))

# Add a new password
def add_password(service, username, password, key):
    passwords = load_passwords(key)
    passwords[service] = {'username': username, 'password': password}
    save_passwords(passwords, key)
    print(f"Password for {service} added successfully.")

# Search for a password
def search_password(service, key):
    passwords = load_passwords(key)
    if service in passwords:
        print(f"Service: {service}")
        print(f"Username: {passwords[service]['username']}")
        print(f"Password: {passwords[service]['password']}")
    else:
        print(f"No password found for service: {service}")

        # Main function to interact with the password manager
def main():
    if not os.path.exists('key.key'):
        print("Key not found. Generating a new key...")
        generate_key()

    key = load_key()

    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. Search for a password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            service = input("Enter the service: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_password(service, username, password, key)
        elif choice == '2':
            service = input("Enter the service to search for: ")
            search_password(service, key)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
 

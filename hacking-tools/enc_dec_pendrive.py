#!/usr/bin/python
#coding: utf8

import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

# Define the USB drive path
usb_drive = "D:\\"

# Define the password for the encryption
password = input("Enter the password for encryption: ")

# Convert password to bytes
password_bytes = password.encode()

# Generate a salt
salt = os.urandom(16)

# Derive the key from the password and salt
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    iterations=100000,
    length=32,
    salt=salt,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password_bytes))

# Create an instance of Fernet class
fernet = Fernet(key)

def encrypt_usb():
    # Encrypt all files in the USB drive
    for root, dirs, files in os.walk(usb_drive):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            with open(file_path, "wb") as f:
                f.write(encrypted_data)

    print("USB drive encrypted successfully!")

def decrypt_usb():
    # Decrypt all files in the USB drive
    for root, dirs, files in os.walk(usb_drive):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                data = f.read()
            decrypted_data = fernet.decrypt(data)
            with open(file_path, "wb") as f:
                f.write(decrypted_data)

    print("USB drive decrypted successfully!")

encrypt_usb()

# Prompt user to decrypt the drive
decrypt = input("Do you want to decrypt the USB drive? (yes/no) ")

if decrypt.lower() == "yes":
    decrypt_usb()
else:
    print("USB drive remains encrypted.")

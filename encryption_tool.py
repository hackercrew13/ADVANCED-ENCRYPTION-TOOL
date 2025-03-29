from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def pad(data):
    return data + b" " * (16 - len(data) % 16)

def encrypt_file(file_name, key):
    if not os.path.exists(file_name):
        print(f"Error: File '{file_name}' not found.")
        return
    
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_name, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(pad(plaintext))
    with open(file_name + ".enc", 'wb') as f:
        f.write(ciphertext)
    print(f"File '{file_name}' encrypted successfully.")

def decrypt_file(file_name, key):
    if not os.path.exists(file_name):
        print(f"Error: File '{file_name}' not found.")
        return
    
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_name, 'rb') as f:
        ciphertext = f.read()
    plaintext = cipher.decrypt(ciphertext).rstrip(b" ")
    with open(file_name.replace(".enc", ""), 'wb') as f:
        f.write(plaintext)
    print(f"File '{file_name}' decrypted successfully.")

if __name__ == "__main__":
    key = get_random_bytes(16)  # 128-bit AES key
    print("AES Encryption Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a file? ").lower()
    file_name = input("Enter file name: ")
    
    if choice == 'e':
        encrypt_file(file_name, key)
    elif choice == 'd':
        decrypt_file(file_name, key)
    else:
        print("Invalid choice!")

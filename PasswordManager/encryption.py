from cryptography.fernet import Fernet

key = "V9PbIrvv6NMaKk1z0-ANCq9pKTWqrEgSHnlnlFHh6C8="
key2 = ""
cipher = Fernet(key)

encrypted = cipher.encrypt("Hola mundo".encode())
print(f"Encrypted message: {encrypted}")

decrypted = cipher.decrypt(encrypted).decode()
print(f"Decrypted message: {decrypted}")
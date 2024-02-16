import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from manage_dotenv import write_dotenv_encryption_key
load_dotenv()

dir = "Python 100 DAYS/PasswordManager/"

try:
    key = os.getenv("ENCRYPTION_KEY")
    encryptor = Fernet(key)
except TypeError as err:
    print("\nNo encryption keys found.\n")
    generate_encryption_key = input ("Would you like to generate your encryption key? (y/n): ")
    if (generate_encryption_key == 'y'):
        key = Fernet.generate_key()
        write_dotenv_encryption_key(dir,key="ENCRYPTION_KEY",value=key.decode())
        print(f"Your encryption key is: {key.decode()}")
        encryptor = Fernet(key)
    else:
        print(f"\nWill not proceed if there is not an encryption (key) for encryptor: {err}")
else:
    encryptor = Fernet(key)
    

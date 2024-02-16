import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from manage_dotenv import write_dotenv_encryption_key

from tkinter import *
from tkinter import messagebox
load_dotenv()

os.chdir("Python 100 DAYS/PasswordManager")

try:
    
    key = os.getenv("ENCRYPTION_KEY")
    encryptor = Fernet(key)
except TypeError as err:
    info = messagebox.showinfo(title="ENCRYPTION KEY",message="Your encryption key was NOT succesfully loaded.")
    generate_encryption_key = messagebox.askquestion(title="GENERATE ENCRYPTION KEY",message="Would you like to generate your encryption key?")
    if (generate_encryption_key == 'yes'):
        key = Fernet.generate_key()
        write_dotenv_encryption_key(os.getcwd(),key="ENCRYPTION_KEY",value=key.decode())
        print(f"Your encryption key is: {key.decode()}")
        encryptor = Fernet(key)
    else:
        print(f"\nWill not proceed if there is not an encryption (key) for encryptor: {err}")
else:
    info = messagebox.showinfo(title="ENCRYPTION KEY",message="Your encryption key was succesfully loaded")
    encryptor = Fernet(key)
    

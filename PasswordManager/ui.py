from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import pyperclip
import json 
from password_generator import PasswordGenerator
import os

class UI:

    def __init__(self,encryptor:Fernet):
        self.window = Tk()
        self.encryptor = encryptor
        
        #CONFIG TITLE AND SIZE
        self.window.title("Password Manager")
        self.window.minsize(width=200,height=300)
        self.window.config(padx=20,pady=20)
        #CREATE CANVAS FOR IMG
        self.canvas = Canvas(width=200,height=200,bg="#f7f5dd", highlightthickness=0)
        self.lock_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100,100,image=self.lock_img)
        self.canvas.grid(row=2,column=2)
        #WEBSITE AND MAIL/USERNAME LABELS
        self.website_title_label = Label(self.window,text="Website: ")
        self.mail_title_label = Label(self.window,text="Email/Username: ")
        self.website_entry = Entry(self.window)
        self.mail_entry = Entry(self.window)
        self.website_title_label.grid(row=3,column=1)
        self.mail_title_label.grid(row=4,column=1)
        self.website_entry.grid(row=3,column=2)
        self.mail_entry.grid(row=4,column=2)
        #GENERATE BUTTON
        self.generate_password_btn = Button(self.window,text="Generate Password",command=self.genPassword)
        self.generate_password_btn.grid(row=5,column=3,padx=10,pady=10)
        # ENTER PASSWORD LABEL AND BUTTON
        self.enter_password_btn = Button(self.window,text="Save Password",command=self.savePassword)
        self.enter_password_entry = Entry(self.window)
        self.enter_password_lbl = Label(self.window,text="Password: ")
        self.enter_password_btn.grid(row=6,column=2,padx=10,pady=10)
        self.enter_password_entry.grid(row=5,column=2,padx=10,pady=10)
        self.enter_password_lbl.grid(row=5,column=1,padx=10,pady=10)
        #SEARCH PASSWORD BUTTON 
        self.search_password_btn = Button(self.window,text="Search Password",command=self.searchPassword)
        self.search_password_btn.grid(row=6, column=3)

        #Setup password gen
        self.pwo = PasswordGenerator()
        self.pwo.minlen = 12
        self.pwo.maxlen = 16
        # WINDOW POP UP ATTRIBUTES 
        self.window.attributes("-topmost",True)
        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()


    def genPassword(self):
        password = self.pwo.generate()
        self.set_text(password)


    def set_text(self,text):
        self.enter_password_entry.delete(0,END)
        self.enter_password_entry.insert(0,text)
        return

    def getPassword(self):
        self.entry = self.enter_password_entry.get()
        self.entry.strip()
        return self.entry

    def getUsername(self):
        self.entry = self.mail_entry.get()
        self.entry.strip()
        return self.entry

    def getWebsite(self):
        self.entry = self.website_entry.get()
        self.entry.strip()
        return self.entry

    def savePassword(self):
        data = self.collectData()
        username = self.getUsername()
        password = self.getPassword()
        website = self.getWebsite()

        #ENCRYPTION
        password = self.cipher(password)
        
        if (username == "" or website == "" or password == ""):
            messagebox.showinfo(title="PASSWORD MANAGER", message="MISSING VALUES!")
       
        else:
            dictionary = {}
            dictionary["username"] = username
            dictionary["password"] = password
            dictionary["website"] = website
            save = messagebox.askquestion(title="Save password?",message=f"Would you like to save this credentials? \n Username:{username} \n Website:{website} \n Password: {self.decipher(password)}")
            if (save == 'yes'):
                data.append(dictionary)
                json_object = json.dumps(data,indent=3)
                with open("users\default user\default_passwords.json",'w') as outfile:
                    outfile.write(json_object)
                messagebox.showinfo(title="PASSWORD MANAGER", message="PASSWORD SAVED!\n username:{} \n website:{} \n password:{}".format(username,website,self.decipher(password)))
            elif (save == 'no'):
                pass

    def searchPassword(self):
        data = self.collectData()
        username = self.getUsername()
        website = self.getWebsite()
        is_user_found = False
        for dict in data:
            if dict["username"] == username and dict["website"] == website:
                is_user_found = True
                password = dict["password"]
                # DECRYPTION
                password = self.decipher(password)
            else:
                pass
        if (is_user_found == True):
            messagebox.showinfo(title="Password",message=f"Your password is: {password} \n copied to clipboard!")   
            pyperclip.copy(password) 
        else:
            messagebox.showinfo(title="Password",message="Your user was not found.")  
        is_user_found = False
    
    def collectData(self):
        
        try:
            with open("users\default user\default_passwords.json", 'r') as openfile:
                json_object = json.loads(openfile.read())  
        except json.JSONDecodeError:
            json_object = []   
        except FileNotFoundError:
            with open("users\default user\default_passwords.json",'w') as openfile:
                json_object = []
        return json_object
    
    """
    ENCRYPT AND DECRYPT
    """

    def cipher(self,message: str):
        encMessage = self.encryptor.encrypt(message.encode())
        return encMessage.decode()

    def decipher(self,encMessage: str):
        decMessage = self.encryptor.decrypt(encMessage).decode()
        return decMessage
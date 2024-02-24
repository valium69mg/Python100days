from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import pyperclip
import json 
from password_generator import PasswordGenerator
import os
from tkinter import ttk

class UI:
    """
    HERE WE INITIALIZE THE MAIN WINDOW WITH ALL ITS ATTRIBUTES
    (WIDTH, HEIGHT, LABELS, BUTTONS, ENTRIES, IMAGES, ETC)
    """
    def __init__(self,encryptor:Fernet):
        #INITIALIZE THE WINDOW
        self.window = Tk()
        self.window.wait_visibility()
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
        # THE CODE BELOW EXTRACTS WEBSITE AND USERNAME STORED DATA OF THE USER
        # TO DISPLAY IT ON THE COMBOBOXES
        self.saved_websites = []
        self.saved_mails =  []
        # WE UPDATE THE COMBOBOX VALUES WITH THE FUNCTION BELOW
        self.website_entry = ttk.Combobox(
            self.window,
            postcommand=self.update_combobox
            )
        self.mail_entry = ttk.Combobox(
            self.window,
            postcommand=self.update_combobox
         )
        self.website_title_label.grid(row=3,column=1)
        self.mail_title_label.grid(row=4,column=1)
        self.website_entry.grid(row=3,column=2)
        self.mail_entry.grid(row=4,column=2)
        #GENERATE BUTTON
        self.generate_password_btn = Button(self.window,text="Generate Password",command=self.genPassword)
        self.generate_password_btn.grid(row=6, column=3,padx=10,pady=10)
        # ENTER PASSWORD LABEL AND BUTTON
        self.enter_password_btn = Button(self.window,text="Save Password",command=self.savePassword)
        self.enter_password_entry = Entry(self.window)
        self.enter_password_lbl = Label(self.window,text="Password: ")
        self.enter_password_btn.grid(row=6,column=2,padx=10,pady=10)
        self.enter_password_entry.grid(row=5,column=2,padx=10,pady=10)
        self.enter_password_lbl.grid(row=5,column=1,padx=10,pady=10)
        #SEARCH PASSWORD BUTTON 
        self.search_password_btn = Button(self.window,text="Search Password",command=self.searchPassword)
        self.search_password_btn.grid(row=7,column=2)
        # DISPLAY ALL SAVED PASSWORDS 
        self.display_all_passwords_btn = Button(self.window,text="Display all passwords",command=self.display_all_passwords_window)
        self.display_all_passwords_btn.grid(row=5,column=3)
        self.pwo = PasswordGenerator()
        self.pwo.minlen = 12
        self.pwo.maxlen = 16
        # WINDOW POP UP ATTRIBUTES 
        self.window.attributes("-topmost",True)
        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()

    """
    THIS FUNCTION GENERATES A RANDOM PASSWORD USING PWO LIBRARY
    THE GENERATED PASSWORD IS BETWEEN 12 AND 16 CHARACTERS
    """
    def genPassword(self):
        password = self.pwo.generate()
        self.set_text(password)

    """
    THIS SET TEXT FUNCTION CHANGES THE TEXT IN THE PASSWORD ENTRY
    IT IS USED BY THE GEN PASSWORD FUNCTION FOR DISPLAYING THE RANDOMLY GENERATED
    PASSWORD 
    """

    def set_text(self,text):
        self.enter_password_entry.delete(0,END)
        self.enter_password_entry.insert(0,text)
        return
    """
    THESE FUNTIONS RETRIEVE THE DATA FROM THE ENTRIES AT THE MAIN WINDOW
    """
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
    """
    THE savePassword FUNCTION SAVES THE CREDENTIALS ENTERED ON A JSON FILE
    THE PASSWORD CREDENTIAL IS CIPHERED THROUG AES ENCRYPTION
    """

    def savePassword(self):
        data = self.collectData()
        username = self.getUsername()
        password = self.getPassword()
        
        website = self.getWebsite()
        # WE SAVE THE DATA INTO A DICTIONARY IN ORDER TO WORK WITH IT 
        data_to_save = {}
        data_to_save ["username"] = username
        data_to_save ["password"] = password
        data_to_save ["website"] = website
        
        if (username == "" or website == "" or password == ""):
            messagebox.showinfo(title="PASSWORD MANAGER", message="MISSING VALUES!")  
            return 
        else:
            #ENCRYPTION
            #CIPHER THE PASSWORD WE ARE GOING TO SAVE
            password = self.cipher(password)
            """
            CHECK IF THE CREDENTIALS ARE ALREADY ON THE DATA BASE
            """
            for dict in data:
                if (data_to_save["username"] == dict["username"] and data_to_save["website"] == dict["website"]):
                    messagebox.showinfo(title="PASSWORD MANAGER", message="This credentials are already saved!")
                    return 
            """
            IF NOT WE PROCEED TO SAVE 
            """
            save = messagebox.askquestion(title="Save password?",message=f"Would you like to save this credentials? \n Username:{username} \n Website:{website} \n Password: {self.decipher(password)}")
            if (save == 'yes'):
                data_to_save["password"] = self.cipher(data_to_save["password"])
                data.append(data_to_save)
                json_object = json.dumps(data,indent=3)
                with open("users\default user\default_passwords.json",'w') as outfile:
                    outfile.write(json_object)
                messagebox.showinfo(title="PASSWORD MANAGER", message="PASSWORD SAVED!\n username:{} \n website:{} \n password:{}".format(username,website,self.decipher(password)))
                # WE UPDATE THE COMBOBOX VALUES WITH THE FUNCTION BELOW
                self.update_combobox()
                return 
            elif (save == 'no'):
                pass
        
        """
        THE searchPassword FUNCTION SEARCHES A PASSWORD BY THE USERNAME AND WEBSITE
        IN THE JSON FILE

        WHEN THE PASSWORD OF THE USER AND WEBSITE IS FOUND IT DECIPHERS IT USING THE
        ENCRYPTION KEY IN .ENV FILE
        """
    def searchPassword(self):
        data = self.collectData()
        username = self.getUsername()
        website = self.getWebsite()
        is_user_found = False
        decrypt_success = False
        for dict in data:
            if dict["username"] == username and dict["website"] == website:
                is_user_found = True
                password = dict["password"]
                # DECRYPTION
                try:
                    password = self.decipher(password)
                except:
                    messagebox.showerror("DECIPHER ERROR",message="THE ENCRYPTING KEY IS INVALID!")
                else:
                    decrypt_success = True
            else:
                pass
        if (is_user_found == True and decrypt_success == True):
            messagebox.showinfo(title="Password",message=f"Your password is: {password} \n copied to clipboard!")   
            pyperclip.copy(password) 
        else:
            messagebox.showinfo(title="Password",message="Your user was not found.")  
        is_user_found = False
    
    """
    THIS FUNCTION COLLECTS THE DATA FROM THE JSON FILE

    IN CASE THAT THE JSON FILE DOES NOT EXIST IT CREATES AN EMPTY JSON FILE

    ON THE OTHER HAND IF THE JSON FILE EXIST BUT IT IS EMPTY THE RETURN DATA IS 
    AN EMPTY LIST []

    FINALLY IF IT FOUNDS THE FILE AND THE FILE HAS ELEMENTS IT TRANSFORMS THE JSON
    FILE INTO A LIST OF DICTIONARIES WE CAN WORK WITH
    """

    
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
    ENCRYPT AND DECRYPT FUNCTIONS

    THIS FUNCTIONS USE THE FERNET CLASS MODULE
    AND AN ENCRYPT KEY TO ENCRYPT AND DECRYPT PASSWORDS
    FROM THE FILE 
    """

    def cipher(self,message: str):
        encMessage = self.encryptor.encrypt(message.encode())
        return encMessage.decode()

    def decipher(self,encMessage: str):
        decMessage = self.encryptor.decrypt(encMessage).decode()
        return decMessage
    
    """
    THIS FUNCTION IS TO UPDATE THE COMBOBOXES OPTIONS 
    
    """
    def update_combobox(self):
        data = self.collectData()
        for dict in data: 
            if (dict["website"] not in self.saved_websites):
                self.saved_websites.append(dict["website"])
            if (dict["username"] not in self.saved_mails):
                self.saved_mails.append(dict["username"])
        self.saved_websites = self.quicksort(self.saved_websites)
        self.saved_mails = self.quicksort(self.saved_mails)
        self.website_entry['values'] = self.saved_websites
        self.mail_entry['values'] = self.saved_mails
        return
    """
    QUICK SORT FUNCTION TO SORT THE LIST OF THE COMBOBOXES 
    """
    def quicksort(self,values):
        if len(values) <= 1:
            return values
        less_than_pivot = []
        greater_than_pivot = []
        pivot = values[0]
        for value in values[1:]:
            if value <= pivot:
                less_than_pivot.append(value)
            else:
                greater_than_pivot.append(value)

        return self.quicksort(less_than_pivot) + [pivot] + self.quicksort(greater_than_pivot)

    """
    WINDOW TO DISPLAY ALL PASSWORDS
    """
    def display_all_passwords_window(self):
     
        # Toplevel object which will 
        # be treated as a new window
        self.newWindow = Toplevel(self.window)
        
        # sets the title of the
        # Toplevel widget
        self.newWindow.title("Passord manager")
    
        # sets the geometry of toplevel
       # self.newWindow.geometry("600x600")
    
        # WE MAKE IT THE TOP MOST WINDOW AND CENTER IT
        self.newWindow.attributes("-topmost",True)
        x = self.window.winfo_x() + self.window.winfo_width()//2 - self.newWindow.winfo_width()//2
        y = self.window.winfo_y() + self.window.winfo_height()//2 - self.newWindow.winfo_height()//2
        self.newWindow.geometry(f"+{x}+{y}")
        
        
        """
        MAKE THE LIST OF USERNAMES WEBSITES AND PASSWORDS
        """
        data = self.collectData()
        list_of_credetials = []
        for dict in data:
            credentials = dict["website"] + ", " + dict["username"] + ", " + self.decipher(dict["password"])
            list_of_credetials.append(credentials)
        list_of_credetials = self.quicksort(list_of_credetials)
        
        # COMPUTE THE LONGEST STRING IN OUR CREDENTIALS TO DISPLAY
        characters_of_biggest_string = 0
        for string in list_of_credetials:
            if (len(string) > characters_of_biggest_string):
                    characters_of_biggest_string = len(string)
        # MAKE THE SCROLL BAR AND THE LIST BOX FOR THE PASSWORD LIST
        scrollbar = Scrollbar(self.newWindow)
        self.listbox = Listbox(self.newWindow,height=int(len(list_of_credetials)//1.5),width=characters_of_biggest_string)  
        
        # SCROLL BAR AND LISTBOX LINK
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command = self.listbox.yview) 
        # WE DUMP THE CREDENTIAL VALUES INTO THE LIST BOX
        
        for i in range(0,len(list_of_credetials)-1):
            self.listbox.insert(i, list_of_credetials[i]) 
            
        

        self.newWindow.wait_visibility() 
        self.listbox.pack(side = LEFT, fill = BOTH)
        scrollbar.pack(side=RIGHT,fill=BOTH)
        # WE BIND THE LIST BOX COPY FUNCTION TO THE LISTBOX 
        self.listbox.bind('<Double-Button-1>', self.listbox_copy)

    """
    PASTE THE PASSWORD TO THE CLIPBOARD WHEN A USER SELECTS AN OPTION FROM THE LIST BOX

    """

    def listbox_copy(self,event):
        all_items = self.listbox.get(0, END)
        index_of_selected = self.listbox.curselection()[0]
        item_to_copy = all_items[index_of_selected]
        
        """
        COMPARE THE DATA OF THE LIST BOX TO THE DATABASE DATA
        """
        data = self.collectData()
        for dict in data:
            if (item_to_copy.find(self.decipher(dict["password"])) != -1):
                item_to_copy = self.decipher(dict["password"])
                break 
        messagebox.showinfo(title="Password",message=f"Your password is: {item_to_copy} \n copied to clipboard!")  
        pyperclip.copy(item_to_copy)
       
        
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import pyperclip
import json 
from password_generator import PasswordGenerator
from tkinter import ttk

class UI:
    """
    HERE WE INITIALIZE THE MAIN WINDOW WITH ALL ITS ATTRIBUTES
    (WIDTH, HEIGHT, LABELS, BUTTONS, ENTRIES, IMAGES, ETC)
    """
    def __init__(self,encryptor:Fernet):
        """
        CREATE THE ROOT WINDOW AND SETTING UP INITIAL PARAMETERS
        """
        self.window = Tk()
        self.encryptor = encryptor
        self.window.title("Password Manager")
        self.window.minsize(width=200,height=300)
        self.window.config(padx=20,pady=20)
        """
        IMAGE OF THE APP PASSWORD MANAGER 
        """
        self.canvas = Canvas(width=200,height=200,bg="#f7f5dd", highlightthickness=0)
        self.lock_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100,100,image=self.lock_img)
        self.canvas.grid(row=2,column=2)

        
        """
        SET UP AND PLACEMENT OF THE COMBOBOXES AND THEIR LABELS
        """
        # WEBSITE AND MAIL/USERNAME LABELS   
        self.website_title_label = Label(self.window,text="Website: ")
        self.mail_title_label = Label(self.window,text="Email/Username: ")
        # VARIABLES FOR THE DROP DOWN LIST OF THE COMBOBOXES
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
        # LABEL PLACEMENT FOR WEBSITE AND USERNAME
        self.website_title_label.grid(row=3,column=1)
        self.mail_title_label.grid(row=4,column=1)
        self.website_entry.grid(row=3,column=2)
        self.mail_entry.grid(row=4,column=2)
        """
        GENERATE RANDOM PASSWORD HANDLER
        THIS IS A BUTTON THAT GENERATES A RANDOM SECURE 
        PASSWORD AND DISPLAYS IT ON THE PASSWORD ENTRY ELEMENT
        """
        #GENERATE BUTTON
        self.generate_password_btn = Button(self.window,text="Generate Password",command=self.genPassword)
        self.generate_password_btn.grid(row=6, column=3,padx=10,pady=10)
        """
        BUTTONS THAT HANDLE: SAVE, SEARCH AND DISPLAY ALL PASSWORDS
        """
        # ENTER PASSWORD BUTTON, ENTRY AND LABEL
        self.enter_password_btn = Button(self.window,text="Save Password",command=self.savePassword)
        self.enter_password_entry = Entry(self.window)
        self.enter_password_lbl = Label(self.window,text="Password: ")
        # PLACEMENT OF THE SAVE PASSWORD BUTTON, ENTRY AND LABEL
        self.enter_password_btn.grid(row=6,column=2,padx=10,pady=10)
        self.enter_password_entry.grid(row=5,column=2,padx=10,pady=10)
        self.enter_password_lbl.grid(row=5,column=1,padx=10,pady=10)
        #SEARCH PASSWORD BUTTON DECLARATION AND PLACEMENT
        self.search_password_btn = Button(self.window,text="Search Password",command=self.searchPassword)
        self.search_password_btn.grid(row=7,column=2)
        # DISPLAY ALL SAVED PASSWORDS BUTTON AND PLACEMENT
        self.display_all_passwords_btn = Button(self.window,text="Display all passwords",command=self.display_all_passwords_window)
        self.display_all_passwords_btn.grid(row=5,column=3)

        """
        INITIATION OF PASSWORD GENERATOR CLASS
        IT LIMITS THE PASSWORD GENERATED TO 12-16 CHARACTERS
        """
        self.pwo = PasswordGenerator()
        self.pwo.minlen = 12
        self.pwo.maxlen = 16
        """
        WINDOW POP UP ATTRIBUTES
        HERE WE CONTROLL WHAT THE WINDOW DOES ONCE DISPLAYED
        LIKE CENTERING AND BE ON THE MOST TOP POSITION
        """
        # WINDOW POP UP ATTRIBUTES 
        self.window.attributes("-topmost",True)
        self.window.eval('tk::PlaceWindow . center')
        self.window.wait_visibility()
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
        """
        WE MAKE SURE THE USER HAS INTRODUCED THE NEEDED CREDENTIALS FOR 
        PASSWORD STORAGE
        """
        if (self.getUsername() == "" or self.getWebsite() == "" or self.getPassword() == ""):
            messagebox.showinfo(title="PASSWORD MANAGER", message="MISSING VALUES!")  
            return 
        else: 
            # WE CALL OUR STORED DATA
            data = self.collectData() 
            # WE SAVE THE DATA INTO A DICTIONARY IN ORDER TO WORK WITH IT 
            data_to_save = {}
            data_to_save ["username"] = self.getUsername()
            data_to_save ["password"] = self.cipher(self.getPassword()) #ENCRYPTION
            data_to_save ["website"] = self.getWebsite()    
            """
            CHECK IF THE CREDENTIALS ARE ALREADY ON THE DATA BASE
            IF SO ASK THE USER IF HE WANTS THE CREDENTIALS UPDATED
            """
            if (self.credentials_on_database(self.getWebsite(),self.getUsername()) == True): 
                messagebox.showerror("USER ALREADY REGISTERED",message="This credentials are already saved!")
                update = messagebox.askquestion(title="PASSWORD MANAGER",message=f"Would you like to update this credentials? \nUsername: {self.getUsername()} \n Website:{self.getWebsite()}")
                if (update == 'no'):
                    return 
                elif (update == 'yes'):   
                    for dict in data:
                        if (dict["website"] == data_to_save["website"] and dict["username"] == data_to_save["username"]):
                            index_of_dict = data.index(dict)
                            data[index_of_dict] = data_to_save
                            json_object = json.dumps(data,indent=3)  
                            with open("users\default user\default_passwords.json",'w') as outfile:
                                outfile.write(json_object)   
                            messagebox.showinfo(title="PASSWORD MANAGER", message="\nPASSWORD SAVED!\n username: {} \n website: {} \n password: {}".format(self.getUsername(),self.getWebsite(),self.getPassword()))    
                            return     
            else:           
                """
                IF THE CREDENTIALS ARE NOT ON DATA BASE WE PROCEED TO SAVE THEM 
                """
                save = messagebox.askquestion(title="Save password?",message=f"Would you like to save this credentials? \nUsername: {self.getUsername()} \nWebsite: {self.getWebsite()} \nPassword: {self.getPassword()}")
                if (save == 'yes'): 
                    data.append(data_to_save)
                    json_object = json.dumps(data,indent=3)
                    with open("users\default user\default_passwords.json",'w') as outfile:
                        outfile.write(json_object)
                    messagebox.showinfo(title="PASSWORD MANAGER", message="\nPASSWORD SAVED!\n username: {} \n website: {} \n password: {}".format(self.getUsername(),self.getWebsite(),self.getPassword()))
                    # WE UPDATE THE COMBOBOX VALUES WITH THE FUNCTION BELOW
                    self.update_combobox()
                    return 
                elif (save == 'no'):
                    return 
        
        """
        THE searchPassword FUNCTION SEARCHES A PASSWORD BY THE USERNAME AND WEBSITE
        IN THE JSON FILE

        WHEN THE PASSWORD OF THE USER AND WEBSITE IS FOUND IT DECIPHERS IT USING THE
        ENCRYPTION KEY IN .ENV FILE
        """
    def searchPassword(self):
        decrypt_success = False
        if (self.credentials_on_database(self.getWebsite(),self.getUsername()) == True):
            # DECRYPTION
            try:
                password = self.decipher(self.get_password_from_db(self.getWebsite(),self.getUsername()))
            except:
                messagebox.showerror("DECIPHER ERROR",message="THE ENCRYPTING KEY IS INVALID!")
            else:
                messagebox.showinfo(title="Password",message=f"Your password is: {password} \n copied to clipboard!")   
                pyperclip.copy(password) 
        else:
            messagebox.showinfo(title="Password",message="Your user was not found.")  
    
    
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
    
        # WE MAKE IT THE TOP MOST WINDOW AND CENTER IT
        self.newWindow.attributes("-topmost",True)
        x = self.window.winfo_x() + self.window.winfo_width()//2 - self.newWindow.winfo_width()//2
        y = self.window.winfo_y() + self.window.winfo_height()//2 - self.newWindow.winfo_height()//2
        self.newWindow.geometry(f"+{x}+{y}")
        
        """
        MAKE THE LIST OF USERNAMES WEBSITES AND PASSWORDS
        """
        list_of_credentials = self.get_list_of_credentials()
        characters_of_biggest_string = self.get_listbox_width()
        # MAKE THE SCROLL BAR AND THE LIST BOX FOR THE PASSWORD LIST
        scrollbar = Scrollbar(self.newWindow)
        self.listbox = Listbox(self.newWindow,height=int(len(list_of_credentials)//1.5),width=characters_of_biggest_string)  
        
        # SCROLL BAR AND LISTBOX LINK
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command = self.listbox.yview) 

        # WE DUMP THE CREDENTIAL VALUES INTO THE LIST BOX
        self.fill_listbox(list_of_credentials)
            
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
            if (item_to_copy.find(dict["website"]) != -1 and item_to_copy.find(dict["username"]) != -1):
                item_to_copy = self.decipher(dict["password"])
                break 
        messagebox.showinfo(title="Password",message=f"Your password is: {item_to_copy} \n copied to clipboard!")  
        pyperclip.copy(item_to_copy)
        # WE BRING AGAIN THE ALL PASSWORDS WINDOW TO THE FRONT 
        self.newWindow.attributes('-topmost',1)
       
    """
    THIS FUNCTIONS SEARCHS IF A SPECIFIC USERNAME AND WEBSITE 
    IS ON THE DATA BASE, IF SO IT RETURNS TRUE
    IF NOT FOUND RETURNS FALSE
    """

    def credentials_on_database(self,website: str,username: str):
        data = self.collectData()
        for dict in data:
            if (dict["website"] == website and dict["username"] == username):
                return True
        return False
    
    def get_password_from_db(self,website: str,username: str):
        data = self.collectData()
        for dict in data:
            if (website == dict["website"] and username == dict["username"]):
                return dict["password"]
            
        return False
    
    """
    THIS FUNCTION RETURNS THE LIST OF THE STRINGS THAT GO INTO THE
    DISPLAY ALL PASSWORD LIST BOX
    FORMAT: website, username, password (******)
    """

    def get_list_of_credentials(self):
        data = self.collectData()
        list_of_credentials = []
        for dict in data:
            password_len = len(self.decipher(dict["password"]))
            list_of_password_letters = [] # FOR STORING THE * SIGNS OF THE CENSORED DATA
            for i in range(password_len):
                list_of_password_letters.append("*")

            censored_password = "".join(list_of_password_letters)   
            credentials = dict["website"] + ", " + dict["username"] + ", " + censored_password
            list_of_credentials.append(credentials)
        list_of_credentials = self.quicksort(list_of_credentials)
        return list_of_credentials
    
    """
    THIS RETURNS THE BIGGEST STRING CHARACHTER COUNT FROM THE LIST
    OF THE FORMATTED STRINGS THAT APPEAR ON THE DISPLAY ALL PASSWORDS WINDOW
    IT IS USED TO COMPUTE THE WIDTH OF THE LISTBOX IN ORDER TO ADJUST IT 
    TO THE LONGEST STRING
    """

    def get_listbox_width(self):
        # COMPUTE THE LONGEST STRING IN OUR CREDENTIALS TO DISPLAY
        list_of_credentials = self.get_list_of_credentials()
        characters_of_biggest_string = 0
        for string in list_of_credentials:
            if (len(string) > characters_of_biggest_string):
                    characters_of_biggest_string = len(string)

        return characters_of_biggest_string
    
    """
    THIS FUNCTION DUMPS THE FORMATED STRING VALUES OF THE CREDENTIALS
    INTO THE LISTBOX
    """

    def fill_listbox(self,credentials: list):
        # WE DUMP THE CREDENTIAL VALUES INTO THE LIST BOX
        for i in range(0,len(credentials)-1):
            self.listbox.insert(i, credentials[i]) 
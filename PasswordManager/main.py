"""
PASSWORD MANAGER WITH TKINTER 
autor: carlostr
date: 24.01.2024
"""
from tkinter import *
import csv 
from tkinter import messagebox
from password_generator import PasswordGenerator
import pyperclip

#VARIABLES 
password = None
website = None
username = None

#READ CVS FILE WITH PASSWORDS
try:
    file = open('D:/My files/Python OOP/Python 100 DAYS/PasswordManager/password.cvs', 'r')
except FileNotFoundError:
    file = open('D:/My files/Python OOP/Python 100 DAYS/PasswordManager/password.cvs', 'w', newline='')
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]
    file.close()
else:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]
    file.close()

window = Tk()

#Functions
pwo = PasswordGenerator()
pwo.minlen = 12
pwo.maxlen = 16
def genPassword():
    password = pwo.generate()
    set_text(password)

def set_text(text):
    enter_password_entry.delete(0,END)
    enter_password_entry.insert(0,text)
    return

def getPassword():
    entry = enter_password_entry.get()
    entry.strip()
    return entry

def getUsername():
    entry = mail_entry.get()
    entry.strip()
    return entry

def getWebsite():
    entry = website_entry.get()
    entry.strip()
    return entry

def savePassword():
    global password
    global username
    global website
    global data
    username = getUsername()
    password = getPassword()
    website = getWebsite()
    if (username == "" or website == "" or password == ""):
        messagebox.showinfo(title="PASSWORD MANAGER", message="MISSING VALUES!")
    else:
        dictionary = {}
        dictionary["username"] = username
        dictionary["password"] = password
        dictionary["website"] = website
        save = messagebox.askquestion(title="Save password?",message=f"Would you like to save this credentials? \n Username:{username} \n Website:{website} \n Password: {password}")
        if (save == 'yes'):
            data.append(dictionary)
            with open('D:/My files/Python OOP/Python 100 DAYS/PasswordManager/password.cvs', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['username', 'website','password'])
                for dictionary in data:
                    writer.writerow([dictionary['username'],dictionary['website'],dictionary['password']])
                file.close()
            messagebox.showinfo(title="PASSWORD MANAGER", message="PASSWORD SAVED!\n username:{} \n website:{} \n password:{}".format(username,website,password))
        elif (save == 'no'):
            pass

def searchPassword():
    global username
    global website
    global data
    username = getUsername()
    website = getWebsite()
    is_user_found = False
    for dict in data:
        if dict["username"] == username and dict["website"] == website:
            is_user_found = True
            password = dict["password"]
        else:
            pass
    if (is_user_found == True):
        messagebox.showinfo(title="Password",message=f"Your password is: {password} \n copied to clipboard!")   
        pyperclip.copy(password) 
    else:
        messagebox.showinfo(title="Password",message="Your user was not found.")  
    is_user_found = False
        
    

#CONFIG TITLE AND SIZE
window.title("Password Manager")
window.minsize(width=200,height=300)
window.config(padx=20,pady=20)
#CREATE CANVAS FOR IMG
canvas = Canvas(width=200,height=200,bg="#f7f5dd", highlightthickness=0)
lock_img = PhotoImage(file="D:/My files/Python OOP/Python 100 DAYS/PasswordManager/logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=2,column=2)
#WEBSITE AND MAIL/USERNAME LABELS
website_title_label = Label(window,text="Website: ")
mail_title_label = Label(window,text="Email/Username: ")
website_entry = Entry(window)
mail_entry = Entry(window)
website_title_label.grid(row=3,column=1)
mail_title_label.grid(row=4,column=1)
website_entry.grid(row=3,column=2)
mail_entry.grid(row=4,column=2)
#GENERATE BUTTON
generate_password_btn = Button(window,text="Generate Password",command=genPassword)
generate_password_btn.grid(row=5,column=3,padx=10,pady=10)
# ENTER PASSWORD LABEL AND BUTTON
enter_password_btn = Button(window,text="Save Password",command=savePassword)
enter_password_entry = Entry(window)
enter_password_lbl = Label(window,text="Password: ")
enter_password_btn.grid(row=6,column=2,padx=10,pady=10)
enter_password_entry.grid(row=5,column=2,padx=10,pady=10)
enter_password_lbl.grid(row=5,column=1,padx=10,pady=10)
#SEARCH PASSWORD BUTTON 
search_password_btn = Button(window,text="Search Password",command=searchPassword)
search_password_btn.grid(row=6, column=3)

window.mainloop()


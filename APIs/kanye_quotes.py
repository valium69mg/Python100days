import requests
from tkinter import *
from PIL import Image,ImageTk

URL = "https://api.kanye.rest"
INITIAL_MESSAGE = "Press Kanye for his quote of the day!"

"""
MANAGE THE REQUEST TO THE API
"""
def get_kanye_quote():
    res = requests.get(url=URL)
    data = res.json()
    quote = data['quote']
    return quote

def set_quote_text():
    quote = get_kanye_quote()
    """
    Format the quote in order to skip a line every 10 lines
    """
    words_list = quote.split()
    for i in range(1,len(words_list)):
        if (i % 8 == 0):
            word = words_list[i]
            new_word = word + "\n"
            words_list.insert(i,new_word)
    quote = " ".join(words_list)
    canvas.itemconfig(text,text=f"{quote}")
    

"""
TKINTER WINDOW CONFIGURATION
"""
root = Tk()
root.title("Kanye's random quotes")
root.minsize(width=720,height=480)
root.config(bg='#F5CCA0')

"""
TKINTER ROOT WINDOW LAYOUT
"""
canvas = Canvas(root,width=360,height=240,bg="#F5CCA0",highlightthickness=0)
rectangle = canvas.create_rectangle(0,0,360,200,fill="#6B240C")
x1,y1=180,230
x2,y2=160,200
x3,y3=200,200
triangle_points = [x1,y1,x2,y2,x3,y3]
triangle = canvas.create_polygon(triangle_points,fill="#6B240C")
text = canvas.create_text(180,100,text=INITIAL_MESSAGE,fill="#F5CCA0",font=('Arial',10,"bold"))
canvas.place(relx=0.5,rely=0.4,anchor=CENTER)
"""
KANTE IMAGE IMPORT AND MANAGING OF DIMENTIONS
"""
kanye_png_directory = "Python 100 DAYS/APIs/kanye.png"
my_img = Image.open(kanye_png_directory)
my_resized_img = my_img.resize((100,100))
kanye_img = ImageTk.PhotoImage(my_resized_img)
"""
BUTTON CONFIGURATION 
"""
kanye_button = Button(root,image=kanye_img,command=set_quote_text,borderwidth=0,bg="#F5CCA0",activebackground='#E48F45')
kanye_button.place(relx=0.5,rely=0.95,anchor=S)


root.mainloop()

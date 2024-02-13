from tkinter import *
import random

window = Tk()

"""
DICTIONARY WITH CARD INFORMATION
"""
cards = [{"English":"Chicken", "Portuguese":"A Galinha"},
         {"English":"Horse","Portuguese":"O Cavalo"},
         {"English":"Bull","Portuguese":"O Touro"},
         {"English":"Pork","Portuguese":"O Porco"},
         {"English":"Pork","Portuguese":"O Porco"},
         {"English":"Cow","Portuguese":"A Vaca"},
         {"English":"Duck","Portuguese":"O Pato"},
         {"English":"Rooster","Portuguese":"O Galo"},
         {"English":"Camel","Portuguese":"O Camelo"},
         {"English":"Sheep","Portuguese":"A Ovelha"}
         ]


"""
FUNCTIONS OF THE APP
"""
# DECLARATION OF VARIABLES
right_answers = 0
wrong_answers = 0
current_card = {}



def set_text(header_string,bottom_string):
    canvas.itemconfig(header_text,text=f"{header_string}")
    canvas.itemconfig(bottom_text,text=f"{bottom_string}")


def next_card():
    global cards,current_card,fliper_timer
    if (current_card == {}):
        window.after_cancel(fliper_timer)
        random_choice = random.choice(cards)
        current_card = random_choice
        english_word = current_card["English"]
        set_text("English",english_word)
        fliper_timer = window.after(3000,flip_card)
    else: 
        pass
    

def flip_card():
    global current_card
    portuguese_word = current_card["Portuguese"] 
    set_text("Portuguese",portuguese_word)
    current_card = {}

def score_up():
    global right_answers
    right_answers =+ 1
    next_card()

def score_down():
    global wrong_answers
    wrong_answers =+ 1
    next_card()

# TIMER DECLARATION   
fliper_timer = window.after(3000, func=flip_card)

"""
MAIN WINDOW CONFIGURATION

"""
window.title("Language Flash Cards")
window.minsize(width=720,height=480)
window.config(padx=20,pady=20)
window.config(bg='#EEEDEB')

"""
CREATE CANVAS FOR FLASH CARDS
"""
canvas = Canvas(window,width=680,height=300,bg='#E0CCBE', highlightthickness=0)
header_text = canvas.create_text(340,100,text="Header",fill="#3C3633",font=('Arial',35,"bold"))
bottom_text = canvas.create_text(340,200, text="Bottom",fill="#747264",font=('Arial',20))
canvas.grid(row=1,column=1,columnspan=5)

"""
CREATE BUTTONS FOR THE ANSWERS
"""
img_right = PhotoImage(file='Python 100 DAYS/Flash-cards/right.png')
img_wrong = PhotoImage(file='Python 100 DAYS/Flash-cards/wrong.png')
right_button = Button(window,image=img_right,borderwidth=0,command=score_up)
wrong_button = Button(window,image=img_wrong,borderwidth=0,command=score_down)
right_button.grid(row=2,column=2,padx=20,pady=20)
wrong_button.grid(row=2,column=4,padx=20,pady=20)

next_card()

window.mainloop()

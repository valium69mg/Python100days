import tkinter

window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500,height=300)

#LABELS
my_label = tkinter.Label(text="Im a label",font=("Arial",24,"bold"))
my_label.pack()

my_label["text"] = "NEW TEXT"
# my_label.config(text="New Text")


def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text

#Buttons
button = tkinter.Button(text="Click me!",command=button_clicked)
button.pack()

#Entry 
input = tkinter.Entry()
input.pack()



window.mainloop()

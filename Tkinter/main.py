import tkinter

window = tkinter.Tk()

# WINDOW
window.title("My firs GUI program")
window.minsize(width=500,height=300)

#LABEL
my_label = tkinter.Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.pack(side="left") #Puts the label in the center of the window

window.mainloop()

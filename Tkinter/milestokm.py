#MILES TO KM CONVERTER PROGRAM USING TKINTER 
from tkinter import *


def convert_mi_to_km():
    km = float(input_miles.get())*1.609344 
    calculated_km_label["text"] = km

#Config windows
window = Tk()
window.minsize(width=400,height=200)
window.title("MI TO KM CONVERTER")
window.config(bg="grey")

#Empty label (0,0)
empty_label = Label(text="Hello",font=("Arial",24,"bold"),fg="grey",bg="grey")
empty_label.grid(row=0,column=0)

#Entry 
input_miles = Entry()
input_miles.grid(row=1,column=1)

#Label miles
miles_label=Label(text="Miles",font=("Arial",16,"bold"),bg="grey")
miles_label.grid(row=1,column=2)

#Is equal to label 
equal_to_label=Label(text="equal to ",font=("Arial",16,"bold"),bg="grey")
equal_to_label.grid(row=3,column=0)

# calculated KM label 
calculated_km = "0"
calculated_km_label = Label(text=calculated_km,font=("Arial",16,"bold"),bg="grey")
calculated_km_label.grid(row=3,column=1)

#KM label
km_label = Label(text="km",font=("Arial",16,"bold"),bg="grey")
km_label.grid(row=3,column=2)

#Calculate button
button = Button(text="Calculate",command=convert_mi_to_km)
button.grid(row=4,column=1)

window.mainloop()
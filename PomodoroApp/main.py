
from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    header_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN *  60
    if (reps % 8 == 0):
        count_down(long_break_sec)
        header_label.config(text="Long Break",fg=RED)
    elif (reps % 2 == 0):
        count_down(short_break_sec)
        header_label.config(text="Short Break",fg=PINK)
    else:
        count_down(work_sec)
        header_label.config(text="Work",fg=GREEN)
        
        
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer
    count_minutes = floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text,text=f"{count_minutes}:{count_seconds}")
    if (count > 0):
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = floor(reps/2)
        for i in range(work_sessions):
            mark += "x"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100,pady=50,bg=YELLOW)

#LABELS
header_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"))
header_label.grid(row=1,column=2)

#CANVAS
canvas = Canvas(width=200,height=234,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="PomodoroApp/tomato.png")
canvas.create_image(100,117,image=tomato_img)
timer_text = canvas.create_text(100,117,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

#TIMER

#BUTTONS

check_mark = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
check_mark.grid(row=4,column=2)

start_button = Button(text="start",command=start_timer)
#command=function
reset_button = Button(text="reset",command=reset_timer)
start_button.grid(row=3,column=1)
reset_button.grid(row=3,column=3)


window.mainloop()

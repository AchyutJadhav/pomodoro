import math
from tkinter import *
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
def reset_timer ():
    window.after_cancel(timer)
    tik.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text="Timer")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps = reps + 1
    print(reps)

    if(reps%8 == 0):
        count_down(LONG_BREAK_MIN)
        timer_title.config(text="Long Break", fg=RED)
    elif (reps%2 == 0):
        count_down(SHORT_BREAK_MIN)
        timer_title.config(text="Short Break",fg=PINK)
    else:
        count_down(WORK_MIN)
        timer_title.config(text="Work Time", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if (count_sec < 10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if (count > 0):
        global timer
        timer = canvas.after(1000, count_down, count-1)      #1s = 1000
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        tik.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

#screen
window = Tk()
window.title("Pamodora")
window.config(padx=100, pady=50, bg=YELLOW)

#timer title
timer_title = Label(text="Timer", font=(FONT_NAME, 50, "bold"))
timer_title.config(fg=GREEN, bg=YELLOW)
timer_title.grid(row=1, column=2)

#canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=2, column=2)

#start button

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(row=3, column=1)

#reset_button

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(row=3, column=3)

#tik_button

tik = Label(font=(FONT_NAME, 10, ""), fg=GREEN)
tik.grid(row=4, column=2)



mainloop()
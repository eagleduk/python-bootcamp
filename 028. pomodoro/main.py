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
repos = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def count_reset():
    canvas.itemconfig(timer_text, text="00:00")

    timer_label["text"]="Timer"
    timer_label["fg"]=GREEN

    window.after_cancel(timer)

    check_label["text"] = ""

    global repos
    repos = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_event():
    global repos
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repos == 0 or repos == 2 or repos == 4 or repos == 6:
        timer_label["text"] = "Work"
        timer_label["fg"] = GREEN
        count_down(work_sec)
    elif repos == 1 or repos == 3 or repos == 5:
        timer_label["text"] = "Break"
        timer_label["fg"] = PINK
        count_down(short_break_sec)
    elif repos == 7:
        timer_label["text"] = "Break"
        timer_label["fg"] = RED
        count_down(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{str(count_min).zfill(2)}:{str(count_sec).zfill(2)}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global repos

        if repos == 0 or repos == 2 or repos == 4 or repos == 6:
            check_label["text"] += "✔"

        repos += 1
        start_event()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 38, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_event)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=count_reset)
reset_button.grid(row=2, column=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()
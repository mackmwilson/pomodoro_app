from tkinter import *
import time
from datetime import date

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = 0
timer = None


def current_time():
    current_day = date.today()
    text_time = time.strftime("%H:%M:%S")
    current_timer.config(text=f"{current_day}\n{text_time}")
    current_timer.after(1000, current_time)


def save_log():
    study_log = study_box.get()
    text_time = time.strftime("%H:%M:%S")
    current_day = date.today()

    with open('study_log.txt', 'a') as study_file:
        study_file.write(f"Date: {current_day} | Time: {text_time} | Studying: {study_log}\n")


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text='')
    timer_label.config(text='Timer')


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 1:
        countdown(WORK_MIN * 60)
        timer_label.config(text='Work', fg=GREEN)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60, )
        timer_label.config(text='Break', fg=PINK)


def countdown(count):
    global reps
    global checkmarks
    m, s = divmod(count, 60)
    canvas.itemconfig(timer_text, text=f"{m:02d}:{s:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks += 1
            num_checks = '✓' * checkmarks
            check_marks.config(text=f"{num_checks}")


# Setting up GUI in Tkinter
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='images\\tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=2)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))

current_timer = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'bold'))
current_timer.grid(column=0, row=0)

study_box = Entry(window, width=22)
study_box.insert(END, 'What are you studying?')
study_box.grid(column=1, row=0)

log_button = Button(text='Log Study', command=save_log, highlightthickness=0)
log_button.grid(column=2, row=0)

timer_label = Label(text='Timer', width=5, fg=GREEN, font=(FONT_NAME, 50, 'bold'), bg=YELLOW)
timer_label.grid(column=1, row=1)

start_button = Button(text='Start', command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=3)

reset_button = Button(text='Reset', command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=4)

current_time()
window.mainloop()

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
MIN_TO_SEC = 60
MAX_REPETITIONS = 8
reps = 0
timer = ""


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")


def start_timer():
    global reps
    reps += 1

    if reps % MAX_REPETITIONS == 0:
        timer_value = LONG_BREAK_MIN * MIN_TO_SEC
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        timer_value = SHORT_BREAK_MIN * MIN_TO_SEC
        title_label.config(text="Break", fg=PINK)
    else:
        timer_value = WORK_MIN * MIN_TO_SEC
        title_label.config(text="Work", fg=GREEN)

    count_down(timer_value)


def count_down(count: int):
    global reps
    global timer

    minutes = count // MIN_TO_SEC
    seconds = count % MIN_TO_SEC
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps < MAX_REPETITIONS:
            start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += "✓"
        checkmarks_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(window, text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'bold'))
title_label.grid(column=1, row=0)

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

button_start = Button(text='Start', bg='white', font=(FONT_NAME, 12, 'normal'), borderwidth=1, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text='Reset', bg='white', font=(FONT_NAME, 12, 'normal'), borderwidth=1, command=reset_timer)
button_reset.grid(column=2, row=2)

checkmarks_label = Label(window, text='', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, 'normal'))
checkmarks_label.grid(column=1, row=3)

window. mainloop()

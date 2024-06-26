from tkinter import *
import time
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None
#----------------------------Upload image------------------------------  #




# window.minsize(width=500, height=500)
# img = PhotoImage(file="tomato.png")
#
# #Create a label for the image
# my_label = Label(window, image=img)
# my_label.place(x=0, y=0, relwidth=1, relheight=1)
#
# # def start
# #
# # button1 = Button(text=Start, command=start)
# # button.place(x= -250, y = -230)
#
#
#
# # ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(counter_text, text="00:00")
    label.config(text="Timer")
    label2.config(text="")
    global reps
    reps = 0


# # ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        label.config(text="Work", font=("Courier", 45), bg="#808000", fg="#e2979c")
    elif reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break", font=("Courier", 45), bg="#808000", fg="#9bdeac")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break", font=("Courier", 45), bg="#808000", fg="#f7f5dd")



def stop():
    reset_timer()


# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(counter_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 30)
    else:
        start()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✓"
        label2.config(text=mark)





# def countdown_timer(minutes):
#     while minutes:
#         mins, secs = divmod(minutes, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         minutes -= 1
#     print("Time's up!")
#
# countdown_time = 30
# countdown_timer(countdown_time)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
#window.after(250, )
window.config(padx=100, pady=50, bg="#808000")
canvas = Canvas(width=200, height=224, bg="#808000", highlightbackground="#808000")
img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=img)
counter_text = canvas.create_text(103,128,text="00:00",fill="white", font=("Courier",35, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", font=("Courier", 45), bg="#808000")
label.grid(row = 0, column=1)



label2 = Label(font=("Courier", 20), bg="#808000", fg="#221123")
label2.grid(row = 3, column=1)


button_start = Button(text="Start", command=start)
button_start.configure(fg="#808000", bg="#808000", highlightbackground="#808000")
button_start.grid(row = 2, column =0)

button_stop = Button(text="Stop", command=stop)
button_stop.config(fg="#808000",bg="#808000", highlightbackground="#808000")
button_stop.grid(row = 2, column =2)


window.mainloop()


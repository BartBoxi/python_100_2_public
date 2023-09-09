from tkinter import *
import time
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

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
#
# # ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    count_down(5 * 60)

def stop():
    pass


# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(counter_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


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



label2 = Label(text="✓", font=("Courier", 20), bg="#808000")
label2.grid(row = 3, column=1)


button_start = Button(text="Start", command=start)
button_start.configure(fg="#808000", bg="#808000", highlightbackground="#808000")
button_start.grid(row = 2, column =0)

button_stop = Button(text="Stop", command=stop)
button_stop.config(fg="#808000",bg="#808000", highlightbackground="#808000")
button_stop.grid(row = 2, column =2)


window.mainloop()


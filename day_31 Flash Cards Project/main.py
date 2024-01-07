BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="/images/right.png")
wrong = PhotoImage(file="/images/wrong.png")

window = Tk()
window.title("Flashy")
window.config(width=1000, height=700, bg="#B1DDC6")
canvas = Canvas(width=800, height=526, bg="#B1DDC6")
canvas.create_image(800, 526, image=card_front)
canvas.grid(row=0, column=0)





window.mainloop()
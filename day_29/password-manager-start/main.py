from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=300)

canvas = Canvas(width=200, height=200, bg="#808000", highlightbackground="#808000")
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.pack()

window.mainloop()
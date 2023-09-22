from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=300)

canvas = Canvas(width=200, height=200, bg="#FFFFFF", highlightbackground="#FFFFFF")
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.pack()
window.config(padx=20, pady=20)

window.mainloop()
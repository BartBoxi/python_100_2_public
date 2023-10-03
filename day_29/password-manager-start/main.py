from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    print()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=300)

canvas = Canvas(width=200, height=200, bg="#FFFFFF", highlightbackground="#FFFFFF")
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0,column=1)
window.config(padx=20, pady=20)

#Website label

website_label = Label(text="Website",font=("Courier", 25))
website_label.grid(column = 0, row=2)

#Website entry

entery = Entry


email_label = Label(text="Email/Username",font=("Courier", 25))
email_label.grid(column=0, row=3)

password_label = Label(text="Password",font=("Courier", 25))
password_label.grid(column=0, row=4)



button_add = Button(text="Add", command = add)
button_add.grid(column=1, row = 5, columnspan=2)





window.mainloop()
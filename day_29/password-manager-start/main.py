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
website_label.grid(column = 0, row=1)

#Website entry

webstite_entry = Entry(width = 35 )
webstite_entry.grid(column=1, row=1, columnspan=2)


email_label = Label(text="Email/Username",font=("Courier", 25))
email_label.grid(column=0, row=3)

#email entry

email_entry = Entry(width = 35 )
email_entry.grid(column=1, row=3, columnspan=2)

password_label = Label(text="Password",font=("Courier", 25))
password_label.grid(column=0, row=4)

#password entry

pass_entry = Entry(width = 21)
pass_entry.grid(column=1, row=4)

def pass_generation():
    return 0

pass_button = Button(text="Generate Password", command=pass_generation, width=15)
pass_button.grid(column =2, row=4)


button_add = Button(text="Add", command = add, width=36)
button_add.grid(column=1, row = 5, columnspan=3)





window.mainloop()
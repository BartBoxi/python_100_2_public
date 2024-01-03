from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def pass_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for char in range(nr_letters)] + [random.choice(numbers) for num in range(nr_numbers)] + [random.choice(symbols) for num in range(nr_symbols)]

    random.shuffle(password_list)
    password = ""

    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)






# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
        }
    }

    if len(website) == 0 or len(password) ==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok =messagebox.askokcancel(title= "Title", message=f"These are the details that you entered \n Email:{email} \n "
                                                       f"Website:{website} \n "
                                                       f"Password: {password} \n"
                                                       f"Is it okay to save?")
        if is_ok:
            try:
                with open("saved_password.json", "r") as data_file:
                    #reading data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent= 4)
            else:
                #update the data with new data
                data.update(new_data)

                with open("saved_password.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                    # print(data)
            finally:
                website_entry.delete(0, END)
                pass_entry.delete(0, END)
#------------------------------Search Button---------------------------------#

def find_password(website, "saved_password.json"):
    with open("saved_password.json", "r") as data_file:
        json_data = json.load(data_file)
    return website in data_file.values()





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
#adjust the layout and the other widgets as needed to get the desired look
website_entry = Entry(width = 21)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


email_label = Label(text="Email/Username",font=("Courier", 25))
email_label.grid(column=0, row=3)

#email entry

email_entry = Entry(width = 35 )
email_entry.grid(column=1, row=3, columnspan=2)
email_entry.insert(0, "bartoszpudlo07@gmail.com")

password_label = Label(text="Password",font=("Courier", 25))
password_label.grid(column=0, row=4)

#password entry

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=4)



def pass_generation():
    pass_generator()

pass_button = Button(text="Generate Password", command=pass_generation, width=15)
pass_button.grid(column =2, row=4)

button_add = Button(text="Add", command = add, width=36)
button_add.grid(column=1, row = 5, columnspan=3)


#add a search button next to the website entry field
button_search = Button(text="Search", command = find_password, width=15)
button_search.grid(column = 2, row = 1)




window.mainloop()
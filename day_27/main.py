from tkinter import *

# label = Label("This is the first label")
# label.grid(row =1, column = 1)


window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

label = Label(text="This is old text")
label.grid(row =0, column = 0)


def action():
    print("Do something")

# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()


button = Button(text="Click me", command=action())
button.grid(row= 1, column = 1)

button_2 = Button(text="Click me new", command = action())
button_2.grid(row = 0, column = 2)

# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()

entry = Entry(width=10)
entry.insert(END, string="Some text here bro")
print(entry.get())
entry.grid(row = 2, column=3)


window.mainloop()

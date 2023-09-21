from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width=350, height=250)

label2 = Label(text="Miles")
label2.grid(row =0, column = 3)

label3 = Label(text="KM")
label3.grid(row =1, column = 3)

label = Label(text="")
label.grid(row =0, column =0)
#label.config(padx=10, pady=10)

label1 = Label(text="is equal to")
label1.grid(row =1, column = 1)


entry = Entry(width=10)
entry.grid(row = 0, column=2)



def action():
    miles = float(entry.get())
    km = miles * 1.609
    label4.config(text=km)


button = Button(text="Calculate", command=action)
button.grid(row=2, column=2)

label4 = Label(text="0")
label4.grid(column=2, row=1)


window.mainloop()

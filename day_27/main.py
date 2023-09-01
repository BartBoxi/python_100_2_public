from tkinter import *

window = Tk()



window.title("My GUI program ")
window.minsize(width= 500, height=500)



my_label = Label(text="Im a label", font=("Arial", 24, "italic"))
my_label.pack()

#Button

def button_clicked():
    output = input.get()

    print("I got clicked")
    my_label.config(text=output)


button = Button(text="Click me", command = button_clicked)
button.pack()


#Entry

input = Entry("Text to start with")
input.pack()




window.mainloop()
import tkinter

window = tkinter.Tk()



window.title("My GUI program ")
window.minsize(width= 500, height=500)

my_label = tkinter.Label(text="Im a label", font=("Arial", 24, "italic"))
my_label.pack()






window.mainloop()
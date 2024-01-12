BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text ="French")
    canvas.itemconfig(card_word, text = current_card["French"])

def next_french_word():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card["French"])
    #if next_card()

# TODO: add functionaly when from next french card im going to next card to show first the translation of uknown word
#---------------------------------DATA---------------------------------#



#--------------------------------UI------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="#B1DDC6")
canvas = Canvas(width=800, height=526)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image=card_front)
card_title = canvas.create_text(400, 150, text="title", fill="black", font=("Ariel",40, "italic"))
card_word = canvas.create_text(400, 223, text="word",fill="black", font=("Ariel",60, "bold"))
canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


right = PhotoImage(file="/Users/bartoszpudlo/PycharmProjects/python_100_2/day_31 Flash Cards Project/images/right.png")
wrong = PhotoImage(file="/Users/bartoszpudlo/PycharmProjects/python_100_2/day_31 Flash Cards Project/images/wrong.png")

unknown_button = Button(image=wrong, highlightthickness=0, command = next_card)
unknown_button.grid(row=1, column=0)

good_button = Button(image=right, highlightthickness=0, command= next_french_word)
good_button.grid(row=1, column=1)

next_card()

window.mainloop()
BACKGROUND_COLOR = "#B1DDC6"
import csv
import os
from tkinter import *
import pandas as pd
import random

data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')

current_card = {}




def next_card():
    global current_card
    global flip_timer
    words_to_learn =  []
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text ="French", fill="black")
    canvas.itemconfig(card_word, text = current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
    words_to_learn.update(current_card)
    df = pd.DataFrame(words_to_learn)

    if not os.path.exists("words_to_learn.csv"):
        df.to_csv("words_to_learn.csv", index=False)
    else:
        df=pd.read_csv("words_to_learn.csv")
        new_df=pd.DataFrame(current_card)
        df = df.append(new_df, ignore_index=True)
        df.to_csv("words_to_learn.csv", index=False)







def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def good_word():
    global flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
    to_learn.remove(current_card)

# TODO: add functionaly when from next french card im going to next card to show first the translation of uknown word
#---------------------------------DATA---------------------------------#



#--------------------------------UI------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="#B1DDC6")


flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400,263, image=card_front)
card_title = canvas.create_text(400, 150, text="title", fill="black", font=("Ariel",40, "italic"))
card_word = canvas.create_text(400, 223, text="word",fill="black", font=("Ariel",60, "bold"))
canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


right = PhotoImage(file="/Users/bartoszpudlo/PycharmProjects/python_100_2/day_31 Flash Cards Project/images/right.png")
wrong = PhotoImage(file="/Users/bartoszpudlo/PycharmProjects/python_100_2/day_31 Flash Cards Project/images/wrong.png")

unknown_button = Button(image=wrong, highlightthickness=0, command = next_card)
unknown_button.grid(row=1, column=0)

good_button = Button(image=right, highlightthickness=0, command= good_word)
good_button.grid(row=1, column=1)

window.mainloop()
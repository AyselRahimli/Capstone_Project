from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}
flip_timer = None

try:
    data = pandas.read_csv("data/french_words.csv")
except:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(cart_1,image=card_front)
    flip_timer = window.after(3000,func=flip)
def flip():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(cart_1,image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/WordsToLearn.csv")
    next_card()

window = Tk()
window.title("Flashcard Program")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
cart_1 = canvas.create_image(400, 270, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()

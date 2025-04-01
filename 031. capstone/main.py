import tkinter

from seaborn.external.husl import rgb_to_hex

screen = tkinter.Tk()
screen.config(padx=50, pady=50, width=800, height=528, background="#b1ddc6")

canvas = tkinter.Canvas(width=800, height=526, background="#b1ddc6", highlightthickness=0)
font_image = tkinter.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=font_image)
title_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="Title")
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="Word")
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, background="#b1ddc6")
wrong_button.grid(row=1, column=0)

right_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, background="#b1ddc6")
right_button.grid(row=1, column=1)


screen.mainloop()
from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, width=340, pady=20, padx=20)

        self.score = Label()
        self.score.config(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question = self.canvas.create_text(150, 125, text="Amazon...", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

        true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Canvas(width=100, height=97, highlightthickness=0)
        self.true_button.create_image(50, 49, image=true_button_image)
        self.true_button.grid(row=2, column=0, pady=20, padx=20)

        false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Canvas(width=100, height=97, highlightthickness=0)
        self.false_button.create_image(50, 49, image=false_button_image)
        self.false_button.grid(row=2, column=1, pady=20, padx=20)

        self.window.mainloop()
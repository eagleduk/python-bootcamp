from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, width=340, pady=20, padx=20)

        self.score = 0
        self.score_label = Label()
        self.score_label.config(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

        true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_button_image, command=self.answer_true)
        self.true_button.grid(row=2, column=0, pady=20, padx=20)

        false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_button_image, command=self.answer_false)
        self.false_button.grid(row=2, column=1, pady=20, padx=20)

        self.next_question()

        self.window.mainloop()

    def next_question(self, results=False):
        if results:
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        question_str = self.quiz.next_question()
        self.canvas.config(bg="white")
        self.canvas.itemconfigure(self.question, text=question_str)

    def answer_true(self):
        results = self.quiz.check_answer("true")
        self.answer_feedback(results)

    def answer_false(self):
        results = self.quiz.check_answer("false")
        self.answer_feedback(results)

    def answer_feedback(self, results: bool):

        self.window.after(1000, self.next_question, results)

        if results:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

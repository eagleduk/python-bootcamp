from turtle import Turtle


class Score(Turtle):


    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setx(x)
        self.sety(265)
        self.score = 0
        self.set_score(self.score)

    def set_score(self, s):
        self.score += s

        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 22, 'normal'))

        return self.score

    def winner(self, text):
        self.sety(0)
        self.setx(0)
        self.write(f"Winner: {text}", align="center", font=('Arial', 22, 'normal'))

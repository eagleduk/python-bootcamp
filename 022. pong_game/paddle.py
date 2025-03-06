from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x = 350, y = 0)
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len=1)
        self.color("white")

        # self.hideturtle()

    def up(self):
        if self.ycor() <= 240:
            self.sety(self.ycor() + 20)

    def down(self):
        if -220 <= self.ycor():
            self.sety(self.ycor() - 20)
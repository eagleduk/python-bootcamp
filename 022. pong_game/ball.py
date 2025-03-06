from turtle import Turtle

class Ball(Turtle):

    _x = 10
    _y = -10

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed(0)

    def run(self):
        x = self.xcor() + self._x
        y = self.ycor() + self._y

        if 280 <= y:
            self._y = -10
        elif y <= -280:
            self._y = 10

        self.goto(x, y)
from turtle import Turtle

class Ball(Turtle):

    _x = -10
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

        self.goto(x, y)

    def bounce_x(self):
        self._x *= -1

    def bounce_y(self):
        self._y *= -1

    def reset(self):
        self.home()
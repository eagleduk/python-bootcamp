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

    def run(self, rp, lp):
        x = self.xcor() + self._x
        y = self.ycor() + self._y

        # bounce top, bottom wall
        if 280 <= y or y <= -280:
            self._y *= -1

        # bounce paddle
        if self.distance(rp) < 40 and 320 < self.xcor():
            self._x = -10
        elif self.distance(lp) < 40 and self.xcor() < -320:
            self._x = 10

        self.goto(x, y)

    def reset(self):
        self.home()
from turtle import Turtle
import random

class Car(Turtle):

    _is_move = False

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setx(260)

        y = random.randint(-12, 12) * 20
        self.sety(y)

    def move(self):
        # print(self._is_move)
        # print (not self._is_move)
        # if not self._is_move:
        self.forward(20)
        self._is_move = True

    def gone(self):
        self.clear()
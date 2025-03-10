from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]
SPEED_DISTANCE = 8

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setx(260)

        y = random.randint(-12, 12) * 20
        self.sety(y)

    def move(self, level):
        self.forward(SPEED_DISTANCE * level)

    def gone(self):
        self.clear()

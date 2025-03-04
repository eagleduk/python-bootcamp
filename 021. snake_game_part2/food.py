import turtle
import random


class Food:

    food = None
    x = 0
    y = 0

    def __init__(self):

        self.food = turtle.Turtle(shape="circle")
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food.color("yellow")
        self.food.penup()

    def render(self):

        self.x = random.randint(-280, 290) - 10
        self.y = random.randint(-280, 290) - 10

        self.food.goto(self.x, self.y)

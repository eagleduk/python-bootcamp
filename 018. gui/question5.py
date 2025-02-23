import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)

idx = 5
counts = (360 / idx)

the_turtle = Turtle()
the_turtle.speed("fastest")

for _ in range(int(counts)):
    color = random_color()
    the_turtle.color(color)
    the_turtle.circle(100)
    the_turtle.right(idx)

Screen().exitonclick()

import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)


the_turtle = Turtle()
the_turtle.shape("turtle")
the_turtle.pensize(10)
the_turtle.speed("fastest")

for _ in range(200):
    idx = random.randrange(0,4)
    color = random_color()
    the_turtle.color(color)
    angle = 90 * idx
    the_turtle.right(angle)
    the_turtle.forward(30)

Screen().exitonclick()

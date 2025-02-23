from turtle import Turtle, Screen
import random

the_turtle = Turtle()
the_turtle.shape("turtle")
the_turtle.pensize(10)

colors = ["green yellow", "magenta", "dark green", "blue", "maroon", "black", "dark cyan", "royal blue", "saddle brown", "gold", "medium violet red", "hot pink"]

for _ in range(15):
    idx = random.randrange(1,5)
    the_turtle.color(random.choice(colors))
    angle = 90 * idx
    print(angle)
    the_turtle.right(angle)
    the_turtle.forward(30)



Screen().exitonclick()
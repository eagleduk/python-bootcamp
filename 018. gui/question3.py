from turtle import Turtle, Screen

the_turtle = Turtle()
the_turtle.shape("turtle")

colors = ["green yellow", "magenta", "dark green", "blue", "maroon", "black", "dark cyan"]

for i in range(4, 11):
    angle = 360 / i
    the_turtle.color(colors[i-4])
    for n in range(i):
        the_turtle.forward(100)
        the_turtle.right(angle)




Screen().exitonclick()
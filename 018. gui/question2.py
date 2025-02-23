from turtle import Turtle, Screen

the_turtle = Turtle()
the_turtle.shape("turtle")

for i in range(20):
    if i % 2 == 0:
        the_turtle.pendown()
    else:
        the_turtle.penup()
    the_turtle.forward(10)




Screen().exitonclick()
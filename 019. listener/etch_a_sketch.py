from turtle import Turtle, Screen

def move_forward():
    t.forward(10)

def move_backward():
    t.forward(-10)

def turn_left():
    t.setheading(t.heading() + 10)

def turn_right():
    t.setheading(t.heading() - 10)

def reset():
    t.reset()

t = Turtle()

screen = Screen()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)

screen.exitonclick()
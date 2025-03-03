from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

body_length = 3

snake = []

turn = 0

for i in range(body_length):
    b = Turtle(shape="square")
    b.penup()
    b.color("white")
    b.setx(-i * 19)
    snake.append(b)

while turn < 5:
    turn = turn + 1
    for i in range(body_length):
        b = snake[i]
        b.forward(20)





screen.exitonclick()
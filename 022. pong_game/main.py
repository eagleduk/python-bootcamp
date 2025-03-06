from turtle import Screen, Turtle
import paddle

screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("PONG")
screen.bgcolor("black")
screen.listen()


right_paddle = paddle.Paddle()

screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)

screen.exitonclick()
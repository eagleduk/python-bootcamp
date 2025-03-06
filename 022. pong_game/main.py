from turtle import Screen
import paddle
import ball
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("PONG")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)


right_paddle = paddle.Paddle((350, 0))
left_paddle = paddle.Paddle((-350, 0))

ball = ball.Ball()

screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)


on_game = True

while True:
    screen.update()
    time.sleep(0.1)

    ball.run()


screen.exitonclick()
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("PONG")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
right_score = Score(200)
left_score = Score(-200)

screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)
screen.onkey(key="r", fun=ball.reset)

on_game = True

while on_game:
    screen.update()
    time.sleep(0.1)

    s = ball.run(right_paddle, left_paddle)

    l = left_score.set_score(s[0])
    r = right_score.set_score(s[1])

    if l == 3 or r == 3:
        on_game = False
        if l == 3:
            left_score.winner("LEFT")
        else:
            right_score.winner("RIGHT")

screen.exitonclick()
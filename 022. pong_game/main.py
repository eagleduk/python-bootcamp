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
sleep = 0.1

while on_game:
    screen.update()
    time.sleep(sleep)

    s = ball.run(right_paddle, left_paddle)

    # Score Game
    if 360 < ball.xcor() or ball.xcor() < -360:
        if 360 < ball.xcor():
            left_score.set_score(1)
        else:
            right_score.set_score(1)
        ball.bounce_x()
        ball.home()
        sleep = 0.1

    # bounce top, bottom wall
    if 280 <= ball.ycor() or ball.ycor() <= -280:
        ball.bounce_y()

    # bounce paddle
    if ball.distance(right_paddle) < 40 and 320 < ball.xcor():
        ball.bounce_x()
        sleep *= 0.9
    elif ball.distance(left_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()
        sleep *= 0.9


screen.exitonclick()
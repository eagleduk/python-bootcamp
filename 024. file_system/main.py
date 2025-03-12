from turtle import Screen
import time
import snake
import food
import text

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

score = 0

segments = snake.SnakeSegment()
f = food.Food()
f.render()
t = text.Text()
t.score_board()
is_game_on = True

def re_game():
    segments.re_game()
    t.re_game()

screen.onkey(key="Up", fun=segments.up)
screen.onkey(key="Down", fun=segments.down)
screen.onkey(key="Left", fun=segments.left)
screen.onkey(key="Right", fun=segments.right)
screen.onkey(key="r", fun=re_game)
screen.onkey(key="q", fun=screen.bye)

while is_game_on:
    segments.move()
    time.sleep(0.1)
    screen.update()

    head_segment = segments.segments[0]
    body_segment = segments.segments[2:]

    x = head_segment.xcor()
    y = head_segment.ycor()

    if x < -280 or 280 < x or y < -280 or 280 < y:
        t.game_over()
        segments.stop()

    if head_segment.distance(f.food) < 20:
        f.render()
        t.increase()
        segments.append()

    for tails in body_segment:
        if head_segment.distance(tails) < 20:
            t.game_over()
            segments.stop()

screen.exitonclick()

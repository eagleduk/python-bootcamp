from turtle import Screen, Turtle
import time
import snake
import food
import text


def up():
    print("up")


def down():
    print("down")


def left():
    print("left")


def right():
    print("right")


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

body_length = 13

segments = []

score = 0

for i in range(body_length):
    seg = snake.SnakeSegment()
    seg.set_position(-i * 20, 0)

    segments.append(seg)


f = food.Food()
f.render()
is_game_on = True
t = text.Text()
t.score_board()

while is_game_on:

    time.sleep(0.1)
    screen.update()

    forward_position = None
    positions = []

    for segment in segments:

        t_position = segment.get_position()

        if forward_position is None:
            segment.forward()
            screen.onkey(key="Up", fun=segment.up)
            screen.onkey(key="Down", fun=segment.down)
            screen.onkey(key="Left", fun=segment.left)
            screen.onkey(key="Right", fun=segment.right)

            p = segment.get_position()

            if p[0] < -300 or 300 < p[0] or p[1] < -300 or 300 < p[1]:
                t.game_over()
                is_game_on = False

            for tails in segments[1:]:
                if segment.distance(tails.get_position()) < 20:
                    t.game_over()
                    is_game_on = False

            if segment.distance(f.food) < 20:
                f.render()
                t.increse_score()
                segments.append(snake.SnakeSegment())

        else:
            segment.set_position(forward_position[0], forward_position[1])

        forward_position = t_position

screen.exitonclick()

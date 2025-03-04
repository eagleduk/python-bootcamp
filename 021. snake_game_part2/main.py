from turtle import Screen, Turtle
import time
import snake
import food


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

body_length = 3

segments = []

score = 0

for i in range(body_length):
    seg = snake.SnakeSegment()
    seg.set_position(-i * 20, 0)

    segments.append(seg)


f = food.Food()
f.render()
is_game_on = True
t = Turtle()
t.color("white")
t.penup()
t.hideturtle()
t.sety(280)

while is_game_on:

    t.write(f"score: {score}", False, align="center")

    time.sleep(0.3)
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
                t.sety(0)
                t.write(f"Game Over", False, align="center")
                is_game_on = False

            if segment.distance(f.food) < 20:
                f.render()
                t.clear()
                score = score + 1
                segments.append(snake.SnakeSegment())

        else:
            segment.set_position(forward_position[0], forward_position[1])

        forward_position = t_position

screen.exitonclick()

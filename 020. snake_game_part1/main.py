from turtle import Screen, Turtle
import time
import snake

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

turn = 0

for i in range(body_length):
    seg = snake.SnakeSegment()
    seg.setposition(-i * 20, 0)

    segments.append(seg)

while turn < 100:
    time.sleep(0.3)
    screen.update()
    turn = turn + 1

    forward_position = None
    positions = []

    for segment in segments:

        t_position = segment.getposition()

        if forward_position is None:
            segment.forward()
            screen.onkey(key="Up", fun=segment.up)
            screen.onkey(key="Down", fun=segment.down)
            screen.onkey(key="Left", fun=segment.left)
            screen.onkey(key="Right", fun=segment.right)
        else:
            segment.setposition(forward_position[0], forward_position[1])

        forward_position = t_position



screen.exitonclick()
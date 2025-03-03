from turtle import Screen, Turtle
import time
import snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

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

    for segment in segments:
        segment.forward()




screen.exitonclick()
import turtle

BODY_LENGTH = 3

class SnakeSegment:

    segments = []

    def __init__(self):
        self.forward = 20
        for i in range(BODY_LENGTH):
            seg = turtle.Turtle(shape="square")
            seg.penup()
            seg.color("white")
            seg.goto(-i * 20, 0)

            self.segments.append(seg)

    def move(self):

        x = self.segments[0].xcor()
        y = self.segments[0].ycor()

        self.segments[0].forward(self.forward)

        for segment in self.segments[1:]:
            nx = segment.xcor()
            ny = segment.ycor()
            segment.goto(x, y)
            x = nx
            y = ny

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def append(self):
        seg = turtle.Turtle(shape="square")
        seg.penup()
        seg.color("white")

        self.segments.append(seg)

    def stop(self):
        self.forward = 0

    def re_game(self):
        self.forward = 20

        for segment in self.segments:
            segment.goto(1000, 1000)

        self.segments = []

        for i in range(BODY_LENGTH):
            seg = turtle.Turtle(shape="square")
            seg.penup()
            seg.color("white")
            seg.goto(-i * 20, 0)

            self.segments.append(seg)


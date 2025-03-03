import turtle


class SnakeSegment:
    _segment = None

    def __init__(self):
        self._segment = turtle.Turtle(shape="square")
        self._segment.penup()
        self._segment.color("white")

    def setposition(self, x, y):
        self._segment.goto(x, y)

    def forward(self):
        self._segment.forward(20)


    def getposition(self):
        return (self._segment.xcor(), self._segment.ycor())

    def up(self):
        if self._segment.heading() != 270:
            self._segment.setheading(90)

    def down(self):
        if self._segment.heading() != 90:
            self._segment.setheading(270)

    def left(self):
        if self._segment.heading() != 0:
            self._segment.setheading(180)

    def right(self):
        if self._segment.heading() != 180:
            self._segment.setheading(0)
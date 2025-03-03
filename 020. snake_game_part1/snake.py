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
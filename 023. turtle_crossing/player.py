from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.sety(-284)

    def up(self):
        self.forward(20)

    def goal(self):
        return self.ycor() > 280
        # 280

    def re_game(self):
        self.sety(-284)
from turtle import Turtle

class TextBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setx(-240)
        self.sety(245)

    def write_level(self, level):
        self.clear()
        self.write(f"Level: {level}", align="center", font=('Arial', 22, 'normal'))

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=('Arial', 22, 'normal'))

c = [1,2,3,4]

print(len(c))

c.pop()

print(len(c))
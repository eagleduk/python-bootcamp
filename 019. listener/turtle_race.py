from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=300)
game_over = False
choice_color = screen.textinput(title="bet", prompt="choice color")

colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]

turtles = []
h = -120

for i in range(len(colors)):
    color = colors[i]
    t = Turtle(shape="turtle")
    t.fillcolor(color)
    t.penup()
    t.goto(x=-230, y=h + (i*40))
    turtles.append(t)

winner_turtle = None

while game_over is False:
    for t in turtles:
        random_move = random.randint(0, 10)
        now_x = t.xcor()
        next_x = now_x + random_move
        t.setx(next_x)

        if next_x >= 250:
            game_over = True
            winner_turtle = t.fillcolor() if winner_turtle is None else winner_turtle

if winner_turtle == choice_color:
    print(f'Winner is : {winner_turtle}. You Win!')
else:
    print(f'Winner is : {winner_turtle}. You Lose..')

screen.exitonclick()
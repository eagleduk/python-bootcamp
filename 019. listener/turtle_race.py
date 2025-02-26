from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=300)

colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]

turtles = []
h = -120
# -120 -80 -40 -0 40 80 120
for i in range(len(colors)):
    color = colors[i]
    t.fillcolor(color)
    t.penup()
    t.goto(x=-230, y=h + (i*40))
    turtles.append(t)

screen.exitonclick()
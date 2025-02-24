# import colorgram
import turtle as t
import random

# colors = colorgram.extract("image", -1)
#
# rgbs = []
#
# for i in range(len(colors)):
#     c = colors[i].rgb
#     rgbs.append((c.r, c.g, c.b))
#
# print(rgbs)

rgb_colors = [(131, 164, 204), (228, 149, 99), (30, 44, 64), (238, 245, 242), (245, 234, 238), (166, 58, 48), (202, 135, 147), (237, 212, 85), (41, 101, 150), (135, 183, 161), (150, 62, 71), (52, 42, 45), (159, 33, 31), (219, 82, 73), (238, 165, 155), (58, 117, 99), (60, 49, 45), (173, 29, 31), (231, 163, 168), (35, 61, 56), (15, 96, 71), (33, 60, 107), (170, 188, 222), (188, 101, 111), (104, 126, 161), (14, 85, 109), (174, 200, 188), (33, 151, 211), (65, 66, 57), (100, 141, 129), (155, 202, 223)]

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

tim.teleport(-300, 300)

for _ in range(10):
    tim.setx(-300)
    tim.sety(tim.ycor() - 50)
    for _ in range(10):
        color = random.choice(rgb_colors)
        tim.setx(tim.xcor() + 50)
        tim.color(color)
        tim.dot(20, color)

t.Screen().exitonclick()

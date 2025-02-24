import colorgram
import turtle as t
import random

'''
colors = colorgram.extract("image", -1)

rgbs = []

for i in range(len(colors)):
    c = colors[i].rgb
    rgbs.append((c.r, c.g, c.b))

print(rgbs)
'''
rgbs = [(131, 164, 204), (228, 149, 99), (30, 44, 64), (238, 245, 242), (245, 234, 238), (166, 58, 48), (202, 135, 147), (237, 212, 85), (41, 101, 150), (135, 183, 161), (150, 62, 71), (52, 42, 45), (159, 33, 31), (219, 82, 73), (238, 165, 155), (58, 117, 99), (60, 49, 45), (173, 29, 31), (231, 163, 168), (35, 61, 56), (15, 96, 71), (33, 60, 107), (170, 188, 222), (188, 101, 111), (104, 126, 161), (14, 85, 109), (174, 200, 188), (33, 151, 211), (65, 66, 57), (100, 141, 129), (155, 202, 223)]

t.colormode(255)
the_turtle = t.Turtle()

the_turtle.teleport(-200, 200)

for x in range(10):
    the_turtle.penup()
    the_turtle.setx(-200)
    the_turtle.sety(the_turtle.ycor() - 50)
    for y in range(10):
        color = random.choice(rgbs)
        the_turtle.setx(the_turtle.xcor() + 50)
        the_turtle.speed("fastest")
        the_turtle.color(color)
        the_turtle.pendown()
        the_turtle.dot(20, color)
        the_turtle.penup()



t.Screen().exitonclick()
# from turtle import Turtle, Screen
#
# turtle_a = Turtle()
# turtle_a.shape("turtle")
# turtle_a.color("coral")
# turtle_a.forward(100)
#
# screen_a = Screen()
# screen_a.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
])
table.align = "l"

print(table)
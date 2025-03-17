import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("./blank_states_img.gif")

states_list = pandas.read_csv("./50_states.csv")
states_arr = states_list["state"].to_list()

while len(states_arr) > 0:
    input_state = screen.textinput(f"{50 - len(states_arr)}/50 States Correct", "Input States")

    if input_state is None:
        break

    correct_state = states_list[states_list.state == input_state]

    if not correct_state.empty:
        x = correct_state.x.item()
        y = correct_state.y.item()
        state = correct_state["state"].item()
        text_turtle = Turtle()
        text_turtle.hideturtle()
        text_turtle.penup()
        text_turtle.goto(x, y)
        text_turtle.write(state)

        states_arr.remove(state)

screen.exitonclick()
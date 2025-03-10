import random
from turtle import Screen
import time

from player import Player
from car import Car
from textBoard import TextBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

player = Player()
textBoard = TextBoard()
cars = []

screen.onkey(key="Up", fun=player.up)

level = 1
is_game_over = False

textBoard.write_level(level)

while not is_game_over:
    time.sleep(0.1)
    screen.update()

    if random.randint(0, 10) < level:
        cars.append(Car())

    for car in cars:
        car.move(level)

        if player.distance(car) < 20.0 :
            print("GAME OVER")
            textBoard.game_over()
            is_game_over = True

        if car.ycor() < -280:
            car.gone()

    if player.goal():
        print("Goal")
        level += 1

        player.re_game()
        textBoard.write_level(level)


screen.exitonclick()
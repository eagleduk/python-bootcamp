from turtle import Screen
import time

from player import Player
from car import Car
from textBoard import TextBoard

screen = Screen()
screen.setup(width=600, height=600)

def game_start(s, l):
    s.title("Turtle Crossing")
    s.tracer(0)
    s.listen()
    p = Player()
    t = TextBoard()

    s.onkey(key="Up", fun=p.up)

    t.write_level(l)

    return p, t, []

level = 1
is_game_over = False

player, textBoard, cars = game_start(screen, level)

while not is_game_over:
    time.sleep(0.1)
    screen.update()

    print(len(cars))

    if len(cars) < 10:
        cars.append(Car())

    for index in range(len(cars)):
        car = cars[index]
        car.move()

        if player.distance(car) < 10:
            print("GAME OVER")
            textBoard.game_over()
            # is_game_over = True

        if car.ycor() < -280:
            car.gone()
            cars.pop()

    if player.goal():
        print("Goal")
        level += 1

        screen.reset()
        player, textBoard, cars = game_start(screen, level)

        # screen.update()
        # cars.clear()

screen.exitonclick()
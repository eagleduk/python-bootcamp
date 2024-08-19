import os
from art import logo, vs
from game_data import data
from random import randint


def choise_data(game_data):
    return game_data.pop(randint(0, len(game_data)-1))


def format_str(row):
    return f"{row["name"]}, a {row["description"]}, from {row["country"]}"


def game():
    os.system('cls')
    print(logo)

    game_data = data
    score = 0

    a = choise_data(game_data)
    b = choise_data(game_data)

    while len(game_data) > 0:
        print(f"Compare A: {format_str(a)}")
        print(vs)
        print(f"Compare B: {format_str(b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if (guess == "a" and a["follower_count"] > b["follower_count"]) or (guess == "b" and a["follower_count"] < b["follower_count"]):
            os.system('cls')
            score += 1
            print(f"You're right! Current score: {score}.")
            if guess == "b":
                a = b
            b = choise_data(game_data)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return

    if len(game_data) == 0:
        print(f"All Clear!! your Score: {score}")


game()

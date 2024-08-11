from m003.art import logo
import os

bid = {}

print(logo)
print("Welcome to the secret auction program.")

while(True):
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))

    bid[name] = price

    answer = input("Are there any other bidders? Type 'yes' or 'no'.")

    if answer == 'no':

        n = ""
        max = 0

        for name in bid:
            p = bid[name]
            if max < p:
                n = name
                max = p

        print(f"The winner is {n} with a bid of ${max}")

        break





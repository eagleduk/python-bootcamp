import random

input_name_string = input()

name_list = input_name_string.split(",")

random_integer = random.randint(0, len(name_list)-1)

print(f"{name_list[random_integer]} is going to buy the meal today!")
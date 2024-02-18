print("Thank you for choosing Python Pizza Deliveries!")
pizza = 0

size = input()
if size == "S":
    pizza = 15
elif size == "M":
    pizza = 20
else:
    pizza = 25

add_pepperoni = input()
if add_pepperoni == "Y":
    if size == "S":
        pizza += 2
    else:
        pizza += 3

extra_cheese = input()
if extra_cheese == "Y":
    pizza += 1

print(f"Your final bill is: ${pizza}.")
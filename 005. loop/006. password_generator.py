#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

counts = [nr_letters, nr_numbers, nr_symbols]
chars = [letters, numbers, symbols]

password = ""

for index in range(0, nr_letters+nr_numbers+nr_symbols):
    type_index = random.randint(0, len(chars) - 1)
    counts[type_index] = counts[type_index] - 1
    type_word = chars[type_index]
    password = password + random.choice(type_word)

    if counts[type_index] == 0 and len(chars) > 0:
        c = []
        l = []
        for i in range(0, len(chars)):
            if i != type_index:
                c.append(counts[i])
                l.append(chars[i])
        counts = c
        chars = l

print(password)


###############################
###############################
###############################

password_list = []

for i in range(0, nr_letters):
    password_list += random.choice(letters)

for i in range(0, nr_numbers):
    password_list += random.choice(numbers)

for i in range(0, nr_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)

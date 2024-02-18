print("The Love Calculator is calculating your score...")
name1 = input()
name2 = input()
score1 = 0
score2 = 0

name = name1 + name2
name = name.lower()

score1 = name.count("t") + name.count("r") + name.count("u") + name.count("e")
score2 = name.count("l") + name.count("o") + name.count("v") + name.count("e")

score = score1 * 10 + score2
string = (f"Your score is {score}")

if score < 10 and 90 < score:
    print(f"{string}, you go together like coke and mentos.")
elif 40 <= score and score <= 50:
    print(f"{string}, you are alright together.")
else:
    print(string)
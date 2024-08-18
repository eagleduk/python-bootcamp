import random


def check(answer):
    guess = int(input("Make a guess: "))

    if answer == guess:
        return False
    elif answer < guess:
        print("Too high.")
    elif answer > guess:
        print("Too low.")

    return True


def choose_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return 10
    return 5


def game():
    print("Welcome to the Number Guessing Game!")
    answer = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")

    level = choose_level()

    check_input = True
    check_count = 0

    while check_count < level and check_input:
        print(f"You have {level - check_count} attempts remaining to guess the number.")
        check_input = check(answer)
        check_count += 1

    if check_input:
        print(f"Pssst, the correct answer is {answer}")
        print("You've run out of guesses, you lose.")
    else:
        print(f"You got it! The answer was {answer}.")
        print("Guess again.")


game()
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

random_index = random.randint(0, len(word_list)-1)
word = word_list[random_index]

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

input_char = input("Guess a letter: ")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in word:
    if letter == input_char:
        print("Right")
    else:
        print("Wrong")
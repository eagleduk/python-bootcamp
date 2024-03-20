import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]

you_answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_answer = random.randint(0,2)


if you_answer > 2 or you_answer < 0:
    print("invaild number, you lose")
else:
    print(list[you_answer])
    print("Computer chose:")
    print(list[computer_answer])
    if you_answer == computer_answer:
        print("Draw")
    else:
        if you_answer == 0:
            if computer_answer == 2:
                print("You win")
            else:
                print("You lose")
        
        if you_answer == 1:
            if computer_answer == 0:
                print("You win")
            else:
                print("You lose")
        
        if you_answer == 2:
            if computer_answer == 1:
                print("You win")
            else:
                print("You lose")
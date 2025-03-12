#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/Letters/starting_letter.txt") as s:
        letter_template = s.read()


with open("./input/Names/invited_names.txt") as n:
    names = n.read().split("\n")

for name in names:
    with open(f"./Output/ReadyToSend/letter_to_{name}", mode="w") as l:
        l.write(letter_template.replace("[name]", name))
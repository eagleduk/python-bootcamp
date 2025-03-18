import pandas

natos = pandas.read_csv("./nato_phonetic_alphabet.csv")
print(natos)

nato_dict = {row.letter: row.code for (idx, row) in natos.iterrows()}
print(nato_dict)

name_input = input("Enter a word: ")

result = [nato_dict[letter.upper()] for letter in name_input]

print(result)
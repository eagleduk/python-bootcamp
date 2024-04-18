alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(caesar_text, shift_amount, direction):
  result_text = ""
  for letter in caesar_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount

    if direction == "decode":
      position = alphabet.index(letter, 25)
      new_position = position - shift_amount

    result_text += alphabet[new_position]
  print(f"The {"encode" if direction == "encode" else "decode"} text is {result_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(caesar_text=text, shift_amount=shift, direction=direction)
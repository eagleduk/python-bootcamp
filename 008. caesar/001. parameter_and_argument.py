# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# No Parameter
def greet():
    print("hello")
    print("hello")
    print("hello")

greet()

# 1 Parameter
def greet_with_name(name): # parameter
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Messi") # Argument

# 2 Parameter
def greet_with(name1, name2):
    print(f"Hello {name1}")
    print(f"Hi {name2}")

greet_with("Messi", "Ronaldo")

greet_with(name2="SON", name1="KIM")
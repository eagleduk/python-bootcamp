line1 = ["O","O","O"]
line2 = ["O","O","O"]
line3 = ["O","O","O"]

map = [line1, line2, line3]

position = input()

position0 = position[0]
position1 = position[1]

if position0 == "a" or position0 == "A":
    map[int(position1) - 1][0] = "X"
elif position0 == "b" or position0 == "B":
    map[int(position1) - 1][1] = "X"
else:
    map[int(position1) - 1][2] = "X"

print(map)


try:
    file = open("TEST.txt")
except FileNotFoundError as message:
    file = open("TEST.txt", "w")
else:
    content = file.read()
finally:
    file.close()
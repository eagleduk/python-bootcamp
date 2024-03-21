students = input().split(" ")

total = 0
for student in students:
    total += int(student)

print(f"total height = {total}")
print(f"number of students = {len(students)}")
print(f"average height = {int(total / len(students))}")
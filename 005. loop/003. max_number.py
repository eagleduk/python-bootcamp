scores = input().split(" ")

max_score = 0
for score in scores:
    if max_score < int(score):
        max_score = int(score)

print(f"The highest score in the class is: {max_score}")
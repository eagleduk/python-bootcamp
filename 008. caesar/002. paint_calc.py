import math


def paint_calc(height, width, cover):
    result = math.ceil(height * width / cover)
    print(f"You'll need {result} cans of paint.")

test_h = int(input())
text_w = int(input())
coverage = 5
paint_calc(height=test_h, width=text_w, cover=coverage)
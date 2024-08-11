student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "neville": 62
}

'''
91-100 "Outstanding"
81-90 "Exceeds Expectations"
71-80 "Acceptable"
  -70 "Fail"
'''

student_grades = {}

for name in student_scores:
    score = student_scores[name]
    grade = "Outstanding"

    if score <= 70:
        grade = "Fail"
    elif score <= 80:
        grade = "Acceptable"
    elif score <= 90:
        grade = "Exceeds Expectations"

    student_grades[name] = grade

print(student_grades)
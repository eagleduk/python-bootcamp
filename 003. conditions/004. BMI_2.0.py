height = float(input());
weight = int(input());

bmi = (float(weight / height**2))

string = f"Your BMI is {bmi},"

if bmi < 18.5:
    print(f"{string} you are underweight.")
elif bmi < 25:
    print(f"{string} you have a normal weight.")
elif bmi < 30:
    print(f"{string} you are slightly overweight.")
elif bmi < 35:
    print(f"{string} you are obese.")
else:
    print(f"{string} you are clinically obese.")

print("Enter your weight in pounds")
lb = input()
lb = float(lb) /2.204

print("Enter your height in inches")
height = input()
height = float(height)
height = height * 2.54
height = height / 100

bmi = lb / (height**2)
bmi = round(bmi, 1)

if bmi < 18.5:
	print(f"Your BMI is {bmi}. Classified as underweight.")
elif bmi >= 18.5 and bmi <=24.9:
	print(f"Your BMI is {bmi}. Classified as a normal weight.")
elif bmi >= 25 and bmi <=29.9:
	print(f"Your BMI is {bmi}. Classified as overweight.")
elif bmi >= 30:
	print(f"Your BMI is {bmi}. Classified as obese")

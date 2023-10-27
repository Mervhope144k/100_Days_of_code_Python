print("Welcome to BMI calculator! version 2")
print("Please Enter you height")
height = float(input())
print("Please Enter your weight")
weight = int(input())
BMI = round((weight) / (height * height), )
if (BMI < 18.5):
    print(f"Your BMI is {BMI} and you are Underweight")
elif(BMI >= 18.5 and BMI <= 24.9):
    print(f"Your BMI is {BMI} and you have a normal weight")
elif (BMI >= 25 and BMI <= 29.9):
    print(f"Your BMI is {BMI} and you are overweight")
else:
    print(f"Your BMI is {BMI} and you are Obese")
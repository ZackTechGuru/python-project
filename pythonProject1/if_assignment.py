print("BMI Calculator")
weight = float(input("Enter your weight in Kilograms: "))
height = float(input("Enter your height in meters: "))
BMI = weight/height**2
if BMI < 18.5:
    print("You are underweight")
elif BMI >= 18.5 and BMI <= 25:
    print("Normal")
elif BMI >= 25 and BMI<=30:
    print("You are overweight")
else:
    print("You are obese")
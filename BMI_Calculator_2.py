height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in Kgs: "))

BMI = round(weight / (height ** 2))

if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are UNDERWEIGHT")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you are NORMAL WEIGHT")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are OVERWEIGHT")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are OBESE")
elif BMI > 35:
    print(f"Your BMI is {BMI}, you are clinically OBESE")
else:
    print("Invalid Option!")

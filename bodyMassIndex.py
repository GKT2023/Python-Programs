'''
BMI = weight(kg) / height(m**2)
'''

wt = float(input("enter your weight in kilograms: "))
height = float(input("enter your height in meters: "))

BMI = round((wt / height ** 2), 2)

print(f"body mass index: {BMI}")


if BMI <= 18.5:
    print("you are underweight")
elif 18.5  < BMI <=24.9:
    print("your weight is normal")
elif 25 < BMI <=29.29:
    print("you are overweight")
else:
    print("you are obese")
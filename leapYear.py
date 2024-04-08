year = int(input("Enter a year: "))

## if a year is divided by 100 and 400, then it is a leap yr

## also, if no is not divided by 100 but divided by 4 is  a leap yr

## otherwise no is not a leap yr

if year % 100 == 0 and year % 400 == 0:
    print("leap year")
elif year % 100 != 0 and year % 4 == 0:
    print("leap year")
else:
    print("not a leap year")
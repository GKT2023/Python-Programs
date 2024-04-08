'''
solve a quadratic equation: ax**2 + bx + c = 0
where a,b,c are real no
and a != 0
solution of equation is given by: 

(-b +- (b**2 - 4ac)**0.5)/(2a)

'''
import math

a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = int(input("enter the value of c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    # TWO REAL AND DISTINCT ROOT
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"root1 is :{root1} and root2 is: {root2}")
elif discriminant == 0:
    # ONE REAL (REPEATED ROOT)
    root = -b / (2 * a)
    print("root: ", root)
else:
    # COMPLEX ROOT
    real_part = -b / (2 * a)
    imaginaryPart = math.sqrt(abs(discriminant)) / (2 * a)
    # root1 = real_part + imaginaryPart + "i"
    # root2 = real_part - imaginaryPart + "i"
    print(f"root 1 is: {real_part} + {imaginaryPart}i")
    print(f"root 2 is: {real_part} + {imaginaryPart}i")
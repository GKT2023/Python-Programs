'''
it is the largest possitive integer that divides two or more number, withut leaving a remainder.

formula of HCF: GCD(x,y)

for more than two number, you can find HCF by taking GCD of pairs of numbers at a time until uou reach last pair.
'''

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))


def getHCF(x,y):
    if x < y:
        smaller = x
    else:
        smaller = y
    
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf
    
print(getHCF(x,y))
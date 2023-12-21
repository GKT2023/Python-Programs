'''
write a program to find least common multiple:

LCM is the smallest multiple that is exactly divisible by two or more numbers.

formula:

for two nos a, and b, LCM can be found using:

LCM(a,b) = |a.b| / GCD(a,b)

for more than 2 nos ,you can find LCM step by step. taking lcm of all pairta of a no at a time until you reach last pair.

GCD: greatest common divisor


#############HERE YOU HAVE TO RITE A PROGRAM TO FIND LCM OF TWO NUMBERS###############

'''

x = int(input("Enter a first number: "))
y = int(input("Enter a second number: "))

def getLCM(x,y):
    if x > y:
        largest = x
    else:
        largest = y

##  while loop iterate contnuously until it found a lasrgest number which is divisible by both x and y without any remainder.

    while(True):
        if (largest % x == 0 ) and  (largest % y == 0):
            lcm = largest
            break
        largest += 1
    return lcm


print(getLCM(x,y))
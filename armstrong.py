'''
armstrong no is equals to the sum of its digits raised to the power of no of digits in the no.

ex: 153 = 1**3 + 5** 3 + 3**3
9474 = 9 ** 4 + 4 ** 4 + 7 ** 4 + 4 ** 4

'''

n = input("enter a no: ")
l = len(n)
temp = n
n = int(n)

total  = 0

for i in range(l):
    total += (int(temp[i]) ** l)

if total == n :
    print("no is armstrong")
else:
    print("no is not a armstrong num")


## another method
    
n = int(input("enter a no: "))

temp = n
total = 0
while temp > 0:
    d = temp % 10
    total += d ** len(str(n))
    temp = temp // 10

if total == n:
    print("Armstrong")
else:
    print("Not a armstrong number")

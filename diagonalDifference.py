import numpy as  np 
n = int(input())

li = []
for i in range (n):
    li.append([int(x) for x in input().split()])

ar = np.array(li, dtype= int)
# ar = [int(i) for i in ar]

print(li)

leftDiagonalSum = 0
rightDiagonalSum = 0 


for i in range(n):
    for j in range(n):
        if i == j:
            leftDiagonalSum += li[i][j]

for i in range(n):
    for j in reversed(range(n)):
        if i + j == n-1:
            rightDiagonalSum += li[i][j]

# print(leftDiagonalSum, rightDiagonalSum)

print(abs(leftDiagonalSum -rightDiagonalSum))
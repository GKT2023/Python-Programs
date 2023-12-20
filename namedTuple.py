from collections import namedtuple

n = int(input())
column_name = input().split()
# print(*column_name)
student = namedtuple("Student", column_name)
# print(student)
total = 0
sumOfAllMARKS = 0 
for i in range(n):
    # cols = [i for i in input().split()]
    record= student(*input().split())
    sumOfAllMARKS += int(record.MARKS)
    total += 1

average = sumOfAllMARKS/total
print(average)

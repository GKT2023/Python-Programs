import numpy as np

n = int(input())
a = []
b = []

for i in range(n):
    # n = list(map(int, input().split()))
    a.append(list(map(int, input().split())))
    
for i in range(n):
    # n = list(map(int, input().split()))
    b.append(list(map(int, input().split())))

A = np.array(a)
B = np.array(b)

print(A, B)

print(np.dot(A,B))
print(np.cross(A,B))

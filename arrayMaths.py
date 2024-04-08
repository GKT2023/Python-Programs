import numpy as np


n, m = list(map(int, input().split()))
l1 = []
l2 = []

for i in range(n):
    m = list((map(int, input().split())))
    l1.append(m)

for i in range(n):
    m = list((map(int, input().split())))
    l2.append(m)

ar1 = np.array((l1))
ar2 = np.array(l2)

print(ar1 + ar2)
print(ar1 - ar2)
print(ar1 * ar2)
print(ar1 // ar2)   # integer division (floor division)
print(ar1 % ar2)
print(ar1 ** ar2)
print(ar1 / ar2)  # float division

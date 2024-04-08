import numpy as np


r,c = map(int, input().split())

l = []
for i in range(r):
    c  = list(map(int, input().split()))
    l.append(c)

ar = np.array(l)
print(np.transpose(ar))
print(ar.flatten())
import numpy as np

n,m = list(map(int, input().split()))

l1 = []

for i in range(n):
    m = list(map(int, input().split()))
    l1.append(m)

ar = np.array(l1)

ar1 = np.sum(ar,axis=0)
print(ar1)
print(np.prod(ar1))

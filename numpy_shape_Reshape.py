import numpy as np

inp = list(map(int , input().split()))
ar = np.array(inp)
ar.shape = (3,3)
print(ar)

ar_new = np.reshape(ar, (3,3))
print(ar_new)

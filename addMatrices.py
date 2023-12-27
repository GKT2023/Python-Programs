import numpy as np

l1 = [[1,2,3],[4,5,6]]
l2 = [[1,2,3],[4,5,6]]

ar1 = np.array(l1)
ar2 = np.array(l2)

print(ar1 + ar2)
 
# if len(l1) != len(l2):
#     print("matrices should be of equal lengths.")
    
# else:
#     result = []
#     for i in range(len(l1)):
#         print(len(l1))
#         row = []
#         for j in range(len(l1[0])):
#             row.append(l1[i][j] + l2[i][j])
#         result.append(row)

# print(result)
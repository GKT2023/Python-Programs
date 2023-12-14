import numpy as np

array_1 = np.array([[1,2,3],[0,0,0]])
array_2 = np.array([[4,5,6] ,[7,8,9]])
array_3 = np.array([[7,8,9],[12,34,56]])

print (np.concatenate((array_1, array_2, array_3),axis=1))


'''
Task

You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .

Input Format

The first line contains space separated integers ,  and .
The next  lines contains the space separated elements of the  columns.
After that, the next  lines contains the space separated elements of the  columns.

Output Format

Print the concatenated array of size (N+M)*P.

Sample Input

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
'''

n,m,p = map(int, input().split())

l1 = []
l2 = []

for i in range(n):
    p = list(map(int, input().split()))
    l1.append(p)

for i in range(m):
    p = list(map(int, input().split()))
    l2.append(p)

ar1 = np.array(l1)
ar2 = np.array(l2)

print(ar1)
print(ar2)

concat_arr = np.concatenate((ar1, ar2),axis=0)
print(concat_arr)
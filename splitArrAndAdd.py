'''
split an array from index and add last part to the first part.

ex: [1,2,3,4,5] and index is 3

then 

[4,5] + [1,2,3] = [4,5,1,2,3]
'''

l = []
length = int(input("Enter the length of arr: "))

for i in range(length):
    l.append(int(input("enter element for array: ")))


print(l)

k = int(input("Enter an index from which you want to split a list: "))

def splitandAdd(l, k):
    first = l[0:k]
    second = l[k:]
    finalArr = second + first

    return finalArr

print(splitandAdd(l,k))
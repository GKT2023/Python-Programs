'''
itertools.combinations(iterable, r)
This tool returns the  length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Sample Code

>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
Task

You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK

'''

from itertools import combinations

def getCombination(s,r):
    return list(combinations(s,r))

if __name__ == '__main__':
    inp = input()
    s = inp.split()[0]
    s_list = sorted(list(s))
    s_sorted = "".join(i for i in s_list)
    print(s_sorted)
    r = int(inp.split()[1])
    i = 1
    while i <= r:
        comb = getCombination(s_sorted,i)
        # comb.sort()
        # print(" ".join(str(i) for i in comb))
        for items in comb:
            temp = ""
            for each in range(len(items)):
                temp += items[each]
            print(temp)
        i = i + 1
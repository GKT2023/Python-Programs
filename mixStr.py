'''
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

Given:

s1 = "America"
s2 = "Japan"
Expected Output:

AJrpan
'''
s1 = "America"
s2 = "Japan"

ind1 = len(s1)//2
ind2 = len(s2)// 2

out = s1[0] + s2[0] + s1[ind1] + s2[ind2] + s1[len(s1)-1]  + s2[len(s2)-1]
print(out)

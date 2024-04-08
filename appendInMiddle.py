'''
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "Ault"
s2 = "Kelly"
Out: AuKellylt
'''

s1 = "Ault"
s2 = "Kelly"

out = s1[0:len(s1)//2] + s2 + s1[len(s1)//2:]
print(out)
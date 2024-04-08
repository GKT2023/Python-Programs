'''
Write a program to create a new string made of the middle three characters of an input string.
str1 = "JhonDipPeta" - Dip
str2 = "JaSonAy"  - Son
'''

s = "JaSonAy"

indx = len(s) // 2


out = s[indx -1] + s[indx] + s[indx + 1]
print(out) 

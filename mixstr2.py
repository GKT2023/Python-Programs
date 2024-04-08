'''
Exercise 6: Create a mixed String using the following rules
Given two strings, s1 and s2. 
Write a program to create a new string s3 made of the first char of s1, then the last char of s2,
Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end 
of the result.

Given:

s1 = "Abc"
s2 = "Xyz"
Expected Output:

AzbycX
'''
s1 = "AbcIOP"
s2 = "Xyz"

s2_new = s2[::-1]
out = ""
if len(s1) == len(s2):

    for i in range(len(s1)):
        out+= s1[i] + s2_new[i]
elif len(s1) < len(s2):
    for i in range(len(s1)):
        out += s1[i] + s2_new[i]

    out += s2[:len(s1)]

elif len(s2) < len(s1):
    for i in range(len(s2)):
        out += s1[i] + s2_new[i]

    out += s1[len(s2):]

print(out)



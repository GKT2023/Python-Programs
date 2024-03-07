'''
Given string contains a combination of the lower and upper case letters. 
Write a program to arrange the characters of a string so that all lowercase letters should come first.

Given:

str1 = PyNaTive

Expected Output:

yaivePNT
'''

str1 = "PyNaTive"

out = ""
for i in str1:
    if i == i.lower():
        out += i
print(out)
for i in str1:
    if i in out:
        continue  # to skip the current iteration
    else:
        out+= i
print(out)

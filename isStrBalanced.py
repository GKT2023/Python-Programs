'''
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if 
all the characters in the s1 are present in s2. The character’s position doesn’t matter.

Case 1:

s1 = "Yn"
s2 = "PYnative"
Expected Output:

True

Case 2:

s1 = "Ynf"
s2 = "PYnative"
Expected Output:

False

'''
s1 = "Ynf"
s2 = "PYnative"
exist = True

for i in s1:
    if i not in s2:
        exist = False
        break
print(exist)

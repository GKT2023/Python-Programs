'''
Write a program to create a new string made of an input string’s first, middle, and last character.

'''

s = "GARIMAKOUSHIKA"

l = len(s)
mid = ""
if l % 2 == 0:
    mid += (s[(l//2)-1]) + s[l//2] 
else:
    mid+= s[l//2]


out = s[0]+ mid + s[l-1]
print(out)
'''
Write a program to find all occurrences of “USA” in a given string ignoring the case.

Given:

str1 = "Welcome to USA. usa awesome, isn't it?"

Expected Outcome:

The USA count is: 2
'''
str1 = "Welcome to USA. usa awesome, isn't it?" 

sub = "USA"
count = 0
for i in range(len(str1)):
    if str1[i:i+3] == sub.lower() or str1[i:i+3] == sub:
       count += 1
       print(str1[i:i+3])

print(count) 

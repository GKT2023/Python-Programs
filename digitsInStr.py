'''
Given a string s1, write a program to return the sum and average of the digits that appear in the string, 
ignoring all other characters.

Given:

str1 = "PYnative29@#8496"
Expected Outcome:

Sum is: 38 Average is  6.333333333333333

'''


str1 = "PYnative29@#8496"

total = 0
total_digit = 0
avg = 0
for i in str1:
    if i.isdigit():
        total += int(i)
        total_digit += 1

avg = total /total_digit

print(f"Sum is: {total} and average is: {avg}")
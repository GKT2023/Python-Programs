'''
Count all letters, digits, and special symbols from a given string

Given:

str1 = "P@#yn26at^&i5ve"
Expected Outcome:

Total counts of chars, digits, and symbols 

Chars = 8 
Digits = 3 
Symbol = 4

'''

str1 = "P@#yn26at^&i5ve"
digits = 0
chars = 0
symbols = 0
for i in str1:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        chars += 1
    else:
        symbols +=1


print(f"Digits: {digits}\nChars: {chars}\nSymbols: {symbols}")

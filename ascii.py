'''
find ASCII value of a character

ASCII : American standard code for information interchange.

it uses numerical values to represent characters.

it ranges from 0-127(for 7 bit ascii), 0-255(for 8 bit ascii)
'''

char = str(input("Enter a character: "))
print(f"Ascii value of {char } is, {ord(char)}")
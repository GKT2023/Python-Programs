'''
WAP to convert a decimal to binary, octal  and hexadecimal
'''
d = int(input("Enter a decimal number: "))

print(f"binary conversion: {bin(d)}")
print(f"Octal conversion: {oct(d)}")
print(f"Hexadecimal conversion: {hex(d)}")

print("#######################################")

print(f"binary conversion without prefix 0b: {bin(d)[2:]}")
print(f"Octal conversion without prefix 0o: {oct(d)[2:]}")
print(f"Hexadecimal conversion without prefix 0x: {hex(d)[2:]}")
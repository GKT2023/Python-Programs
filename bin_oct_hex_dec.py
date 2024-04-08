"""
binary, octal  and hexa format
"""


n = int(input())
width = len(bin(n)[2:])

for i in range(1, n+1):
    decimal_format = f"{i:{width}d}"
    octal_format = f"{oct(i)[2:]:>{width}}"
    hexadecimal_format = f"{hex(i)[2:].upper():>{width}}"
    binary_format = f"{bin(i)[2:]:>{width}}"

    print(f"no in decimal format: {i}")

    print(f"binary no with prefx 0b: {bin(i)}")
    print(f"binary no without prefx 0b: {bin(i)[2:]}")

    print(f"octal no with prefx 0o: {oct(i)}")
    print(f"octal no without prefx 0o: {oct(i)[2:]}")

    print(f"hexadecimal no with prefx 0x: {hex(i)}")
    print(f"hexadecimal no without prefx 0x: {hex(i)[2:]}")

    print(f"{i} {oct(i)[2:]} {hex(i)[2:]} {bin(i)[2:]}")
    print(f"{decimal_format} {octal_format} {hexadecimal_format} {binary_format}")
## adding nnums

def add(n):
    if n == 1:
        return 1
    else:
        return n + add(n-1)

print("sum: ",add(int(input())))

## factorial

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print("factorial: ", fact(int(input())))
a = 0
b = 1

print(a,b,end=" ")
def fibonacci(a,b):
    for i in range(5):
        c = a + b
        print(c, end = " ")
        a = b
        b = c

fibonacci(a,b)
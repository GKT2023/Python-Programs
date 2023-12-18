n = int(input("Enter a number: "))

def fibonacci(n):
    a = 0
    b  = 1
    for i in range(n):
        c = a + b
        print(c, end= " ")

        a = b
        b = c


fibonacci(n)

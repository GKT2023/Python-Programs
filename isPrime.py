n = int(input("Enter a number: "))
prime = True

if n == 1:
    print("no a prime no.")
elif n >= 2:
    for i in range(2,n+1):
        if n % i == 0 and i !=n:
            prime = False
            break

if prime:
    print("no is prime")
else:
    print("no is not a prime no")


# isPrime(n)
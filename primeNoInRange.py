prime = True
lower = 1
upper = 10

for n in range(lower, upper +1):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0 :
                break
            else:
                print(n)
                break
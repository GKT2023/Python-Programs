def recursiveFibonacci(num):
    if num <= 1 :
        return num
    else:
        return (recursiveFibonacci(num - 1) + recursiveFibonacci (num- 2))

nterms = int(input("Enter a integer: "))

if nterms <=0:
    print("enter a positive integer >= 0")
else:
    for i in range(nterms):
        print(recursiveFibonacci(i))
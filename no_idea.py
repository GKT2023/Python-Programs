length_of_array, length_of_B_set = input().split()

arrayOfElement = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for i in range(len(arrayOfElement)):
    if arrayOfElement[i] in A:

        happiness  = happiness + 1
    elif arrayOfElement[i] in B:
        happiness  = happiness + (-1)
    else:
        happiness += 0

print(happiness)
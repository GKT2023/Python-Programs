a = 10 ; b = 29 ; c=26



if a > b and a > c:
    if b > c :
        secondLargest = b
    else:
        secondLargest = c

elif b > a and b > c:
    if a > c:
        secondLargest = a
    else:
        secondLargest = c

elif c > a and c > b:
    if a > b :
        secondLargest = a
    else:
        secondLargest = b

print(secondLargest)
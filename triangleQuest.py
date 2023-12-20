'''
You are given a positive integer . Print a numerical triangle of height  like the one below:

1
22
333
4444
55555
......
'''

for i in range(1,int(input())): 
    # print(i * (str(i)))
    # print(i * ascii(i))
    print(i * f"{i:d}")


for i in range(1,int(input())): 
    # print(i * (str(i)))
    print(i * ascii(i))
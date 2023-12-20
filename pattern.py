
'''
16
16 8
16 8 4
16 8 4 2
'''
initialNum = 16
lines = 4

# for i in range(1, lines+1):
#     n = initialNum
#     for j in range(i):
#         print(n, end= " ")
#         n //= 2
#     print()

'''
     16
   8 16
  4 8 16
2 4 8 16

'''

initialNum = 16
lines = 4

for i in range(1, lines+ 1):
    n = initialNum
    for j in range(i):
        print(n, end= " ")
        n //= 2
    print()

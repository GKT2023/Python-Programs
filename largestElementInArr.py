l = [2,3,4,6,7,89,100,300,655,2,3,900]

max_num = l[0]

for i in range(len(l)):
    if l[i] >  max_num:
        max_num = l[i]

print(max_num)
print(max(l))
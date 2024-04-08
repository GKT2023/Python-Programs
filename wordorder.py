n = int(input())
li = []
for i in range(n):
    # word = input()
    li.append(input())

d = {}

for i in li:
    if i in d.keys():
        d[i] +=1
    else:
        d[i] = 1

print(len(d.keys()))
for i in d.values():
    print(i, end = " ")
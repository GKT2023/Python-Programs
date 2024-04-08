s = "AABCAAADA"
k = 3


i = 0
sublist = []
while i < len(s):
    
    sublist.append(s[i:i+k])
    i = i +k

print(sublist)

sublist_new = []

for i in sublist:
    temp_str = ""
    for j in range(len(i)):
        if i[j] in temp_str:
            continue
        else:
            
            temp_str += i[j]
    sublist_new.append(temp_str)

# print(sublist_new)

print(" ".join(i for i in sublist_new))
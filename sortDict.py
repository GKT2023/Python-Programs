from collections import OrderedDict
s = 'aabbbccde'
s_list = list(s)

# convert list into dictionary

d = {}
count =   0
for i in s_list:
    if i in d.keys():
        count = count + 1
        d[i]  +=1
    else:
        count = 1
        d[i] = 1

print("original dictionary")
print(d)

print("sort dictionary -- this will only sort keys")
d_sorted = sorted(d)
print(d_sorted)

print("to sort dict according to keys and display key,value pair both ")
d_sorted = sorted(d.items(),key= lambda x: x[0])
print(dict(d_sorted))

print("sorted dictionary as per values: ")
d_sorted = sorted(d.items(),key= lambda x: x[1])
print(dict(d_sorted))

print("sort dictionary as per value in descending order...")
d_sorted = sorted(d.items(),key= lambda x: x[1], reverse=True)
print(dict(d_sorted))

print("sort dictionary as per keys in descending order...")
d_sorted = sorted(d.items(),key= lambda x: x[1], reverse=True)
print(dict(d_sorted))



reversedSortedDict = dict(sorted(d.items(),key=lambda x:x[1], reverse=True))
print(reversedSortedDict)
r = dict(sorted(reversedSortedDict.items(), key= lambda x:(x[1],x[0])))
print(r)

maxVal = max(r.values())
print(maxVal)

top_3_values = list(reversed(sorted(r.values())))
print("top 3 values:" ,top_3_values)

li = []
for key,val in d.items():
    if d[key] == top_3_values[0] and len(li) < 3 and (key,val) not in li:
        # print(key, val)
        li.append((key, val))
    if d[key] == top_3_values[1]  and len(li) < 3 and (key,val) not in li:
        # print(key,val)
        li.append((key, val))
    if d[key] == top_3_values[2] and len(li) < 3 and (key,val) not in li:
        # print(key,val)
        li.append((key, val))


li = sorted(li,key = lambda x: (-x[1],x[0]))
print(li)


for i in li:
    print (i[0], i[1])
l = [1,2,3,4]
s = {2,4,5,6,7,8}
d = {"garima":30,"thalesh":36, "kiyana":1}
t = (2,3,4,5)

# list comprehension

l =[ (i +100) for i in l]
print(l)

s = {i*100 for i in s}
print(s)

d = {key: value * 2 for key,value in d.items()}
print(d)

t = (i * 1000 for i in t)
for i in t:
    print(  i, end  = " ")
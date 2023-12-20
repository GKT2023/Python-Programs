import random


s = "banana"

kevin = 0
stuart = 0

li = []

k = 0
if start == end and start > end: 
    start = random.randint(0,len(s))
    end = random.randint(0,len(s))
    sub = s[start : end]
    while len(sub) != len(s):

        if sub not in li:
            if sub.startswith('a') or sub.startswith('e') or sub.startswith('i') or sub.startswith('o') or sub.startswith('u') :
                li.append(sub)
                count = s.count(sub)
                stuart += count
            else:
                li.append(sub)
                count = s.count(sub)
                kevin += count
        k = k +1

print(kevin, stuart)
            
 
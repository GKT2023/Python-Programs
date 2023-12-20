import re

[]
n = int(input())

for i in range(n):
    inp = input()

    tag = r'<[A-Za-z]+>{0,1}$'
    tag_search = re.search(tag, inp)

    if tag_search:
        print(tag_search.group())

    tag_attr = r'<[A-Za-z]+[\s]*[a-zA-Z]+[\s]*[=][\s]*["][a-zA-Z]+["][*+]["]>'

    tag_attr_search = re.search(tag_attr, inp)
    
    if tag_attr_search:

        print(tag_attr_search.group(1))
        print(tag_attr_search.group(2), " > " , tag_attr_search.group(3))
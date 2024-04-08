txt = "hello, and welcome to my world."
x = ""
li= []
# for i in txt.split(" "):
#        if i == " ":
#         i = " "
#         li.append()
#         else:
#             i = i.capitalize()
#         li.ppend()



for i in txt.split(" "):
    if i == " ":
        li.append(" ")
    else:
        i = i.capitalize()
        li.append(i)
# print(li)

print(" ".join(i for i in li))
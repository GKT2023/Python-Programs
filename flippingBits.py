q = int(input())
# flippedStr = ""
for i in range(q):
    n = int(input())
    s1 = str(n)
    s1 = bin(int(s1))
    s1 = str(s1).replace('0b',"")
    s1 = s1.zfill(32)
    # print("before flippng, " ,s1)
    flippedStr  = ""
    for i in s1:
        if i == "0":
            flippedStr += "1"
        elif i == "1":
            flippedStr += "0"
    
    print(int(flippedStr, 2))

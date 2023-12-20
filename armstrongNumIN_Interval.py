lowerRange = int(input("ENter a lower range: "))
upperRange = int(input("ENter a upper range: "))

for i in range(lowerRange, upperRange+1):
    s_i = str(i)
    temp = i 
    total = 0
    while temp > 0 :
        d = temp % 10
        total += d ** len(s_i)
        temp = temp // 10

    if total == i:
        print(i)
    

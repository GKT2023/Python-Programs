def wrapper(f):
    def fun(l):
        # complete the function
        l2 = []
        l3 = []
        sortedList = []
        for i in l:
            l2.append((str(i)))
        
        for i in l2:
            if i.startswith('0'):
                p = i.replace(str(i[0]), '91')
                print(p)
                formatted_Number= "+" + p[0:2] + " " + p[2:7] + " " + p[7:12]
                l3.append(formatted_Number)                     
            else:
                p = i
                formatted_Number = "+" + p[0:2] + " " + p[2:7] + " " + p[7:12]
                l3.append(formatted_Number)
                
        for i in l3:
            if len(i) < 15:
                temp = i 
                temp  = temp.replace(" ", "")
                # print(temp)
                temp = temp[0:3] + " 91" + temp[3:6] + " " + temp[6:11]
                sortedList.append(temp) 
            else:
                sortedList.append(i)
                # pass
        sortedList.sort()
        for i in sortedList:
            print(i)
    return fun
    


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 



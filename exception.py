T = int(input())
for i in range(T):
    cmd = input()
    cmd = cmd.split(" ")
    a  = cmd[0]
    b = cmd[1]

    try:
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("zero division error: ")
    except ValueError as e:
        print("Error Code: ",e)
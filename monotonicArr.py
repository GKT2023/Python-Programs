'''
an array is monotonic if it is entirely  in increasing order  or decreasing order.

'''

def isMonochrome(arr):
    decrement = increment = True

    ## loop to check if array is not increasing
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]: # check if array is not increasing
            increment = False
    
    ## loop to check if array is decreasng
    for i in range(len(arr) -1):
        if arr[i] < arr [i+1]:
            decrement = False
    
    return increment or decrement


if __name__== '__main__':
    
    l = []
    length = int(input("Enter the length of arr: "))

    for i in range(length):
        l.append(int(input("enter element for array: ")))

    print(l)

    ans = isMonochrome(l)
    if ans == True:
        print("yes")
    else:
        print("No")


'''
swap two variables.
a = 5 b = 8
then
output should be 
a = 8 b = 5

'''

### swap using third variable

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

print(f"value of a before swap is {a} and value of b before swap is {b}")
temp = a
a  = b
b = temp

print(f"value of a after swap is {a} and value of b after swap is {b}")

## swapping without third variable

c = a + b
a = c - b
b = c - a

print(f"value of a after swap is {a} and value of b after swap is {b}")
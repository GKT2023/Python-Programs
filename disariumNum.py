''''
Disarium no is a number that is equal to the sum of its digits each raised to the power of respective position.

ex: 89 = 8 ** 1 + 9 ** 2
'''

s_num = input("Enter a number: ")

i_num = int(s_num)

temp = i_num
final_num = 0 


for i in range(len(s_num)):
    final_num += int(s_num[i]) ** (i + 1)
    # final_num = int(final_num)
    
print(final_num)

if final_num == i_num:
    print("no is a Disarium Number.")
else:
    print("not a disarium number")
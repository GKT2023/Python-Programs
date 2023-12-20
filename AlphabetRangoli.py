'''
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
'''

# row = 10

# ch = chr(65)
# for i in range(1, row + 1):
#     ch = chr(65 +i)
#     print("-"*(row-i), ch * (2 * i -1), "-"*(row-i))
    
# for i in range(row-1, 0, -1):
#     ch =chr(65 + i)
#     print("-"*(row-i), ch * (2 * i -1), "-"*(row-i))



# def print_diamond_pattern(size):
#     for i in range(size):
#         line = ""
#         for j in range(size - i - 1):
#             line += "--"
#         for k in range(i + 1):
#             line += chr(ord('a') + size - k - 1)
#             if k < i:
#                 line += "-"
#         for l in range(i):
#             line += "-" + chr(ord('a') + size - l - 1)
#         for m in range(size - i - 1):
#             line += "--"
#         print(line)

# # Set the size of the diamond (adjust as needed)
# diamond_size = 10

# # Print the diamond pattern
# print_diamond_pattern(diamond_size)



print (set(set(['H','a','c','k','e','r','r','a','n','k'])))

print (set(['H','a','c','k','e','r','r','a','n','k']))

print (set(enumerate(['H','a','c','k','e','r','r','a','n','k'])))
# set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
'''
Input Format

The first line contains integer , the number of elements in the set .
The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer , the number of commands.
The next  lines contains either pop, remove and/or discard commands followed by their associated value.

Constraints



Output Format

Print the sum of the elements of set  on a single line.

Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
Sample Output

4
'''

n = int(input())
s = set(map(int, input().split()))
noOfCommands = int(input())
for command in range(noOfCommands):
    command = input()
    
# print(len(s))


for cmd in command:
    cmd = cmd.split(" ")
    if "pop" in cmd:
        s= s.pop()

    elif "remove" in cmd:
        s= s.remove(int(cmd[1]))
    elif  "discard" in cmd:
        s = s.discard(int(cmd[1]))
print(len(s))

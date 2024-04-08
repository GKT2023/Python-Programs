# Enter your code here. Read input from STDIN. Print output to STDOUT

testCase = int(input())

blocks = []
for i in range(testCase):
    noOfCubes = int(input())
    for i in range(noOfCubes):
       blocks.append(list(map(int, input().split())))

            
print(blocks)

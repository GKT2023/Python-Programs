sizeOfString = int(input())
inputStrings = []
QueryStrings = []

for i in range (sizeOfString):
    inputStrings.append(input())


sizeOfQueries = int(input())

for i in range(sizeOfQueries):
    QueryStrings.append(input())

# print(inputStrings, QueryStrings)

finalCount = []
for s in QueryStrings:
    # count = 0 
    if s in inputStrings:
        count = inputStrings.count(s)
    else:
        count = 0 
    finalCount.append(count)

for i in finalCount:
    print(i)
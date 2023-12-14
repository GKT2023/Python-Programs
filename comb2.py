from itertools import combinations

def getCombination(s,k):
    return list(combinations(s,k))

if __name__ == '__main__':
    cmd = input().split()
    s = cmd[0]
    k = int(cmd[1])

    for i in range(1, k+1):
        c = getCombination(sorted(s),i)
        # print(c)
        for j in c:
            for k in j:
                print(k, end = "")
                
            print()

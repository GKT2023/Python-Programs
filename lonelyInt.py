def lonelyInteger(li):
    for i in li:
        if li.count(i) == 1:
            return i
            # break


if __name__ == '__main__':
    n = int(input())
    li = list(map(int, input().split()))
    out = lonelyInteger(li)
    print(out)
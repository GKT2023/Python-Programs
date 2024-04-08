for n in range(1,101):
    s = str(n)
    disarium = 0
    for i in range(len(s)):
        disarium += int(s[i]) ** (i+1)
    if disarium == n :
        print(n)
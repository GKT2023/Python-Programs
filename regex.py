import re

s = input()

# p = r'[^aeiouAEIOU]([aeiouAEIOU])\1{2}+[^aeiouAEIOU]'
p = r'[^aeiouAEIOU]([aeiouAEIOU]{2,})+[^aeiouAEIOU]'

m = re.findall(p,s)


if m:
    print(*m, sep = "\n")
    
else:
    print(-1)

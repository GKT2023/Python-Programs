s1 = "We promptly judged antique ivory buckles for the next prize"
s2 = "We promptly judged antique ivory buckles for the prize"

def isPangram(s):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabets:
        if i not in s.lower():
            return False
        # break
    return True
    

s1 = isPangram(s1)
s2 = isPangram(s2)

print(s1, s2)
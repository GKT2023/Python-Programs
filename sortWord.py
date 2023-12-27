s = "How are you Garima. Hope you are doing well. How is your mental health. is it better"

c = ""

words = [word.capitalize() for word in s.split()]

print(words)

words.sort()

print(" ".join(words))
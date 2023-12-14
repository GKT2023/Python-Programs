from itertools import combinations_with_replacement, combinations
 
 
a ="GEeks"
 
l = list(combinations_with_replacement(a, 2))
print("COMBINATIONS WITH REPLACEMENTS OF STRING GEeks OF SIZE 2.")
print(l)

l1 = list(combinations(a,2))
print(l1)
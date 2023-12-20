from itertools import combinations

N = int(input())
alpha_list = list(input().split())
k = int(input())

possible_tuples = list(combinations(alpha_list,k ))
# print("possible all tuples: ", possible_tuples)

occurrence = 0
for i in possible_tuples:
    if 'a' in i:
        occurrence += 1

# print(occurrence)

probability = occurrence / len(possible_tuples)
print(probability)

# print(round(probability, 4))
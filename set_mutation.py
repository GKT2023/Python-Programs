length_set_A = int(input())
A = set(map(int, input().split()))
No_of_other_sets = int(input())


for i in range(No_of_other_sets):
    cmd = input().split()
    B = input().split()
    final_set = set()
    if cmd[0] == "update":
        A.update(set(B))
        
    elif cmd[0] == "intersection_update":
        A.intersection_update(set(B))



print(sum(A))
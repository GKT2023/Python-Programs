def findPercentage(query_name):
    avg = 0
    for key,val in student_marks.items():
        if key == query_name:
            avg = (sum(student_marks[query_name]))/ len(student_marks[query_name])
            avg = round(avg,2) 
    return avg





if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *marks = input().split()
        scores = list(map(float,marks))
        student_marks[name] = scores
    query_name = input()
    print(findPercentage(query_name))



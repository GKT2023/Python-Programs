'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
'''
python_students = []
for i in range(int(input())):
    name = input()
    marks = float(input())
    python_students.append([name,marks])
print(python_students)

temp = []

for i in python_students:
    temp.append(i[1])

minScore = min(temp)
updated_students = []
for i in range (len(python_students)):
    if python_students[i][1] != minScore:
        updated_students.append(python_students[i])

print(updated_students)

temp2 = []

for i in updated_students:
    temp2.append(i[1])


minUpdatedStudent = min (temp2)

studentsWithSecondLowestScors = []
for i in range(0,len(updated_students)):
    if updated_students[i][1] == minUpdatedStudent:
        studentsWithSecondLowestScors.append(updated_students[i][0])

# print(studentsWithSecondLowestScors)
studentsWithSecondLowestScors.sort()
for i in studentsWithSecondLowestScors:
        print(i)

# updatedList = [i for i in students if students[i][1] != minScore]
# print(updatedList)
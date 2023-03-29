students = [i for i in range(1, 31)]
for j in range(28):
    temp = int(input())
    students.pop(students.index(temp))

[print(k) for k in students]

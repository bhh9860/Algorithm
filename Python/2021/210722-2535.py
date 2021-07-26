list1 = []
for i in range(int(input())):
    list1.append(list(map(int, input().split())))

list1.sort(key=lambda x: x[2])
class1 = []

class1.append(list1[-1][0])
[print(i, end = ' ') for i in list1.pop()[:2]]
print()
class1.append(list1[-1][0])
[print(i, end = ' ') for i in list1.pop()[:2]]
print()

if len(list(set(class1))) == 1:
    for i in list1:
        if i[0] == class1[0]:
            del list1[list1.index(i)]
    [print(i, end = ' ') for i in list1.pop()[:2]]

else:
    [print(i, end = ' ') for i in list1.pop()[:2]]

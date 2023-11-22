a = []
[a.append(list(map(int, input().split()))) for i in range(9)]

num = 0
idx = [1, 1]
for i in range(9):
    temp = max(a[i])
    if num < temp:
        num = temp
        idx = [i+1, a[i].index(temp)+1]

print(num)
for i in idx:
    print(i, end=' ')

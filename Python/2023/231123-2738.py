a, b = map(int, input().split())
c = []
for i in range(a):
        c.append(list(map(int, input().split())))

d = []
for i in range(a):
        d.append(list(map(int, input().split())))

        
ans = []
for i in range(a):
    temp = []
    for j in range(b):
        temp.append(c[i][j]+d[i][j])
    ans.append(temp)

for i in ans:
    for j in i:
        print(j, end=' ')
    print()

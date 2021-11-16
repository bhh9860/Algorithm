n = int(input())
rank = [1] * n
lists = []
for _ in range(n):
    lists.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if lists[i][0] < lists[j][0] and lists[i][1] < lists[j][1]:
            rank[i] += 1

[print(i, end = ' ') for i in rank]

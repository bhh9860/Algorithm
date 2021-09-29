a = 0
lists = []
for i in range(10):
    c = list(map(int, input().split()))
    a -= c[0]
    a += c[1]
    lists.append(a)

print(max(lists))

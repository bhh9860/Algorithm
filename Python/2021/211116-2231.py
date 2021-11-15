n = int(input())
ans = 0
for i in range(1, n+1):
    if n == i + sum(list(map(int, list(str(i))))):
        ans = i
        break

print(ans)

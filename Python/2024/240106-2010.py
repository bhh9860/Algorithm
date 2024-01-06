import sys

n = int(sys.stdin.readline())
ans = 0
for i in range(n):
    ans += int(sys.stdin.readline())

ans -= n-1

print(ans)

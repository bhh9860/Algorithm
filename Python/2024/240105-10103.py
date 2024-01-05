a, b = 100, 100
for i in range(int(input())):
    c, d = list(map(int, input().split()))
    if c < d:
        a -= d
    elif c > d:
        b -= c

print(a)
print(b)

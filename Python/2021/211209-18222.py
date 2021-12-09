n = int(input())
tmp = 1
cnt = 0

while tmp < n:
    tmp *= 2

while tmp != 1:
    if n > (tmp//2):
        cnt += 1
        tmp //= 2
        n -= tmp
    else:
        tmp //= 2

print(0) if cnt % 2 == 0 else print(1)

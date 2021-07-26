import math

def sosu(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n = int(input())
number = list(map(int, input().split()))
count = 0
for i in number:
    if i == 1:
        pass
    else:
        if sosu(i):
            count += 1

print(count)

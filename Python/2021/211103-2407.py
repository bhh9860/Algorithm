from math import factorial
n, m = list(map(int, input().split()))
up = factorial(n)
down = factorial(n-m) * factorial(m)
print(up/down)

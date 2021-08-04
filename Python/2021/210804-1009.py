import sys

for i in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    c = pow(a, b, 10)
    if c == 0:
        print(10)
    else:
        print(c)

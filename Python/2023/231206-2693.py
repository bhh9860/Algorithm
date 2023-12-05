n = int(input())
for _ in range(n):
    elem = list(map(int, input().split()))
    elem.sort()
    print(elem.pop(len(elem)-3))

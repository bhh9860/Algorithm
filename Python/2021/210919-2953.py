a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
e = list(map(int, input().split()))

lists = [sum(a), sum(b), sum(c), sum(d), sum(e)]

print(lists.index(max(lists))+1, max(lists))

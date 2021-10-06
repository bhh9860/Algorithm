import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
listsn = list(map(int, input().split()))
m = int(input())
listsm = list(map(int, input().split()))

c = Counter(listsn)

for i in listsm:
	print(c[i], end = ' ')

import sys

n = int(input())
time = []
for i in range(n):
	time.append(list(map(int, sys.stdin.readline().split())))
time.sort(key = lambda x: (x[1], x[0]))

point = 0
a = time[0][1]
cnt = 1

for i in time[1:]:
	point += 1
	if i[0] >= a:
		cnt += 1
		a = time[point][1]
print(cnt)

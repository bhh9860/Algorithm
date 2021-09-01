import sys
num = []

input = sys.stdin.readline
for i in range(int(input())):
	n = int(input())
	if n != 0:
		num.append(n)
	else:
		del num[-1]
		
print(sum(num))

n = int(input())
i = 1
sum = 0

while True:
	if n >= sum + i:
		sum += i
		i += 1
	else:
		break

print(i-1)

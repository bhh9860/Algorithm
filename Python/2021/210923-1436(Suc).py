n = int(input())
count = 0
while n:
	count += 1
	if '666' in str(count):
		n -= 1
		print(count)
print(count)

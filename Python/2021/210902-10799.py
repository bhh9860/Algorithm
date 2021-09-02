input = input()
cnt = 0
n = 0
for i in range(len(input)):
	if input[i] == '(':
		n += 1
	else:
		n -= 1
		if input[i-1] == '(':
			cnt += n
		else: 
			cnt += 1
	
print(cnt)

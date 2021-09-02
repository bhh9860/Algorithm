while True:
	stack = []
	ans = True
	sentence = input()
	if sentence == '.':
		break
		
	for i in sentence:
		if i == '.':
			break
		elif i == '[' or i == '(':
			stack.append(i)
		elif i == ']' or i == ')':
			if len(stack) > 0:
				if i == ']':
					if stack[-1] == '[':
						del stack[-1]
					else:
						ans = False
						break
				if i == ')':
					if stack[-1] == '(':
						del stack[-1]
					else:
						ans = False
						break
			else:
				ans = False
				break
				
	if len(stack) != 0:
		ans = False
		
	if ans:
		print('yes')
	else:
		print('no')

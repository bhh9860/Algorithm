stack = []
number = [i for i in range(1, int(input())+1)]
number.reverse()
plan = [int(input()) for j in range(number[0])]
n = 0
answer = []

while True:
	stack.append(number.pop()) # number append
	answer.append('+')
	while stack[len(stack)-1] == plan[n]: # 確認
		del stack[len(stack)-1]
		answer.append('-')
		n += 1
		if len(stack) == 0:
			break
	
	if len(answer) // 2 == len(plan):
		break
		
	if len(number) == 0 and plan[n] != stack[len(stack)-1]:
		answer.append('NO')
		break

if answer[len(answer)-1] == 'NO':
	print('NO')
else:
	for i in answer:
		print(i)



#[print(i) if answer[len(answer)-1] != 'NO' else print('NO') for i in answer]

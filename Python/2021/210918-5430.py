# sys 스트립은 왜 붙이는지 모르겠는데 안붙여도 맞았다고 나옴.
# sys 스트립은 다른거 베껴서 그냥 넣음. 좀 더 빠른 것 같아서
from collections import deque
import sys

input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
	command = list(input().strip())
	lenlists = int(input())
	lists = input().strip()
	if len(lists) == 2:
		if command.count('D') == 0:
			print('[]')
			continue
		else:
			print('error')
			continue
	else:
		lists = deque(list(map(int, (lists[1:-1]).split(","))))
	index = True
	error = False
	
	for i in command:
		if i == 'R':
			index = not index
		elif i == 'D':
			try:
				if index:
					lists.popleft()
				else:
					lists.pop()
			except:
				print('error')
				error = True
				break
	
	if error:
		continue
	else:
		lists = list(map(str, lists))
		print('['+(','.join(lists))+']') if index else print('['+(','.join(lists[::-1]))+']')

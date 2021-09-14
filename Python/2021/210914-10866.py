import sys
from collections import deque
lists = deque(list());
input = sys.stdin.readline

for _ in range(int(input())):
	a, *b = list(map(str, input().split()))
	if b:
		if a[-1] == 't':
			lists.appendleft(b[0])
		else:
			lists.append(b[0])
	
	elif a == 'pop_front':
		print(lists.popleft()) if lists else print(-1)
	
	elif a == 'pop_back':
		print(lists.pop()) if lists else print(-1)
	
	elif a == 'size':
		print(len(lists))
		
	elif a == 'empty':
		print(1) if not lists else print(0)
	
	elif a == 'front':
		print(lists[0]) if lists else print(-1)
		
	elif a == 'back':
		print(lists[-1]) if lists else print(-1)

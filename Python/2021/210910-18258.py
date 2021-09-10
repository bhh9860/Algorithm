import sys
from collections import deque
input = sys.stdin.readline

lists = deque()
for _ in range(int(input())):
	command = deque(input().split())
	
	if command[0] == "push":
		lists.append(int(command[1]))
		
	elif command[0] == "pop":
		if len(lists) > 0:
			print(lists.popleft())
		else:
			print(-1)
	
	elif command[0] == "size":
		print(len(lists))
	
	elif command[0] == "empty":
		if len(lists) == 0:
			print(1)
		else:
			print(0)
	
	elif command[0] == "front":
		if len(lists) == 0:
			print(-1)
		else:
			print(lists[0])
	
	elif command[0] == "back":
		if len(lists) == 0:
			print(-1)
		else:
			print(lists[-1])

from collections import deque

for _ in range(int(input())):
	n, get = list(map(int, input().split()))
	importance = deque(list(map(int, input().split())))
	count = 1
	
	while True:
		complete = True
		for i in range(1, len(importance)):
			if importance[0] < importance[i]:
				if get == 0:
					get = len(importance)-1
				else:
					get -= 1
				importance.append(importance.popleft())
				complete = False
				break
		
		if complete	== True:
			if get == 0:
				print(count)
				break
			else:
				count += 1
				importance.popleft()
				get -= 1

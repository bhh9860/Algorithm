from collections import deque
lists = deque()

n = int(input())
[lists.append(i) for i in range(1, n+1)]

while len(lists) >= 2:
	del lists[0]
	lists.append(lists.popleft())

print(lists[0])

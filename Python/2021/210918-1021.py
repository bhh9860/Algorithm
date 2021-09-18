from collections import deque

n, popnum = list(map(int, input().split()))
select = list(map(int, input().split()))
lists = deque(list(range(1, n+1)))
count = 0

for i in select:
	if i == lists[0]:
		lists.popleft()
	else:
		index = lists.index(i)
		if index <= len(lists) // 2:
			for j in range(index):
				lists.rotate(-1)
				count += 1
		else:
			for j in range(len(lists) - index):
				lists.rotate()
				count += 1
		
		lists.popleft()
print(count)

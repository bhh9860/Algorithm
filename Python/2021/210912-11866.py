n, cnt = list(map(int, input().split()))
lists = list(map(int, range(1, n+1)))
index = 0
ans = []

while len(lists) != 1:
	index += cnt-1
	if len(lists) > index:
		ans.append(lists.pop(index))
	else:
		index %= len(lists)
		ans.append(lists.pop(index))

ans.append(lists[0])
ans = list(map(str, ans))
print("<" + ', '.join(ans) + ">")

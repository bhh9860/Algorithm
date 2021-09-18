n = int(input())
lists = list(map(int, input().split()))
ans = []
temp = -1

for i in range(len(lists)-1):
	if temp == -1:
		pass
		
	else:
		if temp == lists[i+1]:
			pass
		else:
		if tempi >= lists[i]:
			ans.append(temp)
			continue
		
	
	count = 0
	for j in range(i+1, len(lists), 1):
		if lists[i] < lists[j]:
			temp = lists[j]
			tempi = lists[i]
			ans.append(temp)
			break
		
		
	if temp == -1:
		ans.append(-1)		
			
print(ans.append(-1))
print(ans)

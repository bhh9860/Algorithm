import sys
input = sys.stdin.

n = int(input())

lists = list(map(int, input().split()))
ans = []
index = len(lists)-1
count = 0

for i in range(len(lists) - 1):
	count += 1
	if index == i:
		index = len(lists) - 1
	for j in range(i+1, index+1, 1):
		if lists[i] < lists[j]:
			index = j
			ans.append(lists[j])
			break
		
	
		if j+1 == len(lists):
			if len(ans) > 0:
				if count > i:
					ans.append(-1)
			else:
				ans.append(-1)	

ans.append(-1)
print(ans);

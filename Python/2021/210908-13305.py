n = int(input())
km = list(map(int, input().split()))
cost = list(map(int, input().split()))

temp = 0
ans = 0
for i in range(1, n):
	if cost[temp] >= cost[i]:
		ans += cost[temp] * sum(km[temp:i])
		temp = i

if temp != i:
	ans += cost[temp] * sum(km[(n-1)-(i-temp):])
	
print(ans)

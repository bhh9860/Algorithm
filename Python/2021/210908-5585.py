cost = int(input())
money = 1000 - cost
ans = 0
coin = [500, 100, 50, 10, 5, 1]

for i in coin:
	if money >= i:
		ans += money // i
		money = money % i

print(ans)

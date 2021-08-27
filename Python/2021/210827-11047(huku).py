coin = []
cnt = 0
n, hap = map(int, input().split())
for _ in range(n):
	coin.append(int(input()))

for i in coin[::-1]:
	if hap >= i:
		cnt += hap // i
		hap %= i

print(cnt)

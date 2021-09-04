n, k = map(int, input().split())
nfac = 1
for i in range(2, n+1):
	nfac *= i

nkfac = 1
for i in range(2, n-k+1):
	nkfac *= i
	
kfac = 1
for i in range(2, k+1):
	kfac *= i

print(int(nfac/(nkfac*kfac)))

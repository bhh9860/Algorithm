n = int(input())
listsn = sorted(list(map(int, input().split())))
m = int(input())
listsm = list(map(int, input().split()))


def binary_find(start, end, listsnum, find):
	mid = (start + end) // 2
	if start > end:
		return 0
	else:
		if mid > len(listsnum)-1:
			return 0
		elif listsnum[mid] == find:
			return 1
		elif listsnum[mid] > find:
			return binary_find(start, mid-1, listsnum, find)
		elif listsnum[mid] < find:
			return binary_find(mid+1, end, listsnum, find)
			
for i in listsm:
	print(binary_find(0, n, listsn, i))

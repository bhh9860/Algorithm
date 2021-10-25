n, m = list(map(int, input().split()))
trees = list(map(int, input().split()))
longest_tree = max(trees)
shortest_tree = 0

def check(trees, longest_tree, shortest_tree, m):
	if shortest_tree < longest_tree:
		global temp 
		slice_tree = (longest_tree + shortest_tree) // 2
		temp = slice_tree
		sum = 0
		for i in trees:
			if i > slice_tree:
				sum += i - slice_tree
				if sum >= m:
					shortest_tree = slice_tree + 1
					return check(trees, longest_tree, shortest_tree, m)
				
		longest_tree = slice_tree - 1
		return check(trees, longest_tree, shortest_tree, m)
	
	else:
		return longest_tree, shortest_tree

print(check(trees, longest_tree, shortest_tree, m))

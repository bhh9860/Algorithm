for i in range(int(input())):
	first, second = input().split()
	lists = []
	for j in range(len(first)):
		firstord = ord(first[j])
		secondord = ord(second[j])
		if secondord >= firstord:
			lists.append(secondord - firstord)
		else:
			lists.append((secondord+26) - firstord)
	
	lists = list(map(str, lists))
	print("Distances: " + ' '.join(lists))

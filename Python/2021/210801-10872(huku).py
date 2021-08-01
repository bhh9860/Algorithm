def fac(x):
	if x == 1:
		return 1
	elif x == 0:
		return 1
	elif x >= 2:
		return fac(x-1) * x


print(fac(int(input())))

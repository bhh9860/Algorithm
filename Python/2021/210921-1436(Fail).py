n = int(input())
lists = ['0666', '1666', '2666', '3666', '4666', '5666', '6660', '6661', '6662', '6663', '6664', '6665', '6666', '6667', '6668', '6669', '7666', '8666', '9666']

namuji = n % 19 - 1
mok = (n-1) // 19

if mok > 0:
	print(f'{mok}{lists[namuji]}')
else:
	if namuji == 0:
		print(f'{lists[namuji][1:4]}')
	else:
		print(f'{lists[namuji]}');

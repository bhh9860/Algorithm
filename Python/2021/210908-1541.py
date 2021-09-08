a = list(input())
numbersplit = []
symbol = []
for i in a:
	try:
		numbersplit.append(int(i))
		
	except:
		if i == '(' or i == ')':
			continue
		symbol.append(i)
		numbersplit.append('')
		
temp = ''
number = []
for i in numbersplit:
	if i != '':
		temp += str(i)
	else:
		number.append(temp)
		temp = ''
number.append(temp)

number = list(map(int, number))

i = 0
for _ in range(len(symbol)-1):
	if symbol[i] == '-' and symbol[i+1] == '+':
		number.insert(i+1, number[i+1] + number[i+2])
		del number[i+2]
		del number[i+2]
		del symbol[i+1]
	else:
		i += 1

ans = number[0]
del number[0]
for i in range(len(number)):
	if symbol[i] == '-':
		ans -= number[i]
	else:
		ans += number[i]

print(ans)

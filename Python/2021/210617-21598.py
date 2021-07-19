a = list(map(int, input().split()))
b = 0
c = []

for i in a:
  if i > 100:
    c.append('hacker')
    break;
  else:
    b += i
if len(c) > 0:
  print('hacker')

if b > 100 and len(c) == 0:
  print('draw')
elif b < 100 and len(c) == 0:
  print('none')
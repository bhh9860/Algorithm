pibo = [0, 1]
a = 0
b = 1
c = 1
n = int(input())

if n == 2:
    print('1')
    
else:
    for i in range((n-2)//1):
        c = a + b
        a = b + c
        b = c + a
        pibo.extend([c, a, b])

    print(pibo[n])

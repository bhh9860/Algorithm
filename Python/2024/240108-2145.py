while True:
    n = input()
    if int(n) == 0:
        break;
    else:
        n = list(map(int, n))
        k = sum(n)
        while k >= 10:
            n = list(map(int, str(k)))
            k = sum(n)
        print(k)

while True:
    m, f = list(map(int, input().split()))
    if m == 0 and f == 0:
        break;
    else:
        print(m+f)

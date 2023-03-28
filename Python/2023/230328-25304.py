sum_price = int(input())
total_count = int(input())

check_sum_price = 0

for i in range(total_count):
    temp = list(map(int, input().split()))
    check_sum_price += temp[0] * temp[1]


if sum_price == check_sum_price:
    print('Yes')
else:
    print('No')

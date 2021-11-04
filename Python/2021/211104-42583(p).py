def choi(a, b): # 두 수의 최소공배수 리턴함수
    c, d = a, b
    while b != 0:
        r = a % b
        a = b
        b = r

    return c*d//a

ans = [arr[0]]

# 차례대로 arr의 두 원소끼리의 최소공배수를 구해줌
for i in range(1, len(arr)):
    ans.append(arr[i])
    temp = choi(ans[0], ans[1])
    ans.pop()
    ans.pop()
    ans.append(temp)

print(temp)

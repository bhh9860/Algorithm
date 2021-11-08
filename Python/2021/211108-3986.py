ans = 0
for i in range(int(input())):
    words = list(input())
    stack = []

    for j in words:
        if len(stack) == 0:
            stack.append(j)
        else:
            stack.append(j)
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

    if len(stack) == 0:
        ans += 1

print(ans)

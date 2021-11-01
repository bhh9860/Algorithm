def solution(s):
    if len(s) % 2 == 1:
        return 0
    
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    
    if len(stack)== 0:
        return 1
    else:
        return 0

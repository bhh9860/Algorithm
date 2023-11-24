tempList = []
[tempList.append([]) for _ in range(15)]
for i in range(5):
    temp = input()
    for j in range(len(temp)):
        tempList[j].append(temp[j])

ans = ''
for k in range(15):
    ans += ''.join(tempList[k])

print(ans)

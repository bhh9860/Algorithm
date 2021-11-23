from collections import Counter

lists = []
for i in range(int(input())):
    lists.append(input())

dict_lists = dict(Counter(lists))
dict_lists_max = max(dict_lists.values())
ans = []
for key, value in dict_lists.items():
    if value == dict_lists_max:
        ans.append(key)

ans.sort()
print(ans[0])

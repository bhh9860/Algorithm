import collections

not_heard_num, not_saw_num = list(map(int, input().split()))
not_heard = []
not_saw = []

for i in range(not_heard_num):
    not_heard.append(input())

for j in range(not_saw_num):
    not_saw.append(input())

not_heard_saw = not_heard + not_saw

not_heard_saw_cnt = collections.Counter(not_heard_saw) # 딕셔너리 형태로 카운트 해서 리턴


ans = []
for k in not_heard_saw_cnt.keys():
    if not_heard_saw_cnt[k] >= 2: #언급이 2번 이상이면
        ans.append(k)

ans.sort()
print(len(ans))
[print(m) for m in ans]

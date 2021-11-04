def solution(progresses, speeds):
    
    suc = 0 # 배포 성공 인덱스(진척도)
    ans = []
    while suc < len(progresses):
        for i in range(suc, len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0 # 오늘 배포 성공
        for j in range(suc, len(progresses)):
            if progresses[j] >= 100:
                cnt += 1
                suc += 1
            else:
                break

        if cnt >= 1: # 오늘 배포완료된 게 하나라도 있으면
            ans.append(cnt)

    return ans

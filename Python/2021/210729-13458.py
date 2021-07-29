Test_room = int(input())
Tester = list(map(int, input().split()))
Seeter = list(map(int, input().split()))
answer = 0

for i in Tester:
    i -= Seeter[0]
    answer += 1
    if i > 0:
        answer += i // Seeter[1]
        if i%Seeter[1] > 0:
            answer += 1

print(answer)

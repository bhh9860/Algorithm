from collections import Counter

nums = []

for i in range(10):
    nums.append(int(input()))

print(sum(nums) // 10)
[print(a) for a, b in dict(Counter(nums)).items() if max(Counter(nums).values()) == b]

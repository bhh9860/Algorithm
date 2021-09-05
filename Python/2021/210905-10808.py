lists = [0] * 26
word = input()
for i in word:
    lists[ord(i) - 97] += 1

[print(i, end = ' ') for i in lists]

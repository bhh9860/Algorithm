dice = input().split()
dice = list(map(int, dice))
after_dice = list(set(dice))

if len(after_dice) == 3:
    print(max(after_dice) * 100)
elif len(after_dice) == 2:
    for i in after_dice:
        dice.pop(dice.index(i))
    print(1000 + dice[0]*100)
else:
    print(10000 + after_dice[0] * 1000)

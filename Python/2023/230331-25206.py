score = 0
grade = 0
for i in range(20):
    temp = input()
    if temp[-1] == 'P':
        pass
    elif temp[-1] == 'F':
        score += int(temp[-5])
    else:
        score += int(temp[-6])
        j = temp[-2:]
        if j == 'A+':
            grade += int(temp[-6]) * 4.5
        elif j == 'A0':
            grade += int(temp[-6]) * 4.0
        elif j == 'B+':
            grade += int(temp[-6]) * 3.5
        elif j == 'B0':
             grade += int(temp[-6]) * 3.0
        elif j == 'C+':
            grade += int(temp[-6]) * 2.5
        elif j == 'C0':
            grade += int(temp[-6]) * 2.0
        elif j == 'D+':
            grade += int(temp[-6]) * 1.5
        elif j == 'D0':
            grade += int(temp[-6]) * 1.0
            
if score == 0:
    print('0.000000')
else:
    print(round(grade / score, 6))

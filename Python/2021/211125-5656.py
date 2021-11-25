i = 0
while True:
    i += 1
    try:
        print(f'Case {i}: false') if eval(input()) == False else print(f'Case {i}: true')
    except:
        break

#i=1
#while 'E'not in(s:=input()):print(f'Case {i}:',['false','true'][eval(s)]);i+=1
#새로 알게 된 :=, 'E'

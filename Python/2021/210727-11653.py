#def abcd(a):
a= [2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
while count != len(a):
    delete = []
    for i in range(count+1, len(a)-count):
        print(i)
        if a[i] % a[count] == 0:
            delete.append(i)
    for i in delete[-1::-1]:
        del a[i]
    print(delete)
    count += 1
    continue
    #return a

#내일 할래

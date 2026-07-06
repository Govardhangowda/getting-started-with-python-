student={}
print('Welcome to SRVK')
while True:
    print('Enter')
    print('1,Enter a detail')
    print('2.Display detail')
    print('3.Exit')
    i=int(input())
    if i in[1,2,3]:
        if i ==1:
            ini=int(input('No. of details: '))
            for j in range(ini):
                key=input('Key:')
                value=input('Value:')
                student[key]=value
        elif i==2:
            my=list(student.items())
            print(my)
        else:
            print('Goodbye ')
            break
    else:
        print('Invalid Output')

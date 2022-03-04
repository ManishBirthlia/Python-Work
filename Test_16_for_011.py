
num=int(input('\t take any number\n'))
li=[]
i=1
while i>=1 and i<=num:
    li.append(i)
    i=i+2

for i in range(1,num+1):
    print('*',end='')
    if i in li:
        print('*',end='')
    else:
        print(' ',end='')
    print('*')
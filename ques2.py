n=int(input('take any +ve number'))

for i in range (n):
    for j in range (n):
        if j==0 or j==n-1 or i==0 or i==n-1:
            print('*',end='')
        else :
            print(' ',end='')
    print()

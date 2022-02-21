a=int(input('take 1st number:\n'))
b=int(input('take 2nd number:\n'))
c=int(input('take 3rd number:\n'))

if(a<33 or b<33 or c<33) or ((a+b+c)/3<40):
    print('you are fail')
else:
    print('you are pass')
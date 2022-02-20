
a=0
while (a<=19) or (a>20):
    a=int(input('geuss the age of the programer who made this game :\n'))
    if(a<=19):
        print('take higher number')
    if(a>20):
        print('take lower number')
    if(a<=19) or (a>20):
        print('and try again')
    else:
        print('yes you geuss it right')

n=int(input('take any number'))

with open('game.txt','w') as f:
    a=f.write('this is a game and you are playing it ')
    print(a)

    
for i in range(n):
    with open('game.txt','a') as f:
        p=input('write any thing')
        a=f.write(p)
        print(a)

f.close()   
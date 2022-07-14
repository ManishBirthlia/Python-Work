def inch_cm(I):
    c=I*2.54
    return c

def multi(n):
    for i in range (11):
        print(f'{n}*{i}={n*i}')



    
print(multi(4))
print(f'{inch_cm(2)}')
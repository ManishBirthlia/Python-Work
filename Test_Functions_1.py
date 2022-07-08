def greatest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c :
        return b
    else:
        return c

print(f' the greatest number is {greatest(4,3,1)}')
a=int(input('take 1st number:\n'))
b=int(input('take 2nd number:\n'))
c=int(input('take 3rd number:\n'))
d=int(input('take 4th number:\n'))

if (a==b or a==c or a==d or b==c or b==d or d==c):
    print("two or more numbers are same")
if (a>=b and a>=c and a>=d):
    print(a,"is the greatest number")
elif (b>=a and b>=c and b>=d):
    print(b,"is the greatest number")
elif (c>=b and c>=a and c>=d):
    print(c,"is the greatest number")
else:
    print(d,"is the greatest number")
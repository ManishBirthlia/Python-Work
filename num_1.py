n=int(input('take any number\n'))
a=n%2
L=int((n-a)/2)
li=[]
if a==1:
        li.append(a)
while L>=1:
    a=L%2
    L=int((L-a)/2)
    if a==1:
        li.append(a)
print(f'''there are total "{len(li)}" 1's in binary number you entered''')
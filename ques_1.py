n=int(input('take any number\n'))
a=n%2
L=int((n-a)/2)
li=[a]
while L>=1:
    a=L%2
    L=int((L-a)/2)
    li.append(a)
li.reverse()
for i in range(len(li)):
    print(li[i],end='')
num=int(input('take an number \n'))
li=[]
i=1
while i>=1 and i<=num:
    li.append(i)
    i=i+1
else:
    print(f"sum of all natural numbers upto {num}--'{li}' is:",sum(li))

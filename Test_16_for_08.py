#factorial
num=int(input('\t take any number\n'))

a=1
for i in range(1,num+1):
    a=a*i

print(f'\t factorial of number {num} is',a)
print(f'\t {num}! =',a)
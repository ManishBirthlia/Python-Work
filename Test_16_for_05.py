num=int(input('take an number which you think is prime \n'))
for i in range(2,num):
    if (num%i==0):
        print(f'your number {num} is not a prime number because of number {i}')
        break
else:
    print(f'your number {num} is a prime number')
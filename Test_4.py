from asyncore import loop
from tracemalloc import start

from pip import main
# taking input from user
a=input("Input :")
print(type(a))
# this is small function i made to find value at given index
# x=0
# print(a[x])
# x+=1
# print(a[x])
# x+=1
# print(a[x])
# x+=1
# print(a[x])
# x+=1
# print(a[x])
# x+=1
# print(a[x])
# x+=1
x=int(input('take any number from 0 onward '))
print(a[x])
print(a[2:x])# here x in excluded or simply not taken in python
print(a[x:10])
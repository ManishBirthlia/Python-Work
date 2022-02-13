from asyncore import loop
from tracemalloc import start

from pip import main

a=input("Input :")
print(type(a))
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
print(a[2:x])
print(a[x:10])
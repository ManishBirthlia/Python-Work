from re import A


t=(7,2,4,3,5,6,1,7,8,43,6)
print(type(t))
# print(t)
# t[0]=100 #this will throw some error
# print(t)
a=int(input("index of number u want to find :\n"))
print(t[a])
print(t[-4:])
# tuple methods
print(t.index(6))
print(t.count(6))

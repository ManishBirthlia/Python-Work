                                                         ###  for list
a=[] #empty list
print(type(a))
a=[1]
b=[1,]
print(type(a))
print(type(b))
print(a)
print(b)
# ultered
a=[3,2,'manish',float ,int]
print(a)
print(type(a[3:]))
# change variables
a[3]=int
print(a)
b=[1,"1",[1,2],(1,2),{1,2,3,1,2},{"name":'manish'}]
print(b)

                                                      # for tuple

a=() #empty tuple
print(type(a))
a=(1)
b=(1,)
print(type(a))
print(type(b))
print(a)
print(b)
# ultered
a=(3,2,'manish',float ,int)
print(a)
print(type(a[3:]))
# change variables
# a[3]=int # gives error
b=(1,"1",(1,2),[1,2],{1,2,3,1,2},{"name":'manish'})
print(b)

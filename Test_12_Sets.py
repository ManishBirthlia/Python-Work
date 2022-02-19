a={1,2,3,4,5,1,2}
print(type(a))
print(a)
b=int(input("type to add in the set:\n"))
a.add(b)
a.pop()

a.remove(2)
a.add((1,2,3))
print(len(a))
print(a)
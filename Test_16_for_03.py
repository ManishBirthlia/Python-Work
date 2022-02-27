# for loop with break statement
for i in range(1,8):
    
    if i==6:
        break
    print(i)
else:
    print('this else is inside for loop')
print('\t\t')
# for loop with continue
for i in range(1,8):
    if i==6:
        continue #it will skip 6 and rest will print
    print(i)
else:
    print('this else is inside for loop')

# pass statement
for i in range(1,8):
    pass # this will give no error and act as do nothing function

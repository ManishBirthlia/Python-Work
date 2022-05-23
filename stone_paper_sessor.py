import random
li=['stone','paper','sessor']
a=input('stone,paper and sessor take any one\n')

if a==li[0] or li[1] or li[2] :
    print(random.choice(li))
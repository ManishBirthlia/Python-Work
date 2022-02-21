marks=int(input('enter your marks for grade :\n'))

if(marks<=100 and marks>=90):
    print(marks,'out of 100, your grade is Ex')
elif(marks>=80):
    print(marks,'out of 100, your grade is A')
elif(marks>=70):
    print(marks,'out of 100, your grade is B')
elif(marks>=60):
    print(marks,'out of 100, your grade is C')
elif(marks>=50):
    print(marks,'out of 100, your grade is D')
else:
    print(marks,'out of 100, your grade is F')
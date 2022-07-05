
p=open('sample.txt','r')
data=p.read()
print(data)
data.find('twinkle')
print(data.count('twinkle'))
p.close

# p=open('sample.txt','w')
# data2=p.write('hlo who are you ')
# print(data2)
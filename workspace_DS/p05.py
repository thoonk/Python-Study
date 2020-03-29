a = [1,2,3,4,5]
b= 'abcde'
c= []
for i,j in zip(a,b):
    c.append((i,j))

print(c)
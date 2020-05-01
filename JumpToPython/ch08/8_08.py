#역순 저장

f = open('abc.txt', 'r')
line = f.readlines()
f.close()

line.reverse()

f=open('abc.txt', 'w')
for i in line:
    i = i.strip()
    f.write(i)
    f.write('\n')
f.close()
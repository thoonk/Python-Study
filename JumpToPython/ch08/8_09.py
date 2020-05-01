#평균값 구하기

f = open('sample.txt', 'r')
line = f.readlines()
f.close()

sum = 0
for i in line:
    #num = int(i)
    sum += int(i)

avg = sum / len(line)

f = open('result.txt', 'w')
f.write(str(avg))
f.close()
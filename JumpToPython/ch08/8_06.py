#입력한 숫자의 총합 구하기

n=input("숫자 입력: ")
num = n.split(",")
sum = 0
for i in num:
    sum += int(i)
print(sum)
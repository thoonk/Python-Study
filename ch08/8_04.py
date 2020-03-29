#리스트 총합 구하기

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

sum = 0
while A:
    num = A.pop()
    if num >= 50:
        sum += num
print(sum)
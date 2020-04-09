# 평균 점수
i, sum = 0, 0

for i in range(5):
    a = int(input())
    if a >= 40:
        sum += a
    else: sum += 40

print(round(sum/5))


# 세 정수 중에 중간값 찾기
a, b, c = map(int, input().split())
if a >= b:
    if b >= c:
        median = b
    elif a <= c:
        median = a
    else:
        median = c
elif c < a:
    median = a
elif b > c:
    median = c
else:
    median = b
print(median)
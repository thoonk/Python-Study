# 속이 빈 직사각형 별 찍기

a, b = map(int, input().split())

for i in range(a):
    print("*")
print()
for i in range(1, i <= b-2):
    print("*")
    for j in range(1, j <= a-2):
        print(" ")
    print("*")
    print()
for i in range(1, a):
    print("*")



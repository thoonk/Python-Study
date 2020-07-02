# 달팽이 배열
n = int(input())

arr = [[0] * n for m in range(n)]
row = 0
col = -1
value = 0
inc = 1
while True:
    for i in range(1, n+1):
        value += 1
        col += inc
        arr[row][col] = value
    n -= 1
    if n <= 0:
        break
    for j in range(1, n+1):
        value += 1
        row += inc
        arr[row][col] = value

    inc *= -1

for k in range(len(arr)):
    for l in range(len(arr[0])):
        print('%3d' % arr[k][l], end='')
    print()


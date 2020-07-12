# 평면 좌표 정렬 x기준

n = int(input())
lst = []
for i in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))

sortedList = sorted(lst, key=lambda l: (l[0], l[1]))
for x, y in sortedList:
    print(str(x) + ' ' + str(y))
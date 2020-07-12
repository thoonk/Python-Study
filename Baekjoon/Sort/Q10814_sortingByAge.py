# 나이순 정렬
from sys import stdin

n = int(stdin.readline())
lst = []
for _ in range(n):
    age, name = map(str, stdin.readline().split())
    age = int(age)
    lst.append((age, name))

sort_lst = sorted(lst, key=lambda l: (l[0]))

for i in sort_lst:
    print(i[0], i[1])

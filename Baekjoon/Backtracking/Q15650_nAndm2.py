# 조합
from sys import stdin
n, m = map(int, stdin.readline().split())

visited = [False] * (n + 1)
lst = [0] * m


def explode(depth, n, m):
    if depth == m:
        for i in range(m):
            print(lst[i], end=' ')
        print()

        return
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        lst[depth] = i
        explode(depth + 1, n, m)

        for j in range(i+1, n):
            visited[j] = False

explode(0, n, m)


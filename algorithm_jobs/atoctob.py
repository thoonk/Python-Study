# a에서 c까지 증가 후 b까지 감소

a, c, b = map(int, input().split())

def atoctob(a, c, b):
    for i in range(a, c + 1):
        print(i, end=' ')

    for j in range(c - 1, b - 1, -1):
        print(j, end=' ')


atoctob(a, c, b)

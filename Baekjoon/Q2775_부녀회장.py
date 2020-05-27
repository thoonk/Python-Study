T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())

    inhabitants = [j for j in range(1, n+1)]
    for l in range(k):
        for m in range(1, n):
            inhabitants[m] += inhabitants[m-1]
    print(inhabitants[n-1])


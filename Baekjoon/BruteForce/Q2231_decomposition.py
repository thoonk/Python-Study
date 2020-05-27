n = int(input())
result = 0
for i in range(1,n+1):
    num_lst = list(map(int, str(i)))
    result = i + sum(num_lst)

    if n == result:
        print(i)
        break
    if i == n:
        print(0)

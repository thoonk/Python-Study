#한수

N = int(input())

def func(N: int):
    cnt = 0
    for i in range(1, N+1):
        if i < 100:
            cnt += 1
        else:
            lst = list(map(int, str(i)))
            if lst[0] - lst[1] == lst[1] - lst[2]:
                cnt += 1
    print(cnt)

func(N)
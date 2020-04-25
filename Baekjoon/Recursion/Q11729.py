# 하노이탑

def hanoi(n, start, via, to):
    if n==1:
        print(start, to)
    else:
        hanoi(n-1, start, to, via)
        print(start, to)
        hanoi(n-1, via, start, to)

num = int(input())
cnt = 1
for i in range(num-1):
    cnt = cnt*2 + 1
print(cnt)
hanoi(num, 1, 2, 3)
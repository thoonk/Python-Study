#별 찍기-13

n = int(input())
for i in range(1, 2*n):
    if(i <= n):
        star = i
    else:
        star = n*2 - i
    print(star*"*")

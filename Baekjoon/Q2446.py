#별 찍기-9

n = int(input())

for i in range(1, 2*n):
    if i < n:
        star = 2*(n-i+1) - 1
        space = ((2*n-1) - star)//2
    else:
        star = 2*(i-n) + 1
        space = ((2*n-1) - star)//2
    print(space*' ' + star*"*")

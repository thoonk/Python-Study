#별 찍기-21

n = int(input())
for i in range(1, n+1):

    if n%2==1:
        upStar = i
        downStar = i-1
    else:
        upStar = i
        downStar = i
    print(upStar*"*" + " ")
    print(" " + downStar*"*" + " ")
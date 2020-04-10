#평균은 넘겠지
test_num = int(input())
for i in range(test_num):
    score = 0
    cnt = 0
    stu = [int(x) for x in input().strip().split(' ')]
    score = sum(stu[1:])
    avg = score / stu[0]
    for j in stu[1:]:
        if j > avg:
            cnt += 1
    print(str("%0.3f"%round(cnt/stu[0]*100, 3)) + '%')

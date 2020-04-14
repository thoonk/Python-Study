#문자열 반복

test_num = int(input())
for i in range(test_num):
    re_num, str = input().split(' ')
    lst = list(str)
    for re in lst:
        print(re*int(re_num), end='')
    print()


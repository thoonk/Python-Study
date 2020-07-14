n = int(input())
nums= list(map(int, input().split()))
sort_nums = sorted(nums)
for i in sort_nums:
    print(i, end=' ')

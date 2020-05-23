nums = map(int, input().split())
verif = 0
for num in nums:
    verif += (num**2)
print(verif%10)

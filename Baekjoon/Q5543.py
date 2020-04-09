# 제일 싼 햄버거 세트 가격 구하기

lst = []
for i in range(5):
    a = int(input())
    lst.append(a)

hamburger = min(lst[:3])
beverage = min(lst[3:])
print(hamburger + beverage - 50)

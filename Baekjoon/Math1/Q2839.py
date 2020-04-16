#설탕 배달

n = int(input())
bag = 0

while n > 0:
    if n % 5 != 0:
        n -= 3
        if n < 0:
            bag = -1
            break
        bag += 1
    elif n % 5 == 0:
        n -= 5
        bag += 1
    elif n % 5 != 0 and n % 3 != 0:
        bag = -1

print(bag)


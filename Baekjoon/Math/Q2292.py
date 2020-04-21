#벌집

n = int(input())
last = 1
tolerance = 1
num = 1
if n == 1:
    print(n)
else:
    while True:
        last += tolerance * 6
        tolerance += 1
        num += 1
        if n <= last:
            break
    print(num)


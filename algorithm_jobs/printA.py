n = int(input())
d = n * 2
left = n - 1
right = n - 1
for i in range(n):
    for j in range(d):
        if i == 0:
            if j == n - 1:
                print('*', end="")
            else:
                print(' ', end="")

        elif i == n // 2:
            if left <= j <= right:
                print('*', end="")
            else:
                print(' ', end="")

        else:
            if j == left or j == right:
                print('*', end="")
            else:
                print(' ', end="")
    left -= 1
    right += 1
    print()

<<<<<<< HEAD
n = int(input())
d = n * 2
left = n - 1
right = n - 1
for i in range(n):
    for j in range(d):
=======
# A 모양 별 찍기
n = int(input())
col = n * 2
left = n - 1
right = n - 1
for i in range(n):
    for j in range(col):
>>>>>>> 572b31e5addc0c1afd1b81ae2078df127eb48386
        if i == 0:
            if j == n - 1:
                print('*', end="")
            else:
                print(' ', end="")
<<<<<<< HEAD

        elif i == n // 2:
=======
        elif i == n//2:
>>>>>>> 572b31e5addc0c1afd1b81ae2078df127eb48386
            if left <= j <= right:
                print('*', end="")
            else:
                print(' ', end="")
<<<<<<< HEAD

=======
>>>>>>> 572b31e5addc0c1afd1b81ae2078df127eb48386
        else:
            if j == left or j == right:
                print('*', end="")
            else:
                print(' ', end="")
    left -= 1
    right += 1
    print()
<<<<<<< HEAD
=======

>>>>>>> 572b31e5addc0c1afd1b81ae2078df127eb48386

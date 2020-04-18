#분수찾기

n = int(input())
step, acc = 1, 1
while step + acc <= n:
    acc += step
    step += 1

index = n - acc
x, y = index + 1, step - index
if step % 2 == 0:
    print('{}/{}'.format(x, y))
else:
    print('{}/{}'.format(y, x))


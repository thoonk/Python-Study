#손익분기점

static, variable, price = map(int, input().split(' '))
if variable < price:
    print(int(static/(price - variable)) + 1)
else:
    print(-1)

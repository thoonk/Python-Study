#상수 로꾸꺼

x, y = input().split(' ')
compX = x[::-1]
compY = y[::-1]
if compX > compY:
    print(compX)
elif compX < compY:
    print(compY)

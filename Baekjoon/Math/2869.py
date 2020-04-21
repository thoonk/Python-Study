#달팽이는 올라가고 싶다

a, b, v = map(int, input().split())
day = (v-b)/(a-b) # a*k - b*(k-1) >= v
if day == int(day):
    print(int(day))
else:
    print(int(day)+1)

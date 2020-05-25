while True:
    tri = list(map(int, input().split()))
    m = max(tri)
    if sum(tri)==0: break
    tri.remove(m)
    if tri[0]**2 + tri[1]**2 == m**2:
        print('right')
    else:
        print('wrong')

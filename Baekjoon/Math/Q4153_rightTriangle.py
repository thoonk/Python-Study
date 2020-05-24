while True:
    input = list(map(int, input().split()))
    m = max(input)
    if sum(input)==0: break
    input.remove(m)
    if input[0]**2 + input[1]**2 == m**2:
        print('right')
    else:
        print('wrong')

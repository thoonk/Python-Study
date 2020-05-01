def getTotalPage(m, n):
    if m%n == 0:
        return m//n
    else:
        return m//n+1


print(getTotalPage(3,10))
print(getTotalPage(10,10))
print(getTotalPage(13,10))
print(getTotalPage(20,10))
print(getTotalPage(23,10))
print(getTotalPage(30,10))
print(getTotalPage(33,10))
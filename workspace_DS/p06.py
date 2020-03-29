def avg_num(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

r = avg_num(1,2,3,4,5)
print(r)
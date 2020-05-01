def cal_avg(*args):
    result=0
    for i in args:
        result = result + i
    return result / len(args)

print(cal_avg(1,2,3,4,5))
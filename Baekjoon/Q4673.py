#셀프 넘버

def self_num():
    num = set(range(1, 10001))
    num_set=set()
    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        num_set.add(i)
    result = num - num_set
    for n in sorted(result):
       print(n)

self_num()






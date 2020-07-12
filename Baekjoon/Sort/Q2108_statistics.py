# statistics
from sys import stdin
from collections import Counter


def arith_average(sl):
    return round(sum(sl) / len(sl))


def median(sl):
    mid = len(sl) // 2
    if len(sl) % 2 == 0:
        return (sl[mid - 1] + sl[mid]) / 2
    else:
        return sl[mid]


def best(sl):
    cnt = Counter(sl)
    if len(sl) == 1:
        return sl[0]
    most = cnt.most_common(2)
    return most[1][0] if most[0][1] == most[1][1] else most[0][0]


def max_min_range(sl):
    return sl[n - 1] - sl[0]


if __name__ == "__main__":
    n = int(stdin.readline())
    lst = [int(stdin.readline()) for _ in range(n)]
    sort_lst = sorted(lst)

    print(arith_average(sort_lst))
    print(median(sort_lst))
    print(best(sort_lst))
    print(max_min_range(sort_lst))

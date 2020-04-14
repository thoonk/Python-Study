from typing import List

#평균
def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

#중심값
def median(v:List[float])->float:
    sortedList = sorted(v)
    listLen = len(v)
    index = (listLen - 1) // 2
    if (listLen % 2):
        return sortedList[index]
    else:
        return (sortedList[index] + sortedList[index + 1]) / 2.0

assert median([1,10,2,9,5])==5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

#분위
def quantile(xs: List[float], p:float) -> float:
    p_index = int (p*len(xs))
    return sorted(xs)[p_index]

#최빈값
from collections import Counter
from typing import List
num_friends = [1,2,3,4,5,6,7,8,1,1,6,6]
def mode(x: List[float]) -> List[float]:
    cnt = Counter(num_friends)
    m = max(cnt.values())
    res = [i for i, c in cnt.items() if c == m]
    return res

print(mode(num_friends))
assert set(mode(num_friends)) == {1, 6}

#산포도(dispersion)

from scratch.linear_algebra import sum_of_squares

def de_mean(xs: List[float]) -> List[float]:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    assert len(xs) >= 2
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations)

import math

def standard_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))

def interquartile_range(xs: List[float]) -> float:
    return quantile(xs, 0.75) - quantile(xs, 0.25)

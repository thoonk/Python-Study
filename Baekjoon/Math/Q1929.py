# 소수 구하기
import math

def isPrime(num):
    if num == 1:
        return False
    n2 = int(math.sqrt(num))
    for i in range(2, n2+1):
        if num % i == 0:
            return False
    return True

a, b = map(int, input().split())

for j in range(a, b+1):
    if isPrime(j):
        print(j)


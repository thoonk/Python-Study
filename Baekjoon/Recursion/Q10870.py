# 피보나치 수 5

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

num = int(input())
print(fibo(num))

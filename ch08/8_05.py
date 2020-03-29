#피보나치 함수

def fib(n):
    if n==0: return 0
    if n==1: return 1
    return fib(n-2)+fib(n-1)

for i in range(8):
    print(fib(i))
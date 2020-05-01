#한 줄 구구단

def multiple(n):
    for i in range(1, 10):
        print(n*i, end = ' ')

n = input("구구단을 출력할 숫자를 입력하세요(2~9): ")
multiple(int(n))

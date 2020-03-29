#오류와 예외 처리

result = 0

try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)

# result의 실행결과는 7로 예측이 되고 그 이유는 try문에서 제일 첫 번째인 [1,2,3][3] 에서 인덱스 에러가 발생하기 때문에 except로
#빠지고 3이 더해지며 finally에서 4가 더해져 result는 7이 된다.
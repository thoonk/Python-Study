#총 단어의 개수 출력

s = input()
lst = list(s.split())
cnt = 0
for char in lst:
    cnt += 1
print(cnt)
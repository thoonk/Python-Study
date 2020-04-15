#그룹 단어 체커

n = int(input())
cnt = 0

def groupChecker(s):
    for i in range(len(s)):
        check = ['F', 'F']
        for j in range(i+1, len(s)):
            if s[i] != s[j]: #연속으로 나오지 않는 경우
                check[0] = 'T'
            if s[i] == s[j] and check[0] == 'T': #연속으로 나오지 않고 나중에 같은 문자가 나오는 경우
                check[1] = 'T'
            if check[0] == 'T' and check[1] == 'T':
                return 0
    return 1

for i in range(n):
    cnt += groupChecker(input())
print(cnt)


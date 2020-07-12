# 단어 정렬

lst = []
n = int(input())
for i in range(n):
    s = input()
    s_len = len(s)
    lst.append((s, s_len))

lst = list(set(lst))  # deduplication

lst.sort(key=lambda s: (s[1], s[0])) # sorting by len first & dictionary order

for word in lst:
    print(word[0])
#단어 공부

s = input().upper()
lst = list(set(s))
cnt_lst = []
for char in lst:
    cnt = s.count(char)
    cnt_lst.append(cnt)
if(cnt_lst.count(max(cnt_lst)) >= 2):
    print("?")
else:
    print(lst[cnt_lst.index(max(cnt_lst))])


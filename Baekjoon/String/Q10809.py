#알파벳 찾기

from string import ascii_lowercase

alpha_list = list(ascii_lowercase)
s = input()
lst = list(s)
result=[]
for char in alpha_list:
    for i in range(len(lst)):
        if char == lst[i]:
            result.append(i)
            break
        elif i < len(lst)-1:
            continue
        else:
            result.append(-1)
for i in result:
    print(i, end=' ')

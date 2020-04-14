#크로아티아 알파벳

s = input()
alph_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alph_lst:
    s = s.replace(i, 'o')
print(len(s))
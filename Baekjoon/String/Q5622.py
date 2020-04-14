#다이얼

w = input()
alpha_lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for i in range(len(w)):
    for j in alpha_lst:
        if w[i] in j:
            time += alpha_lst.index(j) + 3
print(time)

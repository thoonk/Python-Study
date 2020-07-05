from string import ascii_lowercase

a, b = map(int, input().split())
alpha_lst = list(ascii_lowercase)

ref_a = []
for i in range(a):
    ref_a.append(alpha_lst[i])
print(ref_a)


def permutation(lst, n):
    result = []
    if n > len(lst):
        return result
    if n == 1:
        for l in lst:
            result.append(l)
    elif n > 1:
        for i in range(len(lst)):
            temp = [j for j in lst]
            temp.remove(lst[i])
            for k in permutation(temp, n - 1):
                result.append(lst[i] + k)

    return result


ret = permutation(ref_a, b)
print(len(ret))
print(ret)

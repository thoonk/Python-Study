#문자열 압축하기

input = "aaabbcccccca"

def str_comp(s):
    next = ""
    output = ""
    cnt = 0

    for i in s:
        if next != i:
            next = i
            if cnt:
                output += str(cnt)
            output += i
            cnt = 1
        else:
            cnt += 1
    if cnt: output += str(cnt)
    print(output)

str_comp(input)


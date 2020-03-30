#0~9까지의 모든 숫자를 한 번씩만 사용하여 모든 숫자가 다 있는지 확인

input = "0123456789 01234 01234567890 6789012345 012322456789"

def check_duplicate(n):
    check = []
    for i in n:
        if i not in check:
            check.append(i)
        else:
            return False
    if len(check) == 10:
        return True
    else:
        return False

print(check_duplicate("0123456789"))
print(check_duplicate("01234"))
print(check_duplicate("01234567890"))
print(check_duplicate("6789012345"))
print(check_duplicate("012322456789"))

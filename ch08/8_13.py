#연속되는 수가 홀수면 사이에 - 짝수면 사이에 * 삽입

num = "4546793"

def odd_even(num):
    toIntList = list(map(int, num))
    output = []

    for i, n in enumerate(toIntList):
        output.append(str(n))
        if i < len(toIntList)-1:
            if n % 2 == 1 and toIntList[i+1] % 2 == 1:
                output.append("-")
            elif n % 2 == 0 and toIntList[i+1] % 2 == 0:
                output.append("*")
    print("".join(output))

odd_even(num)
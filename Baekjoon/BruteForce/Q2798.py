# 블랙잭

n, m = map(int, input().split())
card = list(map(int, input().split()))
result = 0

for i in range(len(card)-2):
    for j in range(i+1 ,len(card) - 1):
        for k in range(j+1, len(card)):
            sum = card[i] + card[j] + card[k]
            if result < sum <= m:
                result = sum
            elif sum == m:
                result = sum
                break
print(result)


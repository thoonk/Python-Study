import random

result =[]
while len(result) < 6:
    num=random.randint(1,45)
    if num not in result:
        result.append(num)

print(result)
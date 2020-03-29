#사칙연산 계산기

class Calculator:
    def __init__(self, list):
        self.list = list

    def sum(self):
        result = 0
        for i in self.list:
            result += i
        return result

    def avg(self):
        sum = self.sum()
        return sum / len(self.list)

cal = Calculator([1,2,3,4,5])
print(cal.sum())
print(cal.avg())
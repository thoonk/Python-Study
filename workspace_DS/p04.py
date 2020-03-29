class Calculator:
    cnt = 0
    def __init__(self):
        self.value = 0
        Calculator.cnt += 1
    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val;



cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

c1 = Calculator()
c2 = Calculator()
print(Calculator.cnt)
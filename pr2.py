#1
import math
def funcZ(m):
    if (m >= 0):
        return math.sqrt(m) + 10
    else:
        print("Не вдається знайти корінь з відємного числа")
        return
m = float(input("Введіть число m: "))
print("Відповідь: " ,funcZ(m))


def AvgEven(x, y):
    sum = 0
    num = 0
    step = 1 if x < y else -1
    for i in range(x, y+step, step):
        if (i % 2 == 0):
            sum += i
            num += 1
    return sum/num

x = int(input("Введіть число x: "))
y = int(input("Введіть число y: "))
print("Середнє арифметичне парних чисел від x до y: ",AvgEven(x,y))

#2

from average import AverageOfEvenBetween
print("З підключеним модулем")
x = int(input("Введіть число x: "))
y = int(input("Введіть число y: "))
print("Середнє арифметичне парних чисел від x до y: ",AverageOfEvenBetween(x,y))



def AverageOfEvenBetween(x, y):
    sum = 0
    num = 0
    step = 1 if x < y else -1
    for i in range(x, y+step, step):
        if (i % 2 == 0):
            sum += i
            num += 1
    return sum/num

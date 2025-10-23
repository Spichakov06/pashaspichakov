#1
a = int(input("Введіть число а від 1 до 100 "))
while (a < 1 or a > 100):
    a = int(input("Число а введено некоректно, введіть а від 1 до 100 "))
b = int(input("Введіть число b від 1 до 100 "))
while (b < 1 or b > 100):
    b = int(input("Число b введено некоректно, введіть b від 1 до 100 "))

if (a < b):
    X = (b/a) - 1
elif (a > b):
    X = (a-235)/b
else:
    X = -295

print("Відповідь: ", X)

#2
time = 2
grow = 3
step = 12
numb = 1

for i in range(0, 49, step):
    if (i != 0):
        devides = i/time
        res = numb * grow ** devides
        print(i, " hours    |   ", res)


#3
n = int(input("Введи число від 1 до 9 (межі не включно) "))
while (n < 1 or n > 9):
    n = int(input("Число n введено некоректно, введіть n від 1 до 9 "))

for i in range(n):
    print()
    for j in range(n, 0, -1):
        k = j
        if (j-1 <= i):
            print(j, end = " ")
        else:
            print(" ", end= " ")
#1
n = int(input("Введі кількість елементів масиву "))
while (n <= 0):
    n = int(input("Введі коректну кількість елементів масиву (> 0) "))

arr = []
for i in range(n):
    arr.append(float(input("Введіть числовий елемент ")))

el = min(arr)

for a in arr:
    if (a < 0 and a > el):
        el = a

if (el < 0):
    print("Найбільший серед відємних елементів: ", el)
else:
    print("Відємних елементів в масиві немає")

#2
n = 7
arr = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        arr[i][j] = j-i

for i in range(n):
    print()
    for j in range(n):
        if(arr[i][j] >= 0):
            print("",arr[i][j], end=" ")
        else:
            print(arr[i][j], end=" ")
print()

#3
n = int(input("Введі кількість елементів масиву "))
while (n <= 0):
    n = int(input("Введі коректну кількість елементів масиву (> 0) "))

arr = []
for i in range(n):
    arr.append(int(input("Введіть числовий елемент ")))

def MakeNewList(array):
    new_list = list(array)
    for i in range(len(new_list)):
        if (new_list[i] % 2 == 0):
            new_list.append(new_list[i])
    return new_list

arr = MakeNewList(arr)
print(arr)

#4
n = int(input("Введі кількість елементів масиву "))
while (n <= 0):
    n = int(input("Введі коректну кількість елементів масиву (> 0) "))

arr = []
for i in range(n):
    arr.append(int(input("Введіть числовий елемент ")))

def NewList(prev_list):
    new_list = []
    prev_list = list(prev_list)
    for i in range(len(prev_list)):
        if (prev_list.count(prev_list[i]) > 1 and (prev_list[i] not in new_list)):
            new_list.append(prev_list[i])
    return new_list

arr = NewList(arr)
print(arr)

#5
import math
X = {i for i in range(8,23)}
y = []
Z = {i for i in range(8,23)}

for el in X:
    isPrime = True
    if (el == 1):
        y.append(el)
    elif (el % 2 == 0 or el % 3 == 0):
        isPrime = False
    for i in range(3, round(math.sqrt(el)) + 1):
        if (el % i == 0):
            isPrime = False
    if (isPrime):
        y.append(el)

Y = set(y)

print("X: ", X)
print("Y: ", Y)
print("Z: ", Z)
#1
word = input("Введи будь-яке слово або речення (хоча б 2 літери): ")
if (len(word) >= 2):
    print("Друга літера слова: ", word[1])
    print("Передостання літера слова: ", word[-2])
else:
    print("Занадто коротке слово для цього завдання")

#2
word = input("Введи будь-яке слово або речення: ")  
for i in range(1, len(word)):
    if (i >= len(word)):
        break
    while (word[i-1] == word[i]):
        word = word[:i-1] + word[i:]
        if (i >= len(word)):
            break
print("Після видалення всіх однакових символів поспіль слово виглядає так: ", word)

#3
word = input("Введи будь-яке слово або речення: ")
word = word.replace("b", "c")
print(word)
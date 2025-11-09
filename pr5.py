
students = {
    "Іваненко": [10, 9, 8, 11, 12, 10, 9, 8, 10, 12],
    "Петренко": [8, 7, 9, 10, 9, 8, 9, 7, 8, 9],
    "Сидоренко": [11, 10, 12, 10, 11, 12, 11, 12, 10, 12],
    "Коваленко": [7, 6, 8, 9, 7, 8, 9, 6, 8, 7],
    "Бондаренко": [9, 9, 9, 10, 9, 10, 9, 10, 9, 9],
    "Мельник": [12, 12, 11, 12, 12, 11, 12, 12, 11, 12],
    "Гриценко": [8, 8, 9, 9, 10, 9, 9, 8, 9, 9],
    "Шевченко": [6, 7, 8, 7, 6, 8, 7, 7, 6, 7],
    "Олійник": [9, 10, 9, 10, 11, 10, 9, 10, 10, 10],
    "Романенко": [11, 11, 10, 12, 11, 11, 12, 12, 10, 11]
}

def output(students):
    for name, grades in students.items():
        print(f"{name}: {grades} (сума = {sum(grades)})")

def add_student(students):
    try:
        name = input("Введіть прізвище учня: ").strip()
        if name in students:
            print("Такий учень вже є у списку.")
            return
        grades = []
        for i in range(10):
            while True:
                try:
                    mark = int(input(f"Введіть оцінку {i+1}-го предмету (1-12): "))
                    if 1<=mark <= 12:
                        grades.append(mark)
                        break
                    else:
                        print("Оцінка має бути від 1 до 12.")
                except ValueError:
                    print("Введено некоректне значення.")
        students[name] = grades
        print("Учня додано!")
    except Exception as e:
        print("Помилка при додаванні:", e)

def delete_student(students):
    try:
        name = input("Введіть прізвище учня для видалення: ").strip()
        del students[name]
        print("Учня видалено.")
    except KeyError:
        print("Такого учня немає у списку.")
    except Exception as e:
        print("Помилка при видаленні:", e)

def sort_students(students):
    for name in sorted(students.keys()):
        print(f"{name}: {students[name]}")

def best_and_worst(students):
    if not students:
        print("Список учнів порожній.")
        return
    total_scores = {name: sum(grades) for name, grades in students.items()}
    best=max(total_scores, key=total_scores.get)
    worst=min(total_scores, key=total_scores.get)
    print(f"Учень з найбільшою сумою оцінок: {best} ({total_scores[best]})")
    print(f"Учень з найменшою сумою оцінок: {worst} ({total_scores[worst]})")

def menu():
    while True:
        print("\nОберіть дію:")
        print("1 - Вивести всіх учнів і оцінки")
        print("2 - Додати учня")
        print("3 - Видалити учня")
        print("4 - Вивести учнів за алфавітом")
        print("5 - Знайти учня з найбільшою та найменшою сумою оцінок")
        print("0 - Вихід")
        choice = input("Ваш вибір: ")
        if choice == "1":
            output(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice =="4":
            sort_students(students)
        elif choice =="5":
            best_and_worst(students)
        elif choice =="0":
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

menu()

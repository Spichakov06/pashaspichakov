import matplotlib.pyplot as plt
import numpy as np
import csv

#1
def task1_plot_function():
    x = np.linspace(0.1, 10, 500)
    y = np.cos(x ** 2) / x
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color='green', linewidth=2, linestyle='-', label='y = cos(x²)/x')
    plt.title("Графік функції y = cos(x²)/x")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

#2
def task2_visualization_from_csv(filename):
    years = []
    usa_values = []
    ukraine_values = []

    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)
        usa_row = next(reader)
        ukr_row = next(reader)
        years = [year for year in range(2004, 2025)]
        usa_values = [float(v) for v in usa_row[4:25]]
        ukraine_values = [float(v) for v in ukr_row[4:25]]

    plt.figure(figsize=(8, 5))
    plt.plot(years, usa_values, color='blue', label='United States')
    plt.plot(years, ukraine_values, color='orange', label='Ukraine')
    plt.title("Population ages 30–34, male (% of male population)")
    plt.xlabel("Year")
    plt.ylabel("% of male population")
    plt.legend()
    plt.grid(True)
    plt.show()

    country = input("Введіть назву країни для побудови стовпчастої діаграми (USA або Ukraine): ").strip().lower()

    if country == "usa":
        plt.bar(years, usa_values, color='blue')
        plt.title("Population ages 30–34, male (% of male population) — USA")
    elif country == "ukraine":
        plt.bar(years, ukraine_values, color='orange')
        plt.title("Population ages 30–34, male (% of male population) — Ukraine")
    else:
        print("Невідома країна. Використовується Україна за замовчуванням.")
        plt.bar(years, ukraine_values, color='orange')
        plt.title("Population ages 30–34, male (% of male population) — Ukraine")

    plt.xlabel("Year")
    plt.ylabel("% of male population")
    plt.grid(True, axis='y')
    plt.show()

#3
def task3_pie_chart():
    labels = ['Вугілля', 'Нафта', 'Газ', 'Відновлювані джерела', 'Атомна енергія']
    data = [27, 31, 23, 12, 7]
    colors = ['dimgray', 'orange', 'skyblue', 'lightgreen', 'violet']

    fig, ax = plt.subplots(figsize=(7, 6))
    wedges, texts, autotexts = ax.pie(
        data,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        shadow=True,
        explode=[0, 0.05, 0, 0.1, 0],
        textprops={'color': 'black', 'fontsize': 10}
    )

    ax.legend(
        wedges,
        labels,
        title="Джерела енергії",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1)
    )

    plt.setp(autotexts, size=10, weight="bold")
    ax.set_title("Світова структура енергоспоживання", fontsize=14, pad=20)
    plt.show()

if __name__ == "__main__":
    while True:
        print("\nОберіть завдання для виконання:")
        print("1 — Побудова графіка функції y = cos(x²)/x")
        print("2 — Візуалізація даних з World Bank CSV")
        print("3 — Кругова діаграма")
        print("0 — Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            task1_plot_function()
        elif choice == "2":
            filename = "pr10.csv"
            task2_visualization_from_csv(filename)
        elif choice == "3":
            task3_pie_chart()
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

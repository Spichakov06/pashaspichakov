def open_file(name, mode):
    try:
        f = open(name, mode, encoding="utf-8")
    except Exception as e:
        print(f"Не вдалося відкрити файл {name}. Причина: {e}")
        return None
    else:
        print(f"Файл {name} відкрито успішно.")
        return f

file_in = "TF19_1.txt"
file_out = "TF19_2.txt"
f_write = open_file(file_in, "w")
if f_write:
    f_write.write("  Я  вчуся  програмувати   на   Python  \n")
    f_write.write("  Ця   мова  дуже   зрозуміла   і   приємна   у  роботі  \n")
    f_write.write("  Сьогодні   я  створюю  програму   для  обробки  тексту \n")
    print("Дані успішно записані до файлу TF19_1.txt.")
    f_write.close()
    print("Файл TF19_1.txt закрито.")
f_read = open_file(file_in, "r")
f_new = open_file(file_out, "w")
if f_read and f_new:
    for line in f_read:
        words = [w for w in line.split() if len(w) > 1]
        cleaned = " ".join(words)
        f_new.write(cleaned + "\n")
    print("Оброблені рядки збережено у TF19_2.txt.")
    f_read.close()
    f_new.close()
    print("Роботу з файлами завершено.")
print("\nВміст TF19_2.txt:")
f_show = open_file(file_out, "r")
if f_show:
    for l in f_show:
        print(l.strip())
    f_show.close()
    print("Файл TF19_2.txt закрито.")

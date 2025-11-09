import csv
input_filename = 'data.csv'
output_filename = 'fdi_results.csv'
valid_data = []

print(f"--- 1. Спроба відкрити та прочитати файл: {input_filename} ---")

try:
    with open(input_filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        if '2015 [YR2015]' not in reader.fieldnames:
            print(f"Помилка: у файлі відсутня колонка '2015 [YR2015]'")
            exit()
        print("\n--- 2. Вміст файлу .csv (Країна: Інвестиції 2015) ---")
        print(f"{'Country Name':<45} | {'2015 [YR2015]':<20}")
        print("-" * 67)
        for row in reader:
            if not row.get('Country Name') or not row.get('2015 [YR2015]'):
                continue
            country = row['Country Name']
            value_str = row['2015 [YR2015]']
            print(f"{country:<45} | {value_str:<20}")
            if value_str != "..":
                try:
                    value_float = float(value_str)
                    valid_data.append({'country': country, 'value': value_float})
                except ValueError:
                    continue
except FileNotFoundError:
    print(f"\n!!! ПОМИЛКА !!!")
    print(f"Файл '{input_filename}' не знайдено.")
    exit()
except Exception as e:
    print(f"Виникла неочікувана помилка при читанні файлу (Блок 1 або 2): {e}")
    exit()
print("\n" + "---" * 20)
print("--- 3. Аналіз даних ---")
if not valid_data:
    print("Не знайдено коректних числових даних для аналізу.")
else:
    try:
        max_record = max(valid_data, key=lambda item: item['value'])
        min_record = min(valid_data, key=lambda item: item['value'])
        print(f"Пошук завершено. Знайдено {len(valid_data)} країн з даними.")
        print(f"\nНайбільше значення (Max):")
        print(f"  Країна: {max_record['country']}")
        print(f"  Сума:   {max_record['value']} US$")
        print(f"\nНайменше значення (Min):")
        print(f"  Країна: {min_record['country']}")
        print(f"  Сума:   {min_record['value']} US$")
        print(f"\n--- 4. Збереження результатів у '{output_filename}' ---")
        try:
            with open(output_filename, mode='w', newline='', encoding='utf-8') as result_file:
                writer = csv.writer(result_file)
                writer.writerow(['Statistic', 'Country Name', 'Value (BoP, current US$)'])
                writer.writerow(['Найбільше значення', max_record['country'], max_record['value']])
                writer.writerow(['Найменше значення', min_record['country'], min_record['value']])
            print(f"Результати успішно збережено у файл '{output_filename}'.")
        except IOError:
            print(f"ПОМИЛКА (Блок 4): Не вдалося записати у файл '{output_filename}'.")
        except Exception as e:
            print(f"Виникла неочікувана помилка при записі файлу (Блок 4): {e}")

    except Exception as e:
        print(f"Виникла неочікувана помилка: {e}")
        if 'max_record' in locals():
            print(f"DEBUG (max_record): {max_record}")
        if 'min_record' in locals():
            print(f"DEBUG (min_record): {min_record}")
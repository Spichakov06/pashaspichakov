import json

students=[{"Surname":"Шевченко","Name":"Олег","Grades":[4,5,3,4,5]},
{"Surname":"Коваль","Name":"Ірина","Grades":[3,2,4,3,3]},
{"Surname":"Мельник","Name":"Андрій","Grades":[5,5,5,4,5]},
{"Surname":"Гриценко","Name":"Сергій","Grades":[2,3,2,3,2]},
{"Surname":"Ткаченко","Name":"Олексій","Grades":[4,4,4,5,4]},
{"Surname":"Бондар","Name":"Микола","Grades":[5,4,5,5,5]},
{"Surname":"Кравчук","Name":"Віктор","Grades":[3,3,4,3,4]},
{"Surname":"Мороз","Name":"Дмитро","Grades":[2,2,3,2,2]},
{"Surname":"Федорчук","Name":"Федір","Grades":[4,5,4,4,5]},
{"Surname":"Лисенко","Name":"Наталя","Grades":[3,3,3,3,3]}]

with open("students.json","w",encoding="utf-8")as f:
 json.dump(students,f,indent=4)

def load_data(filename="students.json"):
 with open(filename,"r",encoding="utf-8")as f:
  return json.load(f)

def save_data(data,filename="students.json"):
 with open(filename,"w",encoding="utf-8")as f:
  json.dump(data,f,indent=4)

def view_data():
 data=load_data()
 for s in data:
  print(s)

def add_student():
 data=load_data()
 print("Додаймо нового учня!")
 surname=input("Прізвище: ")
 name=input("Ім'я: ")
 try:
  grades=list(map(int,input("Оцінки через пробіл (5 штук): ").split()))
 except:
  print("Некоректно введено оцінки")
  return
 if len(grades)!=5:
  print("Потрібно рівно 5 оцінок")
  return
 data.append({"Surname":surname,"Name":name,"Grades":grades})
 save_data(data)
 print("Додано успішно!")

def remove_student():
 data=load_data()
 sname=input("Введіть прізвище для видалення: ")
 before=len(data)
 data=[s for s in data if s["Surname"]!=sname]
 save_data(data)
 if len(data)<before:
  print("Учня видалено.")
 else:
  print("Такого прізвища не знайдено.")

def search_student():
 data=load_data()
 field=input("Шукати за полем (Surname/Name):")
 value=input("Введіть значення: ")
 res=[s for s in data if s.get(field)==value]
 if res:
  for r in res:print(r)
 else:
  print("Нічого не знайдено.")

def max_min_sum_grades():
 data=load_data()
 if not data:
  print("Дані порожні :(")
  return
 sums=[(s["Surname"],s["Name"],sum(s["Grades"]))for s in data]
 max_s=max(sums,key=lambda x:x[2])
 min_s=min(sums,key=lambda x:x[2])
 result={"Найвища сума":{"Surname":max_s[0],"Name":max_s[1],"Sum":max_s[2]},
 "Найнижча сума":{"Surname":min_s[0],"Name":min_s[1],"Sum":min_s[2]}}
 save_data(result,"grades_result.json")
 print("Результат записано у файл grades_result.json")
 print(result)

while True:
 print("\nМеню:\n1-Переглянути\n2-Додати\n3-Видалити\n4-Пошук\n5-Знайти найкращого/найгіршого\n6-Вихід")
 ch=input("Ваш вибір:")
 if ch=="1":view_data()
 elif ch=="2":add_student()
 elif ch=="3":remove_student()
 elif ch=="4":search_student()
 elif ch=="5":max_min_sum_grades()
 elif ch=="6":
  print("До побачення :)")
  break
 else:print("Невірний вибір, спробуй ще.")

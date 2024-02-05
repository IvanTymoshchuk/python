# ------- ПОЗНАЧКИ

#  list - [] - список
#  typle - () - кортедж
#  set - {} - набір
#  dict - {} - словник ( ключ : значення)


# --------- Вивід звичайнх рядків

# name = input("Name: ")
# print("Hello, " + name)
# # or
# print(f"Hello, {name}")

# --------- Перевірка на число (if, elseif, else)
# int - потрібен для того, щоб явно вказати python що ми очікємо переведення в число

# number = int(input("Number: "))
# if number > 0:
#     print("numer is positive")
# elif number < 0:
#     print("number is negative")
# else:
#     print("number is zero ")

# --------- Типи послідовностей , Кортедж ( не можна змінювати послідовність та + нові значення)

# names = ["Ivan", "Oksana", "Inna"]
# print(names[0])
# names.append('Anastasia')
# names.sort()
# print(names)

# ---------

# s = set()
# s.add(1)
# s.add(2)
# s.add(3)
# print(s)
# print(f"The set has {len(s)} element")

# --------- Цикли

# for i in [0, 1, 2, 3, 4, 5]:
#     print(i)
# # теж саме
# for i in range(6):
#     print(i)

# --------- Словники

# houses = {"Ivan": "yes", "Oksana": "no"}

# houses["Anastasia"] = "yes"

# print(houses["Ivan"])

# --------- Функції

# def - позначається функція

# def square(x):
#     return x*x


# for i in range(10):
#     print(f"The square of {i} is {square(i)}")

# Щоб імпортувати фнкцію в інший файл потрібно видалити логіку з цього , а саме :
#  for i in range(10):
#  print(f"The square of {i} is {square(i)}")
# та зробити імпорт : from functions - (це назва файлу) import  square , і підставити логіку яку ми забрали ( якщо потрібно імпортувати цілий файл то пишемо просто import functions)

# zip() - об'єднує декілька в одне ( не важливо яких типів)

# fruis = ["apple", "orange", "banana", "lime"]
# quantatis = [100, 20, 50, 30]
# available = (True, False, True, False)
# fruit_zip = list(zip(fruis, quantatis, available))
# print(
#     fruit_zip
# )  # [('apple', 100, True), ('orange', 20, False), ('banana', 50, True), ('lime', 30, False)]

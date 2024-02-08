# ІМІТАЦІЯ  ПРОДАЖІВ КВИТКІВ НА ЛІТАК

# class Flyight():
#     def __init__(self, capacity):
#         self.capacity = capacity  # тут ми створюємо к-ст пасажирів
#         self.passengers = []  # тут ми створюємо місяце для пасажира

#     def add_passenger(self, name):
#         if not self.open_seats():  # тут ми перевіряємо на наявність місця
#             return False
#         self.passengers.append(name)  # тут ми додаємо пасажира
#         return True

#     def open_seats(self):
#         # тут ми перевіряємо чи є місце
#         return self.capacity - len(self.passengers)


# flight = Flyight(3)  # тут ми передаємо максимульну кількість пасажирів

# people = ["Ivan", "Oksana", "Inna", "Anastasia"]
# for persone in people:
#     if flight.add_passenger(persone):
#         print(f"Added {persone} to flight succesfully.")
#     else:
#         print(f"No available seat for {persone} ")


# *  ДЕКОРАТОРИ - це функції які можна використовувати та перевиначати у інших функція

# def announce(f):
#     def wrapper():
#         print("About to run the function")
#         f()
#         print("Done with the function")
#     return wrapper


# @announce
# def hello():
#     print("Hello")


# hello()


# * ЛЯМБДА ФУНКЦІ

# import sys
# persone = [
#     {"name": "Ivan", "house": "yes"},
#     {"name": "Oksana", "house": "no"},
#     {"name": "Inna", "house": "yes"},
#     {"name": "Anastasia", "house": "no"}
# ]


# def f(persone):
#     return persone["house"]

#! теж саме тільки lamda - це вбудована функція в python, 1 приймає вхідне значення(persone:), настпунийм вихідне(persone["house"])

# persone.sort(key=lambda persone: persone["house"])

# # persone.sort(key=f)
# print(persone)


# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
# except ValueError:
#     print("Invalid value")
#     sys.exit(1)
# try:
#     result = x / y
# except TypeError:
#     print("Error: Cannot divide by 0 ")
#     sys.exit(1)
# print(f"{x} / {y} = {result}")


# -------------

# set_one = {10, 5, 7, 15, 10}

# set_one.add(200)

# set_two = {20, 7, 300, 100, 200}

# intersected_set = set_one.intersection(set_two)
# print(intersected_set)

# my_list = list(intersected_set)
# print(my_list)

# -------------
# * zip() - об'єднує декілька в одне ( не важливо яких типів)

# fruis = ["apple", "orange", "banana", "lime"]
# quantatis = [100, 20, 50, 30]
# available = (True, False, True, False)
# fruit_zip = list(zip(fruis, quantatis, available))
# print(
#     fruit_zip
# )  # [('apple', 100, True), ('orange', 20, False), ('banana', 50, True), ('lime', 30, False)]

# ----------
# *Глибоке та просте копіювання

#! Приклад 1 : просте копіювання ( якщо в середені об'єкта є значення ключ якого мутабельний(наприклад список []) (див.прикл) тоді в такому разі це значення також буде змінюватися після копіювання)

# info = {"name": "Ivan", "at_home": True, "revievs": []}  # це значення яке можна змінити

# info_copy = info.copy()

# info_copy["reviews"].append("Not Work")

# print(info)
# print(info_copy)

#! Приклад 2 : Глибоке копіювання ( якщо в середені об'єкта є значення ключ якого мутабельний (див.прикл) тоді в такому разі це значення не буде змінюватися після копіювання)

# from copy import deepcopy

# info = {"name": "Ivan", "at_home": True, "reviews": []}  # це значення яке можна змінити

# info_deppcopy = deepcopy(info)
# info_deppcopy["reviews"].append("Work")

# print(info)
# print(info_deppcopy)


# -------------------

# def merge_lists_to_dict(list_one, list_two):
#     return dict(zip(list_one, list_two))


# res_one = merge_lists_to_dict(["a", "b", "c"], [True, 10, []])
# print(res_one)


# ---------------
# #  *args - це довільної кількості аргументівʼ


# def sum_num(*args):
#     print(args)
#     print(type(args))
#     return sum(args)


# print(sum_num(1, 2, 3))

#  ---------------
# * Позиційні аргументи (порядок важливий )


# def get_posts_info(name, qtn):
#     info = f"{name} wrote {qtn} posts"
#     return info


# info = get_posts_info("Ivan", 25)
# print(info)

#  ---------------
# *  Аргументи з ключовими словами  (порядок не важливий )


# def get_posts_info(name, qtn):
#     info = f"{name} wrote {qtn} posts"
#     return info


# info = get_posts_info(name="Ivan", qtn=25)
# print(info)


# -------------------
# 1. Перепишіть виклик функції merge lists_to dict із попереднього завдання
# так, щоб у ньому використовувалися аргументи із ключовими словами
# 2. Додайте ще один виклик функції, в якому буде один позиційний аргумент, а другий - аргумент із ключовим словом

# def merge_lists_to_dict(list_one, list_two):
#     return dict(zip(list_one, list_two))


# res_one = merge_lists_to_dict(list_one=["a", "b", "c"], list_two=[True, 10, []])
# res_two = merge_lists_to_dict(["abc"], list_two=[True, 10, []])
# print(res_one)
# print(res_two)


# -----------
# 1. Створіть функцію update car_info, в якій всі іменовані аргументи об'єднуються в словник саг
# 2. Додайте новий ключ is _available c значенням True до словника
# 3. Поверніть із функції змінений словник
# 4. Викличте функцію з іменованими аргументами brand та price, їх значення можуть бути будь-якими
# 5. Виведіть у термінал результат функції


# def update_car_info(**car):
#     car["is_avalible"] = True
#     return car


# res = update_car_info(brand="BMW", price=100000)
# print(res)


# ---------

# from datetime import date


# def get_weekday():
#     return date.today().strftime("%A")


# def create_new_post(post, weekday=get_weekday()):
#     post_copy = post.copy()
#     post_copy["created _on_weekday"] = weekday
#     return post_copy


# initial_post = {
#     "id": 123,
#     "author": "Ivan",
# }
# post_with_weekday = create_new_post(initial_post)
# print(post_with_weekday)
# # {'id': 123, 'author': 'Ivan','created_on_weekday': 'Thursday'}

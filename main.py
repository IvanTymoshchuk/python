#
# * ------- ПОЗНАЧКИ

#  list - [] - список
#  typle - () - кортедж
#  set - {} - набір
#  dict - {} - словник ( ключ : значення)


# * --------- Вивід звичайнх рядків

# name = input("Name: ")
# print("Hello, " + name)
# # or
# print(f"Hello, {name}")

# * --------- Перевірка на число (if, elseif, else)
# int - потрібен для того, щоб явно вказати python що ми очікємо переведення в число

# number = int(input("Number: "))
# if number > 0:
#     print("numer is positive")
# elif number < 0:
#     print("number is negative")
# else:
#     print("number is zero ")

# * --------- Типи послідовностей , Кортедж ( не можна змінювати послідовність та + нові значення)

# names = ["Ivan", "Oksana", "Inna"]
# print(names[0])
# names.append('Anastasia')
# names.sort()
# print(names)

#! ---------

# s = set()
# s.add(1)
# s.add(2)
# s.add(3)
# print(s)
# print(f"The set has {len(s)} element")

# * --------- Цикли

# for i in [0, 1, 2, 3, 4, 5]:
#     print(i)
# # теж саме
# for i in range(6):
#     print(i)

# * --------- Словники

# houses = {"Ivan": "yes", "Oksana": "no"}

# houses["Anastasia"] = "yes"

# print(houses["Ivan"])

# * --------- Функції

# def - позначається функція

# def square(x):
#     return x*x


# for i in range(10):
#     print(f"The square of {i} is {square(i)}")

# Щоб імпортувати фнкцію в інший файл потрібно видалити логіку з цього , а саме :
#  for i in range(10):
#  print(f"The square of {i} is {square(i)}")
# та зробити імпорт : from functions - (це назва файлу) import  square , і підставити логіку яку ми забрали ( якщо потрібно імпортувати цілий файл то пишемо просто import functions)

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


# * -------------

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


# * -------------------

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

# ---------------
# * callback func

# def print_num_inf(num):
#     if (num % 2) == 0:
#         print("Enter number is even")
#     else:
#         print("Enter number is odd")


# def processs_num(num, callback_func):
#     callback_func(num)


# entred_num = int(input("Enter any number: "))
# processs_num(entred_num, processs_num)

# * ----------- Оператор ** ( дві зірочки )

#! Він розпаковує попередній обʼєкт та додає (або змінює якщо вже є вказане значення) у новий обʼєкт, таким чином не відбувається мутація а копія попереднього обʼєкта

# btn = {"with": 200, "color": "grey"}
# red_btn = {**btn, "color": "red"}

# print(btn)
# print(red_btn)

#! ---- Також можна обʼєднати 2 словаря (обʼкта) в 1 за допомогою **

# btn = {"with": 200, "color": "grey"}
# btn2 = {"height": 200}

# new_btn = {**btn, **btn2}

# print(btn)
# print(btn2)
# print(new_btn)

#! ---- Простіший спосіб обʼєднати 2 словаря (обʼкта) в 1 за допомогою |

# btn = {"with": 200, "color": "grey"}
# btn2 = {"height": 200}

# new_btn = btn | btn2

# print(btn)
# print(btn2)
# print(new_btn)


# * --------- Lambda func
#! Потрібна задля того, щоб повернути в тілі функції іншу функцію ( у рарі якщо інша функція повертає тільки 1 вираз)


# def greeting(greet):
#     return lambda name: f"{greet}, {name}!"

#! Той самий результат тільки без lambda

# def greeting(greet):
#     def info(name):
#         return f"{greet}, {name}!"

#     return info


# morning_greeting = greeting("Good Morning")
# print(morning_greeting("Ivan"))
# # Good Morning, Ivan!
# evening_greeting = greeting("Good Evening")
# print(evening_greeting("Ivan"))


# * ---------- обробка помилок

# try:
#     # print(10 / 0)
#     print(10 / 2)
# except ZeroDivisionError:
#     print("Error - Division by zero!")
# print("Continue")


# * ------ або якщо ми не знаємо яка конкретно буде помилка то робимо так:
# try:
#     print(10 / 0)
# except Exception as e:
#     print(e)

# * ------ самостійне створення помилки


# def divide_nums(a, b):
#     if b == 0:
#         raise ValueError("Second argument can't be 0")
#     return a / b


# try:
#     divide_nums(10, 0)
# except ValueError as e:
#     print(e)
# # Second argument can't be 0
# print("Continue...")

# * --------- Тернарний оператор

# my_img = ("1920", "1080")
# info = (
#     f"{my_img [0]}x{my_img [1]}" if len(my_img) == 2 else "Incorrect image formatting"
# )
# print(info)


# * ----------- while

# import random

# random_num = random.randint(1, 5)
# while True:
#     num = int(input("Guess the number from 1 to 5: "))
#     if num != random_num:
#         print("Try again...")
#         continue
#     print("Congratulations!", random_num)
#     break

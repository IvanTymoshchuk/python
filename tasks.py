#
# * ІМІТАЦІЯ  ПРОДАЖІВ КВИТКІВ НА ЛІТАК

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


# * -------------------
# 1. Перепишіть виклик функції merge lists_to dict із попереднього завдання
# так, щоб у ньому використовувалися аргументи із ключовими словами
# 2. Додайте ще один виклик функції, в якому буде один позиційний аргумент, а другий - аргумент із ключовим словом

# def merge_lists_to_dict(list_one, list_two):
#     return dict(zip(list_one, list_two))


# res_one = merge_lists_to_dict(list_one=["a", "b", "c"], list_two=[True, 10, []])
# res_two = merge_lists_to_dict(["abc"], list_two=[True, 10, []])
# print(res_one)
# print(res_two)


# * -----------
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


# * --------------
# 1. Створіть дві змінні та надайте їм однакові послідовності типу set. При цьому не копіюйте одну змінну до іншої
# 2. Виведіть у термінал результат порівняння двох створених об'єктів, поясніть результат
# 3. Порівняйте два об'єкти використовуйте оператор is, поясніть результат
# 4. Перевірте, чи є певні елементи в наборі, використовуючи оператор in

# set_one = {10, "abc", 50, True}
# set_two = {10, "abc", 50, True}

# print(
#     set_one == set_two
# )  #! Порівнює тільки значення , якщо додати ще 1 значення в будь який обʼєкт, то значення буде False

# print(
#     set_one is set_two
# )  #! У цьому випадку ці 2 змінних порівнюються як обʼєкти, і в такому випадку буде False

# print(10 in set_one)
# print("abcd" in set_one)


# * -------------

# my_list = [1, 2]

# if len(my_list) > 0:
#     print("It's okay")

# #! Така ж сама функція (в пайтоні само приводить до порівнянь, тому не потрібно ускладнювати)

# if my_list:
#     print("It's better")


# * ------------ Задача

# 1. Створіть функцію image _info з одним параметром типу dict
# 2. Функція очікує словник, в якому повинно бути як мінімум два ключа:
# • image_id
# • image_title
# 3. Функція повинна повертати строку такого виду
# "Зображення "мій кіт" має id 5136"
# 4. Якщо одного з цих ключів у словнику немає, функція повинна генерувати помилку TypeError
# 5. Використовуйте функцію і коректно обробіть помилку в разі появи


# def image_info(img):
#     if ("image_id" not in img) or ("image_title" not in img):
#         raise TypeError("Keys image_id and image_title must be present")
#     return f"Image {img['image_title']} has id {img['image_id']}"


# # print(image_info({"image_title": "Welcome", "image_id": 777}))
# try:
#     print(image_info({"image_title": "Welcome"}))
# except TypeError as e:
#     print(e)


# * ------------- Задача

# 1. Створіть функцію route_info, якою передаватиметься словник.
# 2. Якщо у словнику є ключ distance та його значення - ціле число, поверніть рядок "Distance to your destination is ‹ distance›"
# 3. Інакше, якщо у словнику є ключі speed та time, поверніть
# рядок "Distance to your destination is < speed * time›"
# 4. Інакше поверніть рядок "No distance info is available"
# 5. Викличте функцію кілька разів із різними аргументами


# def route_info(route):
#     if ("distance" in route) and (type(route["distance"]) == int):
#         return f"Distance to your distenetion is {route['distance']}"
#     if ("speed" in route) and ("time" in route):
#         return f"Distance to your distenetion is {route['speed'] * route['time']}"
#     return "No distance info is avalible"


# print(route_info({"distance": 15}))
# print(route_info({"speed": 20, "time": 3}))
# print(route_info({"my_speed": 10}))


# * --------- Задача
# 1. Створіть функцію dict_to_list, яка конвертуватиме словник у список кортежів
# 2. Функція повинна приймати словник, а повертати список кортежів, у кожному кортежі повинні бути пари (key, value) зі словника
# 3. Якщо значення ключа - ціле число, то його потрібно помножити на 2 перед додаванням до кортежу


# def dict_to_list(dict_to_converte):
#     list_for_convertion = []
#     for k, v in dict_to_converte.items():
#         if type(v) == int:
#             v *= 2
#         list_for_convertion.append((k, v))
#     return list_for_convertion


# print(dict_to_list({"a": 5, "b": {}}))


# * ----------- Задача
# 1. Створіть функцію filter _list, яка буде фільтрувати список
# 2. Функція повинна мати два параметри - список і тип значення
# 3. Функція повинна повернути новий список, в якому залишаться тільки значення того типу, який був переданий у виклику функції другим аргументом 4. Функцію можна буде викликати наприклад: filter list([35, True, 'abc', 10], int) і отримати [35, 10]


# def filter_list(list_to_filter, value_type):
#     filtered_list = []
#     for el in list_to_filter:
#         if type(el) == value_type:
#             filtered_list.append(el)
#     return filtered_list

#! ----- use filter


# def filter_list(list_to_filter, value_type):
#     def check_el_type(el):
#         return type(el) is value_type


#     return list(filter(check_el_type, list_to_filter))

#! -----  use LAMDA


# def filter_list(list_to_filter, value_type):
#     return list(filter(lambda el: type(el) is value_type, list_to_filter))


# print(filter_list([35, True, "abc", 10], int))
# print(filter_list([35, True, "abc", 10], str))
# print(filter_list([35, True, "abc", 10], bool))


# * ---------- Задача

# 1. Создайте цикл, в котором нужно попросить пользователя ввести в терминале два числа
# 2. Выведите в терминал результат деления первого числа на второе
# 3. После этого спросите пользователя, хочет ли он продолжать yes/no
# 4. Если ответ по, то нужно выйти из цикла
# 5. Иначе нужно повторить всё сначала

# while True:
#     num_one = float(input("Please enter number one: "))
#     num_two = float(input("Please enter number two: "))
#     print(num_one / num_two)

#     answer = input("do you want to continue? (yes/no): ")
#     if answer == "no":
#         break


#! ---- обробка помилок
# while True:
#     try:
#         num_one = float(input("Please enter number one: "))
#         num_two = float(input("Please enter number two: "))
#     except ValueError as e:
#         print(e)
#         print("You must enter numbers!")
#         continue
#     print(num_one / num_two)
#     answer = input("Do you want to continue? (yes/no): ")
#     if answer == "no":
#         break


# * -------- Скорочений for in
# 1. Створіть словник з кількома ключами, значення яких мають бути типу str
# 2. Створіть новий словник на підставі існуючого, в якому значення всіх ключів повинні бути у верхньому регістрі
# 3. Виводьте результуючий словник у термінал

# my_motobike = {"brand": "mercedes", "counry": "germany", "owner": "ivan"}

# bike = {k: v.upper() for k, v in my_motobike.items()}
# print(bike)

# * --------- Скорочений for in
# 1. Создайте список с элементами типа str
# 2. Из этого списка создайте новый список, в котором останутся только строки, длина которых больше 3
# 3. Результирующий список выведите в терминал

# my_motobile = ["BMW", "Germany", "Ivan"]

# bike = [el for el in my_motobile if len(el) > 3]
# print(bike)

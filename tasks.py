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


#  ДЕКОРАТОРИ - це функції які можна використовувати та перевиначати у інших функція

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


# ЛЯМБДА ФУНКЦІ

# import sys
# persone = [
#     {"name": "Ivan", "house": "yes"},
#     {"name": "Oksana", "house": "no"},
#     {"name": "Inna", "house": "yes"},
#     {"name": "Anastasia", "house": "no"}
# ]


# def f(persone):
#     return persone["house"]

# теж саме тільки lamda - це вбудована функція в python, 1 приймає вхідне значення(persone:), настпунийм вихідне(persone["house"])

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

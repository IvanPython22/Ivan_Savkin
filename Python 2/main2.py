# ветление истина или ложь

# age = int(input("Введите ваш возвраст: "))
#
# if 18 <= age <= 70:
#     print("Вы можете зарегистрироваться!")
# else:
#     print("Вам нельзя зарегистрироваться!")

# weekdey = int(input("Введите номер дня недели: "))

# if weekdey == 1:
#     print("Понедельник")
# elif weekdey == 2:
#     print("Вторник")
# elif weekdey == 3:
#     print("Среда")
# elif weekdey == 4:
#     print("Четверг")
# elif weekdey == 5:
#     print("Пятница")
# elif weekdey == 6:
#     print("Суббота")
# elif weekdey == 7:
#     print("Воскресенье")
#
# else:
#     print("Такого дня нет")

# email ="ivan@gmail.com"
# password = "123456"
#
# authorization = False
#
# email_input = input("Ведите свой Email: ")
# password_input = input("Введите пароль: ")
#
# if email_input == email:
#     if password_input == password:
#         authorization = True
#         # print("Вы авторизовались")
#     else:
#         print("Пароль неверный")
# else:
#     print("Невероный Email")
#
# match(authorization):
#     case True:
#         print("Пользователь успешно авторизовался")
#     case False:
#         print("Пользователь не авторизовался")

# number = int(input("Введите число: "))
# if number % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")
#
# number = int(input("Введите число: "))
# if number % 2 != 0:
#     print("Нечетное")
# else:
#     print("Четное")

# if number % 6 == 0:
#     print("Число кратное 6")
# else:
#     print("Число не равное")

# from math import sqrt
# print("a*x^2 + b*x + c")
#
# a = float(input("Введите коэффициент a: "))
# b = float(input("Введите коэффициент b: "))
# c = float(input("Введите коэффициент c: "))
#
# D = b**2 - 4 * a * c
# if D < 0:
#     print("Корней нет!")
# elif D == 0:
#     x = -b/(2 * a)
#     print(f"x = {x}")
# else:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b - sqrt(D)) / (2 * a)
#     print(f"x1 = {round(x1, 2)} x2 = {round(x2, 2)}")

# number_1 = int(input("1-ое число: "))
# number_2 = int(input("2-ое число: "))
#
#
# try: # используется для сложных примеров
#     print(number_1/number_2)
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# else:
#     print("Программа выполнилась без ошибок!")
# finally:
#     print("Запустимлся блок Finalli")

# if number_2 == 0:
#     print("На ноль делить нельзя")
# else:
#     print(number_1/number_2)


# try:
#     raise ValueError("Вызвана ошибка специально") # raise - вызвать ошибку
# except FileNotFoundError:
#     print("Обработана ошибка")

# try:
#     raise ValueError
# except ValueError:
#     print("Обработчик ошибки ValueError_1")
# except BaseException:
#     print("Обработчик ошибки ValueError_2")

# try:
#     year = int(input("Введите год: "))
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print("Год високосный")
#     else:
#         print("Год не високосный")
# except (ValueError, TypeError):
#     print("Год должен быть числом!")


# try:
#     number = int(input("Введите число: "))
#     if number % 7 == 0:
#         print("Number is multiple 7")
#     else:
#         print("Number is not multiple 7")
# except ValueError:
#     print('Введите число')

# number_1 = int(input('Введите 1 число: '))
# number_2 = int(input('Введите 2 число: '))
#
# if number_1 > number_2:
#     print(number_1)
# else:
#     print(number_2)

# number_1 = int(input('Введите 1 число: '))
# number_2 = int(input('Введите 2 число: '))
# nun = input('Выберите действие "сумма чисел, разница чисел, среднеарифметическое, произведение чисел" ')
#
# if nun == "сумма чисел":
#     print(number_1 + number_2)
# else:
#     print(nun)
# if nun == "разница чисел":
#     print(number_1 / number_2)
# else:
#     print(nun)
# if nun == "среднеарифметическое":
#     print(number_1 % number_2)
# else:
#     print(nun)
# if nun == "произведение чисел":
#     print(number_1 * number_2)
# else:
#     print(nun)

time = int(input("Введите время в секундах: "))
time1 = print(12*)

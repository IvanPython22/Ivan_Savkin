# string = 'Hello'
# encoded_string = string.encode(encoding='utf8')
# print(encoded_string)
# decoded_string = encoded_string.decode(encoding='utf8')
# print(decoded_string)

# string = 'abcdefg'
# print(len(string))   # длина строки
# print(string [0])    # получение символа из строки по индексу
# print(string[-1])   # последний элемент
# print(string[len(string) - 1])   # последний элемент
# print(string[0:3])  # срез
# print(string[:3])   # срез
# print(string[3:])   # срез
# print(string[0:5:2])    # срез с шагом
# print(string[-1:3:-1])
# print(string[::-1])

# example = '0123456789'
#
# print(example[0:3])     # 012
# print(example[3:6])    # 345
# print(example[-1:-4:-1])    # 987
# print(example[0:9:2])    # 02468
# print(example[-1:-10:-1])    # 987654321
# print(example[-5:-8:-1])    # 543
# print(example[-2:-7:-2])    # 864
# print(example[-6:-10:-1])    # 4312

# text = 'python is a programming language'
# print(text.capitalize())     # первый символ верхний регистр
# print(text.title())    # каждый первый символ верхний регистр
# print(text.count('p'))     # кол-во последовательности в строке
# print(text.lower())     # переводит в нижний регистр
# print(text.upper())     # переводит в верхний регистр
# print(text.replace(' ', '-'))   # замена символа в строке на новый
# print(text.index('n'))  # ищет сколько индексов в строке
# print(text.find('ж'))   # тоже ищет сколько индексов только не выдает ошибку
# print(text.index('Lang')) # на каком индексе начинается строка
# print(len(text))
# print(text.rsplit()) # убирает пробел справа
# print(text.split()) # убирает пробел слева
# print(text.rfind()) # поиск элемента справа на лево и наоборот
# print(text.swapcase()) # делает все элементы с маленькой если с большой буквы

# string_2 = 'python ruby'
# print(string_2.isalnum()) # проверяет только либо буквы и цифры
# print(string_2.isalpha()) # только буквы
# print(string_2.isdigit()) # проверяет цифры
# print(string_2.islower()) # проверка на нижний регистр всю строку
# print(string_2.isupper()) # проверка на верхний регистр всю строку
# print(string_2.isascii()) # проверка символов в таблице ascii
# print('1234'.isdecimal() # проверка на целое число
# print(string_2.isspace()) # проверка на пробел
# print(string_2.startswith('P')) # проверяет начало текста

# string_1 = 'text@mail.ru'
# # print(string_1.endswith('l.ru')) # проверка на символы
# print('@' in string_1)
# print(string_2.count('@') == 1)

# string_3 = 'python rudy js'
# print(string_3.split('r'))      # деление строк по символу

# Email содержит (@, .ru, .com)
# Password  8 символов, буквы и цифры, без спецсимволов

# registration = False
#
# while not registration:
#     email = input('Введите свой Email: ')
#     password1 = input('Введите пароль: ')
#     password2 = input('Подтвердите пароль: ')
#     if ('@' in email) and (email.endswith('.com') or email.endswith('ru')):
#         if password1 == password2:
#             if len(password1) == 8 and password1.isalnum() and not password1.isalpha() and not password1.isdigit():
#                 print('Вы зарегистрированы!')
#                 registration = True
#             else:
#                 print('Пароль должен содержать 8 символов и т.д.')
#         else:
#             print('Пароли должны совпадать')
#     else:
#         print('email должен содержать @ и заканчиватся на .com или .ru')
#

# registration = False
# while not registration:
#     tel = input('Введите телефон в формате +79xxxxxxxxx: ')
#     if tel.startswith('+79') and len(tel) == 12 and tel[1:].isdigit():
#         name = input('Введите имя: ')
#         surname = input('Введите фамилию: ')
#         if name.isalpha() and surname.isalpha():
#             print(f'Ваше имя: {name.capitalize()}\n'
#                   f'Ваша фамилия: {surname.capitalize()}\n'
#                   f'Номер телефона: {tel}')
#             registration = True
#         else:
#             print('Невалидные имя или фамилия!')
#     else:
#         print('Невалидный номер телефона!')

# print(input('Введите строку: ').count(input('Введите символ для поиска: ')))



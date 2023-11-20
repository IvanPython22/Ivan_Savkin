# Словари

# dictionary = {'name': 'Ivan', 'age': 32}

# print(dictionary)
# print(type(dictionary))

# name = dictionary.get('name')
# dictionary['age'] = 33  # установка нового значения
# dictionary['surname'] = 'Ivanov'
# # dictionary.pop('age')   # удаление ключа в этом случае удаляется возвраст и его значение
# # list_man = ['Ivan', 32, 'Ivan']
#
# # import sys
# #
# # print(sys.getsizeof(dictionary))
# # print(sys.getsizeof(list_man))
# # print(dictionary)
#
# # print(dictionary.keys())
# # print(dictionary.values())
# # print(dictionary.items())
#
# # dictionary_2 = {'name': 'Petya', 'age': 32}  # два словаря складывать и вычетать нельзя
# # dictionary.update(dictionary_2)  # меняет значения словаря
# dictionary.setdefault('address', '')    # добавляет ключ со значением по умолчанию, если ключ уже такой есть то он вернет его
# print(dictionary)



# dictionary = {}
#
#
# def set_country(country):
#     dictionary.setdefault(country, [])
#     print('Страна добавлена')
#
#
# def set_city():
#     key = input('Страна: ')
#     country = dictionary.get(key)
#     city_name = input('Введите название города: ')
#     if country or country == []:
#         for i_city in country:
#             if city_name in i_city.keys():
#                 print('Такой город уже есть')
#                 return
#         population = int(input('Введите население города: '))
#         time_zone = input('Ведите пояс: ')
#         new_city = {city_name: {'population': population, 'time_zone': time_zone}}
#         dictionary[key].append(new_city)
#         print('Город добавлен')
#     else:
#         print('Такой страны нет!')
#
#
# def get_city_info():
#     country = input('Страна: ')
#     get_country = dictionary.get(country)
#     if get_country:
#         city = input('Введите название города: ')
#         for i_city in get_country:
#             if city in i_city.keys():
#                 city_info = i_city[city]
#                 print(f'Население города: {city_info.get("population")}\n'
#                       f'Часовой пояс: {city_info.get("time_zone")}')
#                 return
#     else:
#         print('Такого города нет!')
#
#
# def main():
#     while True:
#         choice = input('1 - Добавить страну\n'
#                        '2 - Добавить город\n'
#                        '3 - Получить инфо по городу -> ')
#         if choice == '1':
#             country = input('Введите название страны: ')
#             set_country(country)
#         elif choice == '2':
#             set_city()
#         elif choice == '3':
#             get_city_info()
#
# main()


# text = input('Введите текст: ')
# frequency_dict = {}
#
# for i_symbol in text:
#     if not i_symbol.isspace():
#         frequency_dict.setdefault(i_symbol, 0)
#         frequency_dict[i_symbol] += 1
# # print(frequency_dict)
#
# for key, value in frequency_dict.items():
#     print(f'{key}: {value}')


# text = input('Введите текст: ')
# frequency_dict = {}

# for i_symbol in text:
#     if not i_symbol.isspace():
#         if i_symbol in frequency_dict.keys():
#             frequency_dict[i_symbol] += 1
#         else:
#             frequency_dict[i_symbol] = 1
# for key, value in frequency_dict.items():
#     print(f'{key}: {value}')

#
# for i_symbol in text:
#     if not i_symbol.isspace():
#         count = text.count(i_symbol)
#         if count in frequency_dict.keys():
#             if i_symbol not in frequency_dict[count]:
#                 frequency_dict[count].appenend(i_symbol)
#         else:
#             frequency_dict[i_symbol] = [i_symbol]
# for key, value in frequency_dict.items():
#     print(f'{key}: {value}')
#

# dict_1 = {
#     'key': {
#         'key_2': {
#             'key_3': 125,
#             'key_4': {
#                 'key_5': 'hello'
#             }
#
#         }
#     }
# }
#
#
# dict_1['key_1']['key_2']['key_3'] = 200
# print(dict_1)













































































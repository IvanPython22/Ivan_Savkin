import random
import threading

number = []


def fill_list():
    global number
    number = [random.randint(0, 100) for _ in range(10)]


def sum_list():
    global number
    summa = sum(number)
    print(f'Сумма всех элементов списка: {summa}')


def average_list():
    global number
    average = sum(number) / len(number)
    print(f'Среднеарифметическое элементов: {average}')


t1 = threading.Thread(target=fill_list())
t2 = threading.Thread(target=sum_list())
t3 = threading.Thread(target=average_list())

t1.start()
t1.join()

t2.start()
t3.start()

t2.join()
t3.join()

print(f'Список чисел: {number}')

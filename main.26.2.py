
import random
import threading

input_file = ''
test = 'test.txt'
test1 = 'test1.txt'


def fill_file():
    global input_file
    with open(input_file, 'w') as f:
        numbers = [str(random.randint(1, 100)) for _ in range(10)]
        f.write('\n'.join(numbers))


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def find_prime_numbers():
    global input_file, test
    prime_numbers = []

    with open(input_file, 'r') as file:
        numbers = file.readlines()
        for number in numbers:
            n = int(number)
            if is_prime(n):
                prime_numbers.append(str(n))

    with open(test, 'w') as file:
        file.write('\n'.join(prime_numbers))

    print(f'Найдено {len(prime_numbers)} простых чисел')


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def calculate_factorials():
    global input_file, test1
    factorials = []

    with open(input_file, 'r') as file:
        numbers = file.readlines()
        for number in numbers:
            n = int(number)
            fact = factorial(n)
            factorials.append(str(fact))

    with open(test1, 'w') as file:
        file.write('\n'.join(factorials))

    print(f'Вычислено {len(factorials)} факториалов')


input_file = input('Введите путь к файлу: ')

fill_thread = threading.Thread(target=fill_file)
fill_thread.start()
fill_thread.join()


prime_thread = threading.Thread(target=find_prime_numbers)
factorial_thread = threading.Thread(target=calculate_factorials)

prime_thread.start()
factorial_thread.start()

prime_thread.join()
factorial_thread.join()

import os
import threading


def search_files(directory, world, result):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    content = file.read()
                    if world in content:
                        result.append(file_path)


def remove_words(file_path, forbidden_words):
    with open(file_path, 'r') as file:
        content = file.read()

    for world in forbidden_words:
        content = content.replace(world, "")

    with open(file_path, 'w') as file:
        file.write(content)


directory = input('Введите путь к существующей директории: ')
word = input('Введите слово для поиска: ')

result = []
search_thread = threading.Thread(target=search_files, args=(directory, word, result))
search_thread.start()
search_thread.join()

print('Найденные файлы: ')
for file_path in result:
    print(file_path)

forbidden_words = []
with open('merged_files.txt', 'r') as file:
    forbidden_words = file.read().splitlines()

for file_path in result:
    remove_words(file_path, forbidden_words)

print('Статистика: ')
print(f'Количество найденных файлов: {len(result)}')
print(f'Количество запрещенных слов: {len(forbidden_words)}')

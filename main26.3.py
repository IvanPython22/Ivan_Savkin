import shutil
import os
import threading


def copy_file(source, destination):
    shutil.copy2(source, destination)


def copy_directory(source, destination):
    if not os.path.exists(source):
        print(f'Папка {source} не существует')
        return
    if not os.path.isdir(source):
        print(f'{source} не является папкой')
        return

    if not os.path.exists(destination):
        os.makedirs(destination)
        print(f'Создана новая папка {destination}')

    files_copied = 0
    directories_created = 0

    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        if os.path.isfile(source_path):
            thread = threading.Thread(target=copy_file, args=(source_path, destination_path))
            thread.start()
            files_copied += 1
        elif os.path.isdir(source_path):
            thread = threading.Thread(target=shutil.copytree, args=(source_path, destination_path))
            thread.start()
            directories_created += 1

    main_thread = threading.current_thread()
    for thread in threading.enumerate():
        if thread is not main_thread:
            thread.join()

    print(f'Скопированы файлы: {files_copied}')
    print(f'Созданы папки: {directories_created}')


source_directory = input('Введите путь к исходной папке: ')
destination_directory = input('Введите путь к целевой папке: ')

copy_directory(source_directory, destination_directory)

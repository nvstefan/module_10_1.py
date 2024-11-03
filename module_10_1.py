# Домашнее задание
# по теме "Введение в потоки".

# Задача "Потоковая запись в файлы":

from datetime import datetime
from time import sleep
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)  # Пауза на 0.1 секунды перед следующей записью
        print(f"Завершилась запись в файл {file_name}")

start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
stop_time = datetime.now()
duration_write = stop_time - start_time
print(f"Работа потоков {duration_write}")

"""Создание потоков"""

threads = []
args_list = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

start_time = datetime.now()
for args in args_list:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()  # Запускаем поток

# Ожидаем завершения всех потоков
for thread in threads:
    thread.join()

stop_time = datetime.now()
duration_write = stop_time - start_time

print(f"Работа потоков {duration_write}")

print("Все потоки завершены.")
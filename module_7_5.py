import os
import time
print('Текущая директория:', os.getcwd())
directory = os.getcwd()

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath =  os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M",  time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file}\n Путь: {filepath}\n Размер: {filesize} байт\n Время изменения: {formatted_time}\n Родительская директория: {parent_dir}')

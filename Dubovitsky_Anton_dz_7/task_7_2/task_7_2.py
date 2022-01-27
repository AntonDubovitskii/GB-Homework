"""
Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:

|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
"""

import os
import json

current_path = os.path.dirname(os.path.abspath(__file__))
base_dir = []

# Код функции идентичен применяемому в задании 7_1
def create_starter(s_dict: dict):
    counter = 0
    # Далее костыль, чтобы как-то сохранить путь до корневой директории и не потерять его в рекурсии
    for key in s_dict.keys():
        base_dir.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), key))
    for key, value in s_dict.items():
        # Использование глобальной переменной, чтобы иметь возможность достраивать путь в рекурсии. Плохо, но пока
        # более изящное решение в голову не идёт
        global current_path
        current_path = os.path.join(current_path, key)
        new_path = current_path
        if not os.path.exists(new_path):
            os.mkdir(current_path)        # создание очередной директории
        if not value:
            current_path = base_dir[0]    # проверка на случай если очередная директория пуста, тогда возврат к корню
        for i, item in enumerate(value):
            # Далее если значение является строкой, а не ещё одним словарём, значит это файл, он создается
            if type(item) is str:
                item_path = os.path.join(new_path, item)
                if not os.path.exists(item_path):
                    file = open(item_path, 'w')
                    file.close()
                    counter += 1
                # Счётчик counter служит для отслеживания тупиков, когда больше нет вложенных директорий. В таком случе
                # происходит возврат к пути корневой директории, чтобы начать создавать очередную ветку структуры
                if i == len(value)-1 and counter == len(value):
                    current_path = base_dir[0]
                    counter = 0
            else:
                create_starter(item)  # Рекурсия. Функция вызывает саму себя, пока не обойдет все словари


if __name__ == '__main__':
    with open('config.yaml', 'r', encoding='utf-8') as fr:
        str_starter = fr.read()
        # Вычитка из файла и преобразование в формат json, чтобы восстановить словарь из строки
        dict_starter = json.loads(str_starter.replace("'",'"'))
        create_starter(dict_starter)


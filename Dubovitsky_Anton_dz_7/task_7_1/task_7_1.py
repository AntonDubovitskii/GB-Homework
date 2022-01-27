"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""
import os

current_path = os.path.dirname(os.path.abspath(__file__))
base_dir = []


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

    dict_for_starter = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}
    create_starter(dict_for_starter)

"""
В дальнейшем можно корректировать словарь под конкретный проект, менять название папок, добавлять файлы. Случаи когда 
папки и файлы уже есть в данном пути учтены.
"""
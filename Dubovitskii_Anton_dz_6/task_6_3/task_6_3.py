"""
Есть два файла users.csv и hobby.csv: в первом хранятся ФИО пользователей сайта, а во втором — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями —
запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные
о хобби (список строковых переменных). Сохранить словарь в файл task_6_3_result.json. Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом 1.
"""
import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    result_tuple = {}

    with open(path_users_file, 'r', encoding='utf-8') as f:
        users_list = f.readlines()

    with open(path_hobby_file, 'r', encoding='utf-8') as f:        # Прочтение строк из файлов и составление списков
        hobbies_list = f.readlines()

    for n in range(0, len(users_list)):
        users_list[n] = users_list[n].replace(',', ' ').replace('\n', '')
    for i in range(0, len(hobbies_list)):
        hobbies_list[i] = hobbies_list[i].replace('\n', '').split(',')         # Очистка списков от всего лишнего

    if len(users_list) >= len(hobbies_list):
        for i in range(0, len(users_list)):             # создание словаря из списков
            if i < len(hobbies_list):
                result_tuple.setdefault(users_list[i], hobbies_list[i])
            else:                                  # Если элементы в списке с хобби заканчиваются, подставляется None
                result_tuple.setdefault(users_list[i], None)
    else:
        sys(exit(1))         # Если записей в файле с хобби больше записей в файле имен - происходит выход с кодом 1

    return result_tuple


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)

with open('task_6_3_result.json', 'r', encoding='utf-8') as fr:
    dict_return = json.load(fr)                                  # Проверка - прочтение данных из json

print(dict_return)


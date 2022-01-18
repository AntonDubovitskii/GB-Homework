"""
Написать свой модуль utils и копировать в него функцию currency_rates() из предыдущего задания.

Создать в корневой директории урока, рядом с модулем utils скрипт task_4_4.py, в котором импортировать модуль
utils и выполнить несколько вызовов функции utils.currency_rates().

Убедиться, что ничего лишнего не происходит.

Приложите в конце скрипта task_4_4.py многострочным комментарием результат его запуска с консоли/терминала.
"""

from utils import currency_rates

print(currency_rates('BRL'))

print(currency_rates('eur'))

print(currency_rates('CNY'))


#C:\Users\Антон\PycharmProjects\GB-Homework\venv\Scripts\python.exe C:/Users/Антон/PycharmProjects/GB-Homework/Dubovitskii_Anton_dz_4/task_4_4.py
#13.70
#86.89
#11.95
#
#Process finished with exit code 0

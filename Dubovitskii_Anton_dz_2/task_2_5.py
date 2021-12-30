from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    str_out = ''

    for item in my_list:
        str_out += f'{int(item):02d} руб {int((str(item * 100))[2:4:]):02d} коп, '

    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""

    print(f'{id(my_list)} - изначальный идентификатор списка')
    my_list.sort()
    return my_list


result_2 = sort_prices(my_list)

print(f'{id(result_2)} - идентификатор списка после сортировки')   # идентификаторы совпадают
print(result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""

    list_out = sorted(my_list, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_out = sorted(my_list)

    return list_out[len(list_out) - 5: len(list_out)]


result_4 = check_five_max_elements(my_list)
print(result_4)

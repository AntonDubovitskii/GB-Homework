"""
Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""

class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


class ListFill:
    @staticmethod
    def enter_data():
        numbers_list = []

        while True:
            try:
                number = input('Введите число: ')
                if number == 'end':
                    break
                elif number.replace('.', '').isdigit():
                    numbers_list.append(number)
                else:
                    raise NotNumber('не число!')
            except NotNumber as err:
                print(f'{number} - {err}')

        return numbers_list


if __name__ == '__main__':

    print(ListFill.enter_data())


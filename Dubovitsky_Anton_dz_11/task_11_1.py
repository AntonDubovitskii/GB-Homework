"""
Реализовать класс Дата, функция-конструктор которого должна принимать дату в виде строки формата день-месяц-год.
В рамках класса реализовать два метода:

Первый — с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_str: str):
        self.date_str = date_str

    @classmethod
    def to_int(cls, date_str):
        date_list = date_str.split('-')
        return int(date_list[0]), int(date_list[1]), int(date_list[2])

    @staticmethod
    def date_validation(date: str):
        i = True
        date_list = date.split('-')
        if not date_list[0].isdigit() or int(date_list[0]) > 31:
            print(f'Неверная дата! Число {date_list[0]} не соответствует формату дня!')
            i = False
        if not date_list[1].isdigit() or int(date_list[1]) > 12 or int(date_list[1]) < 1:
            print(f'Неверная дата! Число {date_list[1]} не соответствует формату месяца!')
            i = False
        if not date_list[2].isdigit() or int(date_list[2]) < 1900:
            print(f'Неверная дата! Число {date_list[2]} не соответствует формату года!')
            i = False
        if i:
            return True
        else:
            return False


if __name__ == '__main__':

    print(Date.to_int('11-10-1990'))

    print(Date.date_validation('10-12-1990'))
    # True
    print(Date.date_validation('05-11-1990'))
    # True
    print(Date.date_validation('51-41-899'))
    """
    Неверная дата! Число 51 не соответствует формату дня!
    Неверная дата! Число 41 не соответствует формату месяца!
    Неверная дата! Число 899 не соответствует формату года!
    False
    """



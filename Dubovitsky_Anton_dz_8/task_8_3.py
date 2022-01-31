"""
Написать декоратор для логирования типов позиционных аргументов функции

Дополнительные задания:

вывести тип значения функции
решить задачу для именованных аргументов
замаскировать работу декоратора
вывести имя функции
"""
from functools import wraps


def f_wrapper(func):

    @wraps(func)
    def log_wrapper(*args, **kwargs):
        """Декоратор, логирующий аргументы функции."""
        result = func(*args, **kwargs)
        result_list = []

        [result_list.append(f'{arg}: {type(arg)}') for arg in args]
        [result_list.append(f'{kwarg}: {type(kwarg)}') for kwarg in kwargs.values()]

        print(f'{func.__name__}({", ".join(map(str, result_list))})')

        return result

    return log_wrapper


@f_wrapper
def my_func(number: int, word: str, statement: bool):
    """
    Принимает число, строку и булево значение. Печатает строку, в которой содержится число во 2 степени, слово в
    верхнем регистре и булево значение обратное переданному. Если это описание возможно прочитать,
    значит работает маскировка декоратора.
    """
    number ** 2
    print(f'Вывод функции: {number} во 2 степени = {number ** 2} | {word.upper()} | {not statement}')


my_func(5, word='3 часа ночи, а я всё Питон учу', statement=False)


print(my_func.__doc__)




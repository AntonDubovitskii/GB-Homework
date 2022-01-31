"""Написать декоратор с аргументом-функцией (callback),
позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так"""
from functools import wraps


def digit_check(value):
    # Проверка значения. Судя по примеру из задания валидацию не должны проходить и отрицательные значения, но лично
    # я не вижу проблем в возведении отрицательных чисел в степень, поэтому оставил
    if str(value).replace('.', '').replace('-', '').isdigit():
        return True


def val_checker(d_check):
    def val_wrapper(func):
        @wraps(func)
        def wrapper(*args):
            for arg in args:
                if not d_check(arg):
                    msg = f'wrong value: {arg}'
                    raise ValueError(msg)
            return func(*args)
        return wrapper
    return val_wrapper


@val_checker(digit_check)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube(-10))
    # print(calc_cube('ss'))


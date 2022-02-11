"""
Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.

Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


class SafeCalc:
    @staticmethod
    def safe_div(dividend: int, divisor: int):
        try:
            if divisor == 0:
                raise DivZeroError("Попытка деления на ноль!")
            result = dividend / divisor
        except TypeError:
            print("Ошибка, в операции деления могут участвовать только числа")
        except DivZeroError as err:
            print(err)
        else:
            print(result)

    @staticmethod
    def safe_div_manual():
        while True:
            try:
                dividend = input('Производится операция деления. Введите делимое: ')
                if str(dividend) == 'end':
                    break
                divisor = input('Введите делитель: ')
                if str(divisor) == 'end':
                    break
                if int(divisor) == 0:
                    raise DivZeroError("Попытка деления на ноль!")
                result = int(dividend) / int(divisor)
            except ValueError:
                print("Ошибка, в операции деления могут участвовать только числа")
            except DivZeroError as err:
                print(err)
            else:
                print(result)


if __name__ == '__main__':

    SafeCalc.safe_div(50, 2)
    # 25.0
    SafeCalc.safe_div(2, 100)
    # 0.02
    SafeCalc.safe_div(3, 0)
    # Попытка деления на ноль!
    SafeCalc.safe_div(25, 'f')
    # Ошибка, в операции деления могут участвовать только числа

    print('-'*50)
    SafeCalc.safe_div_manual()

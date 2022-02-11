"""
Реализовать проект Операции с комплексными числами.

Создать класс Комплексное число.
Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
выполнить сложение и умножение созданных экземпляров.
Проверить корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, sn_string: str):

        i = 0
        sn_string = sn_string.replace(' ', '')     # Удаление пробелов

        if not sn_string.replace('+', '').replace('-', '').replace('i', '').isdigit():
            raise ValueError('Некорректное значение')          # Проверка на корректность значения

        """
        Далее проход по строке, поиск знаков сложения или вычитания, чтобы узнать где заканчивается вещественная и 
        начинается мнимая часть. Перед знаком вставляется пробел.
        """
        while i < len(sn_string):
            if sn_string[i] == '-' and i > 0:
                sn_string = sn_string[:i] + " " + sn_string[i:]
                i += 2
            elif sn_string[i] == '+':
                sn_string = sn_string[:i] + " " + sn_string[i+1:]
                i += 2
            else:
                i += 1
        """
        Разделяю строку по пробелу, теперь по индексу 0 вещественная часть, а по 1 мнимая. Удаляю символ мнимой 
        единицы, он не потребуется для вычислений и будет добавлен обратно позднее. 
        """
        self.real = int(sn_string.split(' ')[0])
        self.imaginary = int(sn_string.split(' ')[1].replace('i', ''))

    def __str__(self):
        if self.imaginary > 0:
            return f'{self.real}+{self.imaginary}i'
        else:
            return f'{self.real}{str(self.imaginary)}i'

    def __add__(self, other):
        new_real = int(self.real) + int(other.real)
        new_imaginary = int(self.imaginary) + int(other.imaginary)
        if new_imaginary > 0:
            new_number = f'{new_real}+{new_imaginary}i'
        else:
            new_number = f'{new_real}{new_imaginary}i'
        return ComplexNumber(new_number)

    def __mul__(self, other):
        a1 = self.real
        a2 = other.real
        b1 = self.imaginary
        b2 = other.imaginary
        new_real = a1 * a2 - (b1 * b2)
        new_imaginary = a1 * b2 + b1 * a2
        if new_imaginary > 0:
            result = f'{new_real} + {new_imaginary}i'
        else:
            result = f'{new_real}{new_imaginary}i'
        return ComplexNumber(result)


if __name__ == '__main__':
    cn1 = ComplexNumber('2+2i')
    cn2 = ComplexNumber('8-7i')

    print(f'Первое тестовое комплексное число: {cn1}')
    print(f'Второе тестовое комплексное число: {cn2}')

    print(f'Сумма тестовых комплексных чисел: {cn1 + cn2}')    # 10-5i
    print(f'Сложение этих же чисел стандартными средствами Питона: {(2+2j) + (8-7j)}')  # (10-5j)

    print(f'Произведение тестовых комплексных чисел: {cn1 * cn2}')  # 30+2i
    print(f'Произведение этих же чисел стандартными средствами Питона: {(2+2j) * (8-7j)}')   # (30+2j)

    # cn3 = ComplexNumber('dsfsdfsd')
    # print(cn1 + cn3)
    """
    Некорректное значение сn3

    Traceback (most recent call last):
    ...
    ValueError: Некорректное значение
    """


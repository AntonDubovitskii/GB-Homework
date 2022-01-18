"""
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего
"""


def get_numbers(src: list):

    x = src[0]
    for el in range(1, len(src)):
        if src[el] > x:
            yield src[el]
        x = src[el]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 11, 98]

print(*get_numbers(src))


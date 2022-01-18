"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
"""

def get_uniq_numbers(src: list):
    unique_set = set()
    repit_set = set()

    for elem in src:
        if elem not in repit_set:
            unique_set.add(elem)                  # Составляется множество уникальных значений
        else:
            unique_set.discard(elem)
        repit_set.add(elem)

    unique_nums = (elem for elem in src if elem in unique_set)  # Создается генератор, выдающий значения без повторов
    return unique_nums                                          # сверяясь с множеством уникальных значений, но в
                                                                # порядке их следования в изначальном списке

src = [2, 2, 2, 7, 23, 1, 44, 35, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))


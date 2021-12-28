"""Реализовать склонение слова процент во фразе N процентов.
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100"""


def transform_string(number: int) -> str:
    """Так как по заданию работа ведется строго в диапазоне от 1 до 100 включительно, можно выделить 4 группы чисел\
влияющих на окончание слова после них. Первая - при делении с остатком на 10 дает остаток 1,
вторая - при делении на 10 с остатком дают остатки 2,3 и 4,
третья - исключение, все числа в диапазоне от 11 до 14 включительно, четвертая - все остальные.
 Теперь остается лишь реализовать все варианты ветвлением."""
    #Сперва проверяется исключение, которое вызывано правилами склонения числительных в русском языке
    if number > 10 and number < 15:
        new_string = f'{number} процентов'
    #Остальное определяется по общим правилам
    elif number % 10 == 1:
        new_string = f'{number} процент'
    elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
        new_string = f'{number} процента'
    else:
        new_string = f'{number} процентов'

    return new_string


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))


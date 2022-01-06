"""" Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Если перевод сделать невозможно, вернуть None. Реализовать корректную работу с числительными, начинающимися с заглавной
буквы — результат тоже должен быть с заглавной."""


def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский"""

    translate_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    capital_letter = False

    if value.istitle():
        value = value.lower()           # Если слово с большой буквы, его следует привести к нижнему регистру
        capital_letter = True           # для обработки.

    str_out = translate_dict.get(value)  # метод .get() извлекает из словаря значение по ключу

    if capital_letter:
        str_out = str_out.title()        # восстанавливается большая буква, если она была изначально
    return str_out


print(num_translate_adv("One"))       # Один
print(num_translate_adv("eight"))     # восемь
print(num_translate_adv("Seven"))     # Семь

print(num_translate_adv("nineteen"))  # если указанного ключа не существует, метод .get() возвращает None


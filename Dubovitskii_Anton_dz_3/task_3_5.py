"""Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Документировать код функции.
Добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках.
Cделать аргументы именованными."""

from random import choice


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_out = []

    while count > 0:   # в базовой версии задачи просто выводится список из строк, повторение слов допускается
        list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        count -= 1

    return list_out


def get_jokes_adv(count: int = 1, flag=False) -> list:
    """
    Возвращает список шуток в количестве count

    :param count: тип int, количество возвращаемых шуток (значение по умолчанию: 1)
    :param flag: тип bool, флаг, при значении True запрещяющий повторы слов в шутках (значение по умолчанию: False)
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_out = []

    if not flag:            # если не выставлен флаг, запрещающий повторения - функция работает идентично предыдущей

        while count > 0:
            list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            count -= 1
    else:
        while count > 0:
            if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:  # проверка на доступность слов
                break
            noun = choice(nouns)
            adverb = choice(adverbs)
            adjective = choice(adjectives)

            list_out.append(f'{noun} {adverb} {adjective}')

            nouns.remove(noun)             # использованные слова удаляются из списков
            adverbs.remove(adverb)
            adjectives.remove(adjective)

            count -= 1

    return list_out


print(get_jokes(3))                  # работа базовой функции

print(get_jokes_adv())               # вызов усложненной функции без параметров, подключаются значения по умолчанию
print(get_jokes_adv(2))              # вызов усложненной функции, генерация двух шуток, возможны повторения
print(get_jokes_adv(4, True))       # вызов усложненной функции, с флагом, генерация 4 шуток без повторений




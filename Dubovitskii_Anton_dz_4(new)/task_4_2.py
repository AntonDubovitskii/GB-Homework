"""В корневой директории урока создать task_4_2.py и написать в нём функцию currency_rates(),
принимающую в качестве аргумента код валюты (например, USD, EUR, SGD, ...) и
возвращающую курс этой валюты по отношению к рублю.

Использовать библиотеку requests.

Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.

В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
"""
from requests import get
import decimal


def currency_rates(code: str) -> decimal:
    """возвращает курс валюты `code` по отношению к рублю"""

    result_value = None

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    x = str(response.content)                                     # получение xml и сохранение как строки

    x = x.split("<CharCode>")                                     # строка делится по открывающему тегу CharCode,
                                                                  # получается список, где в начале каждого элемента - код валюты
    for item in x:
        item = item.split('</CharCode>')                          # код валюты выделяется в отдельный элемент
        if item[0] == code.upper():                               # находится требуемая строка, содержащая нужный код
            item = item[1].split('<Value>')
            result_value = item[1].split('</Value>')              # пошагово отбрасывается всё, кроме значения внутри тегов <Value></Value>
            result_value = result_value[0]
            result_value = f"{result_value.split(',')[0]}.{result_value.split(',')[1]}" # приведение к стандартному виду

    if type(result_value) is str:
        return round(decimal.Decimal(result_value), 2)    # приведение строки к decimal, с округлением до 2 знаков после нуля


if __name__ == "__main__":
    print(currency_rates("usd"))
    print(currency_rates("TRY"))
    print(currency_rates("HUF"))
    print(currency_rates("noname"))


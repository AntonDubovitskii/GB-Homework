"""В task_4_3.py создать функцию currency_rates_adv() аналогичную currency_rates()
прошлого задания, только теперь она должна возвращать кроме курса ещё и дату,
которая передаётся в ответе сервера.

Дата должна быть в виде объекта date. Т.е. функция должна возвращать кортеж из двух
элементов следующих типов float и datetime.date"""

import datetime
from requests import get


def currency_rates_adv(code: str):

    inter_result = None

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    x = str(response.content)

    x = x.split("<CharCode>")

    for item in x:
        item = item.split('</CharCode>')
        if item[0] == code.upper():
            item = item[1].split('<Value>')
            inter_result = item[1].split('</Value>')
            inter_result = inter_result[0]
            inter_result = f"{inter_result.split(',')[0]}.{inter_result.split(',')[1]}"

    if type(inter_result) is str:
        inter_result = round(float(inter_result), 2)                 #в задании 4_2 я выводил значение в decimal, но
                                                                     #в данном задании требуется float и проверка идёт
    date_now = datetime.datetime.now()                               #по типу float, поэтому решил оставить этот тип
    result_value = (inter_result, date_now.date())
    return result_value

kurs, date_value = currency_rates_adv("USD")


empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")

print(f"{kurs}, {date_value}")


from requests import get
import decimal


def currency_rates(code: str) -> decimal:
    """возвращает курс валюты `code` по отношению к рублю"""

    result_value = None

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    x = str(response.content)

    x = x.split("<CharCode>")

    for item in x:
        item = item.split('</CharCode>')
        if item[0] == code.upper():
            item = item[1].split('<Value>')
            result_value = item[1].split('</Value>')
            result_value = result_value[0]
            result_value = f"{result_value.split(',')[0]}.{result_value.split(',')[1]}"

    if type(result_value) is str:
        # return float(result_value)
        return round(decimal.Decimal(result_value), 2)


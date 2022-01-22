"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные)
 файл логов web-сервера nginx_logs.txt — получить список кортежей вида:
  (<remote_addr>, <request_type>, <requested_resource>)
"""

from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    ip_addres = line.split(' ')[0]         # Сохраняется адрес
    parse = line.split('\"')[1]            # "Отщипывается" от остальной строки участок с протоколом и путем
    protocol = str(parse).split(' ')[0]    # Cохраняется протокол
    path = str(parse).split(' ')[1]        # Сохраняется путь
    return ip_addres, protocol, path


list_out = list()

with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    text = fr.readlines()
    for line in text:
        list_out.append(get_parse_attrs(line))       # В результирующий список заносятся все прочитанные строки

pprint(list_out)


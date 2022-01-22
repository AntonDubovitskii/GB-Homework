from pprint import pprint
from requests import get

def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    ip_addres = line.split(' ')[0]
    parse = line.split('\"')[1]
    protocol = str(parse).split(' ')[0]
    path = str(parse).split(' ')[1]
    return ip_addres, protocol, path


list_out = list()

with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    text = fr.readlines()
    for line in text:
        list_out.append(get_parse_attrs(line))

pprint(list_out)
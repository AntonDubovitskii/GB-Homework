"""
Написать тело функции email_parse(email: str),
которая при помощи регулярного выражения извлекает имя пользователя
и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
"""
import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'^[\w!#$%&\'*+\-/=?^_`{|}~]+(\.[\w!#$%&\'*+\-/=?^_`{|}~]+)*' 
                         r'@([\w_\[\]]+(\-\.[\w_\[\]]+)*\.[a-z]+)+$')     # Валидирующее регулярное выражение
    if RE_MAIL.match(email):
        RE_MAIL_SEP = re.compile(r'[\w!#$%&\'*+\-/=?^_`{|}~\.\[\]]+')     # Регулярное выражение для выделении имени
        result_list = RE_MAIL_SEP.findall(email)                          # пользователя и email адреса

        if len(result_list[0]) > 64:                                      # Дополнительная проверка на длину
            msg = f'local-part is longer than 64 characters: {email}'
            raise ValueError(msg)

        result_dict = {'username': result_list[0], 'domain': result_list[1]}
        return result_dict

    else:
        msg = f'wrong email: {email}'
        raise ValueError(msg)


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    print(email_parse('someone@geekbrains.ru'))
    # email_parse('loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong@geekbrains.ru')
    # print(email_parse('someone@geekbrains.ru'))
    # email_parse('someone@geekbrainsru')
    # print(email_parse('someone@geekbrainsru'))


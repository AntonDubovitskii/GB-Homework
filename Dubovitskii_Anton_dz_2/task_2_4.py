def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = []

    x = 0
    i = 0

    while i < len(list_in):                  # каждый элемент списка разделяется по пробелу, берется последний
        sup_list = list_in[i].split()        # по условию это всегда нужное имя
        list_out.append(sup_list[-1])        # имена заносятся в отдельный список
        i += 1

    while x < len(list_out):
        list_out[x] = f'Привет, {list_out[x].title()}!'     # каждый элемент списка достраивается согласно требованиям
        x += 1

    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

result = convert_name_extract(my_list)
print(result)


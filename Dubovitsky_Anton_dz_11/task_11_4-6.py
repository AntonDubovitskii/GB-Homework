"""
Создать класс, описывающий склад. А также класс Оргтехника, который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (Принтер, Сканер, Ксерокс).
В базовом классе определить параметры, общие для приведённых типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).

Реализовать механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных!
"""

import random
from collections import Counter


class EquipmentPurchase:
    @classmethod
    def buy_from_supplier(cls, product, quantity_to_buy: int):
        """
        Инициализирует объекты указанного класса в заданном количестве, после чего составляет из них список
        :param product: класс
        :param quantity_to_buy: целое число, количество объектов класса, которые необходимо инициализировать
        :return: список объектов класса переданного в :param product:
        """
        purchase_list = []
        for x in range(0, quantity_to_buy):
            # Далее очень нехороший способ задать уникальный код продукта, но думаю для данного уровня абстракции сойдёт
            purchase_list.append(product(str(random.randrange(1, 10**7))))
        return purchase_list


class Warehouse:
    def __init__(self, address: str, capacity: int,):
        self.capacity = capacity
        self.address = address
        self.storage = {}       # Словарь, хранящий пары, где ключом является уникальный код оборудования, а значением -
                                # строка с общим названием офисного оборудования

    @staticmethod
    def check_storage(warehouse):
        """"
        Принимает объект класса Warehouse, подсчитывает количество уникальных значений в словаре
        """
        check_list = []
        for eq in warehouse.storage.values():
            check_list.append(eq)
        x = Counter(check_list)
        print(f'\nКоличество оборудования на складе по адресу {warehouse.address}:')
        for a, b in x.items():
            print(a, b)

    def add_equipment(self, supply):
        """
        Заполняет склад оборудованием (объектами из списка)
        :param supply: Список объектов потомков класса OfficeEquipment
        :return: сообщения в виде строк в stdout
        """
        self.count = 0
        try:
            for equipment in supply:
                if not isinstance(equipment, OfficeEquipment):
                    print('Ошибка, склад предназначен для хранения офисного оборудования')
                    continue
                if self.capacity > 0:
                    self.storage.setdefault(equipment.equipment_code, equipment.equipment_type)
                    self.count += 1
                    self.capacity -= 1
                else:
                    print(f'Склад по адресу "{self.address}" заполнен!')
                    break
        except TypeError:
            print('Ошибка составления запроса на поставку')

        print(f'На склад по адресу "{self.address}" отправлено {self.count} единиц оборудования {supply[0].equipment_type}, осталось место для'
              f' {self.capacity} единиц')

    def send_to_department(self, equipment_type: str, quantity: int, department: str):
        """
        Изымает оборудование со склада и "отправляет" его по указанному адресу
        :param equipment_type: строка с названием офисного оборудования
        :param quantity: целое число - количество оборудования, которое необходимо изъять со склада для отправки
        :param department: строка - адрес, куда отправляется оборудование
        :return: сообщения в виде строк в stdout
        """
        self.send_count = 0
        self.send_list = []
        for code, item in self.storage.items():
            if item == equipment_type:
                self.send_list.append(code)
                self.send_count += 1
                quantity -= 1
                if quantity == 0:
                    break
        for code in self.send_list:
            self.storage.pop(code)
        self.capacity += len(self.send_list)
        print(f'{self.send_count} единиц {equipment_type} отправилось со склада по адресу "{self.address}" '
              f'в {department}')
        if quantity > 0:
            print(f'На складе недостаточно требуемого оборудования. {self.send_count} единиц {equipment_type} '
                  f'отправилось в {department} Ещё {quantity} единиц {equipment_type} необходимо приобрести')


class OfficeEquipment:
    def __init__(self, equipment_code: str, price: float):
        self.equipment_type = 'Офисное оборудование'
        self.equipment_code = equipment_code
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, equipment_code: str, price: float = 20000.0, printer_type: str = 'Лазерный'):
        super().__init__(equipment_code, price)
        self.equipment_type = 'Принтер'
        self.printer_type = printer_type


class Scanner(OfficeEquipment):
    def __init__(self, equipment_code: str, price: float = 15000.0, scan_dpi: int = 800):
        super().__init__(equipment_code, price)
        self.equipment_type = 'Сканер'
        self.scan_dpi = scan_dpi


class MFP(Printer, Scanner):
    def __init__(self, equipment_code: str, printer_type: str = 'Лазерный', scan_dpi: int = 800,
                 price: float = 40000.0, fax: bool = False):
        super().__init__(equipment_code, price)
        self.equipment_type = 'МФУ'
        self.printer_type = printer_type
        self.scan_dpi = scan_dpi
        self.fax = fax


class Shredder(OfficeEquipment):
    def __init__(self, equipment_code: str, price: float = 8000.0, cut_type: str = 'Перекрестный'):
        super().__init__(equipment_code, price)
        self.equipment_type = 'Шреддер'
        self.cut_type = cut_type


if __name__ == '__main__':
    pr1 = [Printer('g4684', 5000, 'Laser'), Printer('1dsf4', 5000, 'Laser'), Printer('wvds6', 5000, 'Laser')]
    pr2 = [Printer('weev5', 5000, 'Laser'), Printer('dsvvv', 5000, 'Laser')]
    pr3 = [Printer('234fs', 5000, 'Laser')]

    wh1 = Warehouse('Город С. Улица Пушкина 28', 20)
    wh2 = Warehouse('Город М. Улица Молдавских Строителей 109', 30)

    wh1.add_equipment(pr1)
    wh1.add_equipment(pr2)
    wh2.add_equipment(pr3)

    supply1 = EquipmentPurchase.buy_from_supplier(Scanner, 6)
    supply2 = EquipmentPurchase.buy_from_supplier(MFP, 4)
    supply3 = EquipmentPurchase.buy_from_supplier(MFP, 100)
    wh1.add_equipment(supply1)
    wh2.add_equipment(supply2)
    wh1.add_equipment(supply3)

    print('-' * 150)
    Warehouse.check_storage(wh1)
    Warehouse.check_storage(wh2)

    print('-'*150)
    wh1.send_to_department('Принтер', 8, 'отделение в городе С.')
    wh1.send_to_department('МФУ', 9, 'офис в городe М.')
    wh2.send_to_department('МФУ', 3, 'отделение в городе С.')

    print('-' * 150)
    Warehouse.check_storage(wh1)

    supply8 = EquipmentPurchase.buy_from_supplier(Shredder, 10)
    wh1.add_equipment(supply8)

"""
На склад по адресу "Город С. Улица Пушкина 28" отправлено 3 единиц оборудования Принтер, осталось место для 17 единиц
На склад по адресу "Город С. Улица Пушкина 28" отправлено 2 единиц оборудования Принтер, осталось место для 15 единиц
На склад по адресу "Город М. Улица Молдавских Строителей 109" отправлено 1 единиц оборудования Принтер, осталось место для 29 единиц
На склад по адресу "Город С. Улица Пушкина 28" отправлено 6 единиц оборудования Сканер, осталось место для 9 единиц
На склад по адресу "Город М. Улица Молдавских Строителей 109" отправлено 4 единиц оборудования МФУ, осталось место для 25 единиц
Склад по адресу "Город С. Улица Пушкина 28" заполнен!
На склад по адресу "Город С. Улица Пушкина 28" отправлено 9 единиц оборудования МФУ, осталось место для 0 единиц
------------------------------------------------------------------------------------------------------------------------------------------------------

Количество оборудования на складе по адресу Город С. Улица Пушкина 28:
Принтер 5
Сканер 6
МФУ 9

Количество оборудования на складе по адресу Город М. Улица Молдавских Строителей 109:
Принтер 1
МФУ 4
------------------------------------------------------------------------------------------------------------------------------------------------------
5 единиц Принтер отправилось со склада по адресу "Город С. Улица Пушкина 28" в отделение в городе С.
На складе недостаточно требуемого оборудования. 5 единиц Принтер отправилось в отделение в городе С. Ещё 3 единиц Принтер необходимо приобрести
9 единиц МФУ отправилось со склада по адресу "Город С. Улица Пушкина 28" в офис в городe М.
3 единиц МФУ отправилось со склада по адресу "Город М. Улица Молдавских Строителей 109" в отделение в городе С.
------------------------------------------------------------------------------------------------------------------------------------------------------

Количество оборудования на складе по адресу Город С. Улица Пушкина 28:
Сканер 6
На склад по адресу "Город С. Улица Пушкина 28" отправлено 10 единиц оборудования Шреддер, осталось место для 4 единиц

Process finished with exit code 0

"""



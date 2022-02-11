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


class EquipmentPurchase:
    @classmethod
    def buy_from_supplier(cls, product, quantity_to_buy):
        purchase_list = []
        for x in range(0, quantity_to_buy):
            purchase_list.append(product(str(random.randrange(1, 10**7))))
        return purchase_list


class Warehouse:
    def __init__(self, address: str, capacity: int,):
        self.capacity = capacity
        self.address = address
        self.storage = {}

    def add_equipment(self, supply):
        self.count = 0
        for equipment in supply:
            if not isinstance(equipment, OfficeEquipment):
                print('Ошибка, склад предназначен для хранения офисного оборудования')
                continue
            self.storage.setdefault(equipment.equipment_code, equipment.equipment_type)
            self.count += 1
            self.capacity -= 1
            if self.capacity == 0:
                print('Склад заполнен!')
                break
        print(f'На склад отправлено {self.count} единиц оборудования, осталось место для {self.capacity} единиц')

    def send_to_department(self, equipment_type: str, quantity: int, department: str):
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
        print(f'{self.count} единиц {equipment_type} отправилось в {department}')
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
    pr1 = Printer('g4684', 5000, 'Laser')
    pr2 = Printer('1dsf4', 5000, 'Laser')
    pr3 = Printer('wvds6', 5000, 'Laser')
    pr4 = Printer('weev5', 5000, 'Laser')
    pr5 = Printer('dsvvv', 5000, 'Laser')
    pr6 = Printer('234fs', 5000, 'Laser')

    wh1 = Warehouse('Город С. Улица Пушкина 28', 20)
    # wh1.add_equipment(pr1, pr2, pr3, pr4, pr5, pr6)

    supply1 = EquipmentPurchase.buy_from_supplier(Scanner, 6)

    wh1.add_equipment(supply1)

    wh1.send_to_department('Принтер', 8, 'отделение в городе С.')
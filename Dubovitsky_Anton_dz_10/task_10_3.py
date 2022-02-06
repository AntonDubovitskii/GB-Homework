class Cell:

    def __init__(self, cells: int):
        self.cells = cells

    def make_order(self, number: int) -> str:
        order_str = ''
        i = self.cells
        for _ in range((self.cells // number)+1):
            if i >= number:
                order_str += ('*' * number + '\n')
                i -= number
            elif i != 0:
                order_str += ('*' * i + '\n')
        return order_str

    def cell_chek(self, other):
        if not isinstance(other, Cell):
            raise TypeError('действие допустимо только для экземпляров того же класса')

    def __add__(self, other):
        self.cell_chek(other)
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        self.cell_chek(other)
        if self.cells >= other.cells:
            return Cell(self.cells - other.cells)
        else:
            raise ValueError('недопустимая операция')

    def __mul__(self, other):
        self.cell_chek(other)
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        self.cell_chek(other)
        if other.cells != 0:
            return Cell(self.cells // other.cells)
        else:
            raise ZeroDivisionError('деление на ноль!')

    def __floordiv__(self, other):
        self.cell_chek(other)
        if other.cells != 0:
            return Cell(self.cells // other.cells)
        else:
            raise ZeroDivisionError('деление на ноль!')


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса


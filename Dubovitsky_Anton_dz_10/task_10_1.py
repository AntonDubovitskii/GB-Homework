from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        if type(matrix) is list and matrix:
            m_str_len = len(matrix[0])
            for item in matrix:
                if len(item) != m_str_len:
                    raise ValueError('fail initialization matrix')
            self.matrix = matrix
        else:
            raise ValueError('fail initialization matrix')

    def __str__(self):
        mat_str = ''
        for x in self.matrix:
            mat_str += f'| {" ".join(map(str, x))} |\n'
        return mat_str

    def __add__(self, other):
        new_matrix = self.matrix
        for x in range(len(new_matrix)):
            for y in range(len(new_matrix[0])):
                new_matrix[x][y] += other.matrix[x][y]
        return Matrix(new_matrix)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """


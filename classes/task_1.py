import numpy as np
from helper import MyClass


class InputMatrix(MyClass):

    """Решение первого задания"""

    def __init__(self) -> None:

        self.vector_string_v()
        self.column_vector_w()
        self.arbitrary_matrix_m()


    def vector_string_v(self) -> None:

        """Вектор строка 'v', размерность 2"""

        self._v = np.array([[
            self.InputDigit('Введите первое число вектор-строки "v": '),
            self.InputDigit('Введите второе число вектор-строки "v": ')
        ]])
    

    def column_vector_w(self) -> None:

        """Вектор столбец 'w' размерность 2"""

        self._w = np.array([
            [self.InputDigit('Введите первое число вектор-столбца "w": ')],
            [self.InputDigit('Введите второе число вектор-столбца "w": ')]
        ])

    
    def arbitrary_matrix_m(self) -> None:

        """Произвольная матрица 'm' 2 на 2"""

        self._m = np.array([

            [self.InputDigit('Введите первое число матрицы "m": '),
            self.InputDigit('Введите второе число матрицы "m": ')],

            [self.InputDigit('Введите третье число матрицы "m": '),
            self.InputDigit('Введите четвертое число матрицы "m": ')]
        ])
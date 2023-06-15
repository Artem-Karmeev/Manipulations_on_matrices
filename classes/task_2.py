import numpy as np
from classes.task_1 import InputMatrix


class GeniratorMatrix(InputMatrix):

    """Решение второго задания"""

    def __init__(self) -> None:
        super().__init__()

        self.zero_matrix_m0()
        self.unit_matrix_m1()
        self.random_matrix_mr()
        self.diagonal_unit_matrix_me()


    def zero_matrix_m0(self) -> None:

        """Матрица 'm0' заполненная нулевыми элементами, размерность 2 на 2"""

        self._m0 = np.array([
            [0, 0],
            [0, 0]
        ])


    def unit_matrix_m1(self) -> None:

        """Матрица 'm1' заполненная единицами, размерность 2 на 2"""

        self._m1 = np.array([
            [1, 1],
            [1, 1]
        ])


    def random_matrix_mr(self, start: int = 0, end: int = 10) -> None:

        """Матрица 'mr' заполнена случайными элементами, размерность 2 на 2"""

        self._mr = np.array([
            [np.random.randint(start, end), np.random.randint(start, end)],
            [np.random.randint(start, end), np.random.randint(start, end)]
        ])


    def diagonal_unit_matrix_me(self) -> None:
        
        """Матрица 'me' c единицами по диагонали, размерность 2 на 2"""

        self._me = np.array([
            [1, np.random.randint(0, 10)],
            [np.random.randint(0, 10), 1]
        ])
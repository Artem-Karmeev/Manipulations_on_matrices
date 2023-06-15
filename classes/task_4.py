import numpy as np

class CheckMatrix:
    def __init__(self, matrix) -> None:

        self.matrix = matrix
        self.count_line = len(matrix)
        self.count_column = len(matrix[0])
        self.max_item = matrix.max()
        self.min_item = matrix.min()
        self.sum_items = matrix.sum()
        self.product_items = np.prod(matrix)


    def __str__(self) -> str:
        text = f"""
        Количество строк: {self.count_line};
        Количество столбцов: {self.count_column};
        Максимальный элемент: {self.max_item};
        Минимальный элемент: {self.min_item};
        Сумма элементов: {self.sum_items};
        Произведение элементов: {self.product_items};"""
        return text

import numpy as np
from classes.task_2 import GeniratorMatrix

class AlphaMatrix(GeniratorMatrix):

    """Решение 3 задания"""

    def create_m(self, number: int) -> np.array:

        """Задает матрицу 'М' по формуле, в зависимости от варианта"""

        match number:

            case 1:
                return self._v * self._w + self._m + self._mr * self._me
            case 2:
                return self._m + self._mr * self._me
            case 3:
                return (self._v / self._m) * (self._mr + self._me)
            case 4:
                return self._w * self._v + self._mr * self._me
            case 5:
                return self._m * self._mr + self._me
            case 6:
                return self._m * self._mr + 100
            case 7:
                return self._v * self._w + self._mr - self._m
            case 8:
                return self._m + self._mr * self._me - 10
            case 9:
                return self._m * self._w + self._mr * self._v
            case 10:
                return self._m + self._mr * self._me
        
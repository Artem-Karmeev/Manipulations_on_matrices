from classes.task_3 import AlphaMatrix
from helper import Helper as hlp
from classes.task_4 import CheckMatrix

matrix = AlphaMatrix()
num = hlp.InputDigit()
m = matrix.create_m(num)
m_data = CheckMatrix(m)


print(matrix)
print('Matrix "M":')
print(m)
print(m_data, '\n')


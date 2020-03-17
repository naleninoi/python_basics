# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, m_list):
        self.m_list = m_list
        for i in range(len(self.m_list)):
            if len(self.m_list[i]) != len(self.m_list[0]):
                raise TypeError('Неверное количество элементов в матрице')

    def __str__(self):
        m_string = ''
        for i in range(len(self.m_list)):
            for j in range(len(self.m_list[i])):
                m_string = m_string + str(self.m_list[i][j]) + '\t'
            m_string = m_string + '\n'
        return m_string

    def __add__(self, other):
        sum_list = []
        for i in range(len(self.m_list)):
            sum_line = []
            for j in range(len(self.m_list[i])):
                sum = self.m_list[i][j] + other.m_list[i][j]
                sum_line.append(sum)
            sum_list.append(sum_line)
        return Matrix(sum_list)


matrix_1 = Matrix([[15, 10, 11, 84], [82, 16, 77, -80], [-10, 12, 101, 5]])
matrix_2 = Matrix([[-78, 12, 11, 34], [85, -16, 77, 2], [90, 24, 70, -54]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)

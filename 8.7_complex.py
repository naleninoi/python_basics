# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, c_number):
        """выборка из строки величин a и b """
        self.c_number = c_number
        for pos, symb in enumerate(self.c_number):
            if symb == '+' or symb == '-' and pos != 0:
                self.a = int(self.c_number[0:pos])
                self.b = int(self.c_number[pos:-1])

    def __str__(self):
        return (self.c_number)

    def __add__(self, other):
        """суммирует a и b, преобразует в строку - вид комплексного числа"""
        c = self.a + other.a
        d = self.b + other.b
        sum = str(c) + str(d) + 'i' if d < 0 else str(c) + '+' + str(d) + 'i'
        return Complex(sum)

    def __mul__(self, other):
        """перемножает a и b, преобразует в строку - вид комплексного числа"""
        c = (self.a * other.a) - (self.b * other.b)
        d = (self.a * other.b) + (self.b * other.b)
        mul = str(c) + str(d) + 'i' if d < 0 else str(c) + '+' + str(d) + 'i'
        return Complex(mul)


c_num_1 = Complex('-102+50i')
c_num_2 = Complex('71-102i')
c_num_3 = Complex('64+31i')
print(c_num_1 + c_num_2)
print(c_num_1 * c_num_2)
print(c_num_1 + c_num_3)
print(c_num_2 * c_num_3)

# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры
# класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return (self.name + ' ' + self.surname)

    def get_total_income(self):
        return (self._income['wage'] + self._income['bonus'])


employee_1 = Position('John', 'Smith', 'agent', 12000, 1500)
print('Full name: {}'.format(employee_1.get_full_name()))
print('Job: {}'.format(employee_1.position))
print('Total income: {}'.format(employee_1.get_total_income()))

employee_2 = Position('Luke', 'Skywalker', 'jedi knight', 14000, 1750)
print('Full name: {}'.format(employee_2.get_full_name()))
print('Job: {}'.format(employee_2.position))
print('Total income: {}'.format(employee_2.get_total_income()))

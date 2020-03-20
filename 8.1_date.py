# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date():
    def __init__(self, date='2000-01-01'):
        self.date = date

    @classmethod
    def str_to_number(cls, date):
        date_num = date.split('-')
        return list(map(int, date_num))

    @staticmethod
    def validate(date):
        print(f'Проверка даты: {date}')
        month = date[1]
        day = date[2]
        check = 0
        check += 1 if month >=1 and month <= 12 else 0
        if month == 2:
            check += 1 if day >=1 and day <= 28 else 0
        if month in [1, 3, 5, 7, 8, 10, 12]:
            check += 1 if day >= 1 and day <= 31 else 0
        if month in [4, 6, 9, 11]:
            check += 1 if day >= 1 and day <= 30 else 0
        print ('Дата ОК') if check == 2 else print('Дата некорректна')


Date.validate(Date.str_to_number('2020-10-28'))
Date.validate(Date.str_to_number('2001-13-26'))
Date.validate(Date.str_to_number('2007-02-30'))

# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class ZeroError(Exception):
    def __init__(self, text):
        self.text = text


check = 0
while not check:
    dividend = int(input('Введите делимое - целое число: '))
    divider = int(input('Введите делитель - целое число: '))
    try:
        if divider == 0:
            raise ZeroError('Деление на ноль невозможно')
    except ZeroError as error_msg:
        print(error_msg)
    else:
        res = dividend / divider
        print(f'Результат деления = {res}')
    finally:
        check = input('Нажмите Enter для повтора (или введите что-нибудь для выхода): ')

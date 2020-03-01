def divide(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        print('Ошибка. Деление на 0.')


number_1 = int(input('Введите делимое число: '))
number_2 = int(input('Введите делитель: '))
print(divide(number_1, number_2))

def string_sum(my_string):
    """ Разбивает строку на числа и подсчитывает их сумму
    Символы, содержащиеся в строке, игнорируются
    """
    sum = 0
    for i in my_string.split(' '):
        try:
            sum = sum + float(i)
        except ValueError:
            sum = sum
    return sum


total_sum = 0
while True:
    my_string = input('Введите несколько чисел, разделенных пробелами, или # - для выхода: ')
    if my_string == '#':
        break
    elif my_string.endswith('#'):
        total_sum += string_sum(my_string)
        print(f'Сумма чисел в строке {string_sum(my_string)}, общая сумма - {total_sum}')
        break
    else:
        total_sum += string_sum(my_string)
        print(f'Сумма чисел в строке {string_sum(my_string)}, общая сумма - {total_sum}')
print('*' * 30 + ' Работа завершена ' + '*' * 30)
